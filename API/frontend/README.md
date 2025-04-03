# Frontend Vue - Consulta de Operadoras

Este é um projeto frontend desenvolvido em Vue.js para consulta de operadoras de saúde. Ele permite buscar operadoras por nome fantasia e exibe os resultados em uma tabela com informações detalhadas.

## Tecnologias Utilizadas

- Vue.js 3
- Axios (para requisições HTTP)
- Vue CLI

## Estrutura do Projeto

frontend/
│── src/
│   ├── components/
│   │   ├── OperadorasList.vue   Componente principal para exibir as operadoras
│   ├── App.vue                  Componente raiz
│   ├── main.js                  Arquivo principal de inicialização
│── public/
│   ├── index.html               Arquivo HTML principal
│── package.json                 Configurações e dependências
│── README.md                    Documentação do projeto

## Instalação e Execução

Para rodar o projeto localmente:

Instale as dependências:

- npm install

Inicie o servidor de desenvolvimento:

- npm run serve

O projeto estará disponível em http://localhost:8080/ por padrão.

## Uso

- Digite um nome fantasia no campo de busca para filtrar as operadoras.
- A tabela exibe informações como Registro ANS, CNPJ, Razão Social, entre outros.

## API

O frontend consome uma API que retorna as operadoras com base na consulta do usuário. A API deve estar rodando localmente em http://127.0.0.1:8000/buscar-operadoras.

Melhorias Futuras

Adicionar paginação aos resultados.
Melhorar a responsividade da tabela para dispositivos móveis.

