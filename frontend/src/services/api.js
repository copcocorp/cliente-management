import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const clientesAPI = {
  getAll: () => api.get('/api/clientes/'),
  getById: (id) => api.get(`/api/clientes/${id}/`),
  create: (cliente) => api.post('/api/clientes/', cliente),
  update: (id, cliente) => api.put(`/api/clientes/${id}/`, cliente),
  delete: (id) => api.delete(`/api/clientes/${id}/`),
};

export default api;