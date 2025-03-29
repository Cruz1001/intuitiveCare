import os
import requests
import zipfile
from bs4 import BeautifulSoup
import re

def baixar_pdf(url, nome_arquivo):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(nome_arquivo, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo {nome_arquivo} baixado com sucesso.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo {nome_arquivo}: {e}")

def criar_arquivo_zip(arquivo_pdf, arquivo_zip):
    try:
        with zipfile.ZipFile(arquivo_zip, 'w') as zipf:
            for pdf in arquivo_pdf:
                zipf.write(pdf, arcname=os.path.basename(pdf))
        print(f"Arquivos compactados com sucesso em {arquivo_zip}.")
    except Exception as e:
        print(f"Erro ao criar o arquivo ZIP: {e}")

def obter_links_pdf(url):
    try:
        request = requests.get(url)
        request.raise_for_status()
        soup = BeautifulSoup(request.content, 'html.parser')

        anexo1 = soup.find('a', text=re.compile(r"Anexo I"), href=re.compile(r".pdf"))
        anexo2 = soup.find('a', text=re.compile(r"Anexo II"), href=re.compile(r".pdf"))

        if not anexo1 or not anexo2:
            print("Não foi possível encontrar os anexos PDF.")
            return None, None
        
        url_anexo1 = anexo1['href']
        url_anexo2 = anexo2['href']
        return url_anexo1, url_anexo2
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter os links dos PDFs: {e}")
        return None, None

def main():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    
    # Obtém os links dos PDFs
    url_anexo1, url_anexo2 = obter_links_pdf(url)
    
    if not url_anexo1 or not url_anexo2:
        return  # Sai da execução se os links não forem encontrados
    
    # Baixar os arquivos PDF
    baixar_pdf(url_anexo1, 'web_scraping/arquivos/anexo1.pdf')
    baixar_pdf(url_anexo2, 'web_scraping/arquivos/anexo2.pdf')
    
    # Compactar os PDFs em um arquivo ZIP
    arquivos_pdf = ['web_scraping/arquivos/anexo1.pdf', 'web_scraping/arquivos/anexo2.pdf']
    criar_arquivo_zip(arquivos_pdf, 'web_scraping/arquivos/rol.zip')

main()