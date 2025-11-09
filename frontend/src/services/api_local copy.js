// src/services/api.js
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const clientesAPI = {
  // Obtener todos los clientes
  getAll: () => api.get('/clientes/'),
  
  // Obtener cliente por ID
  getById: (id) => api.get(`/clientes/${id}/`),
  
  // Crear nuevo cliente
  create: (cliente) => api.post('/clientes/', cliente),
  
  // Actualizar cliente
  update: (id, cliente) => api.put(`/clientes/${id}/`, cliente),
  
  // Eliminar cliente
  delete: (id) => api.delete(`/clientes/${id}/`),
};

export default api;