<template>
  <div>
    <h1>Operadoras</h1>
    <input v-model="query" @input="buscarOperadoras" placeholder="Buscar por nome fantasia" />
    
    <table v-if="operadoras.length">
  <thead>
    <tr>
      <th>Registro ANS</th>
      <th>CNPJ</th>
      <th>Razão Social</th>
      <th>Nome Fantasia</th>
      <th>Modalidade</th>
      <th>Logradouro</th>
      <th>Número</th>
      <th>Complemento</th>
      <th>Bairro</th>
      <th>Cidade</th>
      <th>UF</th>
      <th>CEP</th>
      <th>DDD</th>
      <th>Telefone</th>
      <th>Fax</th>
      <th>Endereço Eletrônico</th>
      <th>Representante</th>
      <th>Cargo</th>
      <th>Região</th>
      <th>Data de Registro ANS</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="operadora in operadoras" :key="operadora.Registro_ANS">
      <td>{{ operadora.Registro_ANS }}</td>
      <td>{{ operadora.CNPJ }}</td>
      <td>{{ operadora.Razao_Social }}</td>
      <td>{{ operadora.Nome_Fantasia }}</td>
      <td>{{ operadora.Modalidade }}</td>
      <td>{{ operadora.Logradouro }}</td>
      <td>{{ operadora.Numero }}</td>
      <td>{{ operadora.Complemento }}</td>
      <td>{{ operadora.Bairro }}</td>
      <td>{{ operadora.Cidade }}</td>
      <td>{{ operadora.UF }}</td>
      <td>{{ operadora.CEP }}</td>
      <td>{{ operadora.DDD }}</td>
      <td>{{ operadora.Telefone }}</td>
      <td>{{ operadora.Fax }}</td>
      <td>{{ operadora.Endereco_eletronico }}</td>
      <td>{{ operadora.Representante }}</td>
      <td>{{ operadora.Cargo_Representante }}</td>
      <td>{{ operadora.Regiao_de_Comercializacao }}</td>
      <td>{{ operadora.Data_Registro_ANS }}</td>
    </tr>
  </tbody>
</table>

    <p v-else>Sem resultados para a busca...</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      operadoras: [],
    };
  },
  methods: {
    async buscarOperadoras() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/buscar-operadoras?query=${this.query}`);
        this.operadoras = response.data;
      } catch (error) {
        console.error('Erro ao buscar operadoras:', error);
      }
    },
  },
  created() {
    this.buscarOperadoras(); // Carregar todas as operadoras inicialmente
  },
};
</script>

<style scoped>
/* Estilos para melhorar a visualização da tabela */
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}
</style>
