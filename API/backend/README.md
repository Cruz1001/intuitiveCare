# API

Esta API foi desenvolvida em FastAPI para fornecer informações sobre operadoras de saúde a partir de um arquivo CSV. Ela permite buscar operadoras filtrando pelo Nome Fantasia.

## Bibliotecas utilizadas

- Pandas
- FastAPI

## Endpoints

GET /buscar-operadoras

Descrição: Retorna uma lista de operadoras filtradas pelo Nome Fantasia.

### Parâmetros:

query (opcional): Termo de busca no Nome Fantasia

Exemplo de Requisição:

curl -X 'GET' 'http://127.0.0.1:8000/buscar-operadoras?query=Amil' -H 'accept: application/json'

Exemplo de Resposta:

[
  {
    "Registro_ANS": "123456",
    "CNPJ": "00.000.000/0001-00",
    "Razao_Social": "Amil Assistência Médica Ltda.",
    "Nome_Fantasia": "Amil",
    "Modalidade": "Medicina de Grupo",
    "Logradouro": "Rua Exemplo",
    "Numero": "100",
    "Complemento": "Sala 1",
    "Bairro": "Centro",
    "Cidade": "São Paulo",
    "UF": "SP",
    "CEP": "01000-000",
    "DDD": "11",
    "Telefone": "4002-8922",
    "Fax": "",
    "Endereco_eletronico": "contato@amil.com.br",
    "Representante": "João Silva",
    "Cargo_Representante": "Diretor",
    "Regiao_de_Comercializacao": "Nacional",
    "Data_Registro_ANS": "2000-01-01"
  }
]


