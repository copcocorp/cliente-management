// src/services/api.js
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const clientesAPI = {
  getAll: async () => {
    try {
      const response = await api.get('/api/clientes/');
      return response.data; // devuelve la lista de clientes
    } catch (error) {
      console.error('Error cargando clientes:', error);
      throw error;
    }
  },

  get: async (id) => {
    try {
      const response = await api.get(`/api/clientes/${id}/`);
      return response.data;
    } catch (error) {
      console.error('Error obteniendo cliente:', error);
      throw error;
    }
  },

  create: async (data) => {
    try {
      const response = await api.post('/api/clientes/', data);
      return response.data;
    } catch (error) {
      console.error('Error creando cliente:', error);
      throw error;
    }
  },

  update: async (id, data) => {
    try {
      const response = await api.put(`/api/clientes/${id}/`, data);
      return response.data;
    } catch (error) {
      console.error('Error actualizando cliente:', error);
      throw error;
    }
  },

  delete: async (id) => {
    try {
      const response = await api.delete(`/api/clientes/${id}/`);
      return response.data;
    } catch (error) {
      console.error('Error eliminando cliente:', error);
      throw error;
    }
  },
};

export default api;
