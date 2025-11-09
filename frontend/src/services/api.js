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
      console.log('Clientes cargados:', response.data);
      return response.data;
    } catch (error) {
      console.error('Error cargando clientes:', error);
      if (error.response) {
        console.error('Respuesta del servidor:', error.response.status, error.response.data);
      } else if (error.request) {
        console.error('No se recibió respuesta del servidor:', error.request);
      } else {
        console.error('Error configurando la petición:', error.message);
      }
      throw error;  // Para que la UI sepa que falló
    }
  },
  // ...otros métodos (getById, create, etc.)
};

export default api;
