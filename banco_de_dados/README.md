# Querys

Este repositório contém scripts SQL utilizados para a criação e população de tabelas relacionadas a planos de saúde, bem como consultas para análise de dados financeiros.

## Estrutura das Tabelas

1. PlanosSaude

Tabela que armazena informações sobre planos de saúde, incluindo dados cadastrais da operadora.

Colunas:

Registro_ANS (INT, PRIMARY KEY): Identificador único do plano de saúde.
CNPJ (VARCHAR(18)): Cadastro Nacional de Pessoa Jurídica.
Razao_Social (VARCHAR(255)): Razão social da operadora.
Nome_Fantasia (VARCHAR(255)): Nome comercial.
Modalidade (VARCHAR(100)): Tipo de operadora.
Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP: Informações de endereço.
DDD, Telefone, Fax: Contatos.
Endereco_eletronico: E-mail.
Representante, Cargo_Representante: Dados do representante legal.
Regiao_de_Comercializacao: Área de atuação do plano.
Data_Registro_ANS (DATE): Data de registro do plano na ANS.

2. ContasContabeis

Tabela que armazena informações contábeis relacionadas aos planos de saúde.

Colunas:

DATA (DATE): Data da movimentação contábil.
REG_ANS (INT): Chave estrangeira referenciando a tabela PlanosSaude.
CD_CONTA_CONTABIL (VARCHAR(50)): Código da conta contábil.
DESCRICAO (VARCHAR(255)): Descrição da conta.
VL_SALDO_INICIAL (MONEY): Saldo inicial.
VL_SALDO_FINAL (MONEY): Saldo final.

## Importação de Dados

Os dados são carregados a partir de arquivos CSV utilizando o comando COPY. Os seguintes arquivos são utilizados:

- Relatorio_cadop.csv para a tabela PlanosSaude.
- 1T2023.csv, 2T2023.csv, 3T2023.csv, 4T2023.csv para dados contábeis de 2023.
- 1T2024.csv, 2T2024.csv, 3T2024.csv, 4T2024.csv para dados contábeis de 2024.

## Consultas SQL

1. Operadoras_despesas_ano

Consulta que retorna as 10 operadoras de planos de saúde com maiores despesas relacionadas a eventos/sinistros em 2024.


2. Operadoras_despesas_trimestre

Consulta que retorna as 10 operadoras de planos de saúde com maiores despesas no quarto trimestre de 2024.

## Requisitos
- PostgreSQL 17
- Arquivos CSV no diretório C:\Program Files\PostgreSQL\17\data\Data\

## Como Utilizar

- Tenha certeza que as configurações do seu banco de dados estão definidas para aceitar dados em português, devido ao fato das colunas relacionadas a dinheiro utilizarem "," como separador decimal.
- Execute o script "estruturar_tabelas".
- Execute o script "importar_dados".
- Utilize as consultas SQL "operadoras_despesas_ano" e "operadoras_despesas_trimestre", para obter insights sobre os dados financeiros das operadoras de planos de saúde.



