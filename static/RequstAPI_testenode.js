
const axios = require('axios');

// URL da sua API local
const apiUrl = 'http://127.0.0.1:8000';

// Função para fazer uma requisição GET para a API
async function getTiposPassos() {
    try {
        const response = await axios.get(`${apiUrl}/TiposPassos/`);
        console.log('Tipos de Passos:', response.data);
    } catch (error) {
        console.error('Erro ao obter tipos de passos da API:', error);
    }
}

// Exemplo de uso
getTiposPassos();
