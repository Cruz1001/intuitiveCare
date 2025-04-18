# Transformação de dados

Este projeto realiza a extração de tabelas de um arquivo PDF, consolida os dados em um arquivo CSV e compacta o resultado em um arquivo ZIP.

## Requisitos

Antes de executar o script, certifique-se de ter as seguintes bibliotecas instaladas:
- tabula-py 
- pandas

Além disso, é necessário ter o Java instalado, pois o tabula-py depende do Tabula, que requer Java.

## Estrutura do Projeto

transformação_dados/
│── arquivos/
│   ├── anexo1.pdf   PDF de entrada
│   ├── tabelas_consolidadas.csv   CSV gerado
│   ├── Teste_Vinicius.zip   Arquivo ZIP gerado
│── main.py   Script principal

## Como Funciona

- Extração de Tabelas: O script utiliza a biblioteca tabula-py para extrair tabelas do PDF.

- Transformação dos Dados: As tabelas extraídas são consolidadas em um DataFrame e renomeadas conforme padrões definidos.

- Exportação para CSV: O DataFrame é salvo como um arquivo CSV.

- Compactação: O CSV é compactado em um arquivo ZIP.

## Como Executar

Execute o script com o seguinte comando:

python main.py

O processo iniciará a extração, processamento e compactação dos dados.

## Testes Automatizados

Para garantir que as funções estão funcionando corretamente, há um conjunto de testes localizados na pasta transformação_dados/tests/.
Os testes verificam:

- Se as tabelas são extraídas corretamente do PDF.

- Se o arquivo CSV é gerado corretamente e não está vazio.

- Se o processo de compactação funciona corretamente, garantindo que o CSV está dentro do ZIP.

- Como Executar os Testes

Os testes devem ser executados a partir do diretório transformação_dados/tests/. Para rodá-los, utilize o comando:
- pytest test_main.py

Isso executará os testes e exibirá os resultados no terminal.
## Possíveis Problemas e Soluções

- Erro relacionado ao Java: Certifique-se de que o Java está instalado e configurado no PATH do sistema.

- Nenhuma tabela extraída: Tente alterar o parâmetro lattice para False na função extrair_tabelas.

- Erros ao processar CSV: Verifique se as tabelas foram corretamente extraídas e se o formato do PDF é compatível com a extração automatizada.