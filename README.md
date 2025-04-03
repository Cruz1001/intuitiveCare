# intuitiveCare

Este repositório contém a implementação dos quatro testes de nivelamento exigidos, cobrindo Web Scraping, Transformação de Dados, Banco de Dados e API.
Cada teste foi desenvolvido utilizando Python, POSTGRE e Vue.js, conforme solicitado.

projeto/
│── web_scraping/             # Teste 1 - Extração e compactação de arquivos PDF  
│   ├── main.py               # Script principal para scraping  
│   ├── tests/                # Testes automatizados com pytest  
│── transformação_dados/      # Teste 2 - Extração e transformação de dados  
│   ├── main.py               # Script principal para transformação de dados  
│   ├── tests/                # Testes automatizados com pytest  
│── banco_de_dados/           # Teste 3 - Manipulação de banco de dados   
│── api/                      # Teste 4 - Desenvolvimento de API  
│   ├── backend/              # Servidor em Python com FastAPI  
│   ├── frontend/             # Interface em Vue.js  
│   ├── tests/                # Testes de API  
│── README.md                 # Documentação geral 
│── requirements.txt          # Lista de dependências  

## Teste 1 - Web Scraping
### Objetivo:

- Baixar PDFs do site da ANS.

- Compactar os arquivos em um ZIP.

### Execução:

- python web_scraping/main.py

### Testes:

- pytest web_scraping/tests/
  
## Teste 2 - Transformação de Dados
### Objetivo:

- Extrair tabelas do Anexo I do PDF.

- Salvar os dados em um CSV.

- Compactar o CSV em um ZIP.

### Execução:
- python transformação_dados/main.py

### Testes:

- pytest transformação_dados/tests/

## Teste 3 - Banco de Dados

### Objetivo:

- Criar tabelas no banco de dados.

- Importar os dados dos CSVs.
  
- Executar consultas analíticas.

### Execução:

- Configurar conexão com PostgreSQL.

- Rodar os scripts SQL na pasta banco_de_dados.

## Teste 4 - API
### Objetivo:

- Criar um backend para consulta de operadoras de saúde.
- Desenvolver um frontend em Vue.js.

### Execução:

- cd api/backend && uvicorn main:app --reload  
- cd api/frontend && npm run serve  

### Testes:

- pytest api/tests/
