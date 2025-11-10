// src/App.jsx
import React, { useState, useEffect } from 'react';
import { clientesAPI } from './services/api';
import ClienteForm from './components/ClienteForm';
import ClienteTable from './components/ClienteTable';

function App() {
  const [clientes, setClientes] = useState([]);
  const [clienteEdit, setClienteEdit] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [loading, setLoading] = useState(false);

  // Cargar clientes
  const loadClientes = async () => {
    try {
      setLoading(true);
      const clientesData = await clientesAPI.getAll();
      setClientes(clientesData);
    } catch (error) {
      console.error('Error cargando clientes:', error);
      alert('Error al cargar los clientes');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadClientes();
  }, []);

  // Crear o actualizar cliente
  const handleSaveCliente = async (clienteData) => {
    try {
      if (clienteEdit) {
        await clientesAPI.update(clienteEdit.id, clienteData);
      } else {
        await clientesAPI.create(clienteData);
      }
      await loadClientes(); // recargar la lista
      setShowForm(false);
      setClienteEdit(null);
    } catch (error) {
      console.error('Error guardando cliente:', error);
      alert('Error al guardar el cliente');
    }
  };

  // Editar cliente
  const handleEdit = (cliente) => {
    setClienteEdit(cliente);
    setShowForm(true);
  };

  // Eliminar cliente
  const handleDelete = async (id) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este cliente?')) {
      try {
        await clientesAPI.delete(id);
        await loadClientes();
      } catch (error) {
        console.error('Error eliminando cliente:', error);
        alert('Error al eliminar el cliente');
      }
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <div className="container mx-auto px-4">
        <h1 className="text-3xl font-bold text-gray-800 mb-8 text-center">
          Sistema de Gestión de Clientes
        </h1>

        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-xl font-semibold text-gray-700">Lista de Clientes</h2>
            <button
              onClick={() => {
                setClienteEdit(null);
                setShowForm(true);
              }}
              className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg transition duration-200"
            >
              Agregar Cliente
            </button>
          </div>

          {showForm && (
            <ClienteForm
              cliente={clienteEdit}
              onSave={handleSaveCliente}
              onCancel={() => {
                setShowForm(false);
                setClienteEdit(null);
              }}
            />
          )}

          {loading ? (
            <div className="text-center py-8">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto"></div>
              <p className="mt-2 text-gray-600">Cargando clientes...</p>
            </div>
          ) : (
            <ClienteTable
              clientes={clientes}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
