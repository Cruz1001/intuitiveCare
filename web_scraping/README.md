# Web Scraping

Este projeto realiza web scraping na página da Agência Nacional de Saúde Suplementar (ANS) para obter os links dos arquivos Anexo I e Anexo II em formato PDF. Os arquivos são baixados e compactados em um arquivo ZIP automaticamente.

## Funcionalidades

- Obtém os links dos PDFs diretamente da página da ANS.
- Realiza o download automático dos arquivos.
- Compacta os PDFs em um arquivo ZIP para armazenamento eficiente.

## Requisitos

Certifique-se de ter instalado:

- Python 3.x

Bibliotecas necessárias:
- requests 
- beautifulsoup4

Para instalar as dependências, execute:

pip install -r requirements.txt

pip install requests beautifulsoup4

Estrutura de Diretórios

O código espera que os PDFs sejam armazenados dentro da pasta web_scraping/arquivos/. Caso a pasta não exista, crie-a antes da execução do script.

web_scraping/
│── arquivos/   Diretório onde os PDFs e o ZIP serão salvos
│── main.py   Código principal

## Como Usar

Execute o script com o comando:

- python script.py

- O script buscará os PDFs na página da ANS e fará o download automático.

- Após o download, os arquivos serão compactados no diretório web_scraping/arquivos/ com o nome rol.zip.

## Explicação do Código

- obter_links_pdf(url): Acessa a página e extrai os links dos PDFs.

- baixar_pdf(url, nome_arquivo): Faz o download dos arquivos.

- criar_arquivo_zip(arquivos_pdf, arquivo_zip): Compacta os PDFs baixados.

- main(): Função principal que gerencia todo o processo.

## Possíveis Erros e Soluções

1. Erro ao baixar arquivos

- Verifique sua conexão com a internet.

- Confirme se a página da ANS está acessível.

- Confira se a estrutura do site não foi alterada.

2. Erro de diretório não encontrado

- Certifique-se de que a pasta web_scraping/arquivos/ existe antes de executar o script.
