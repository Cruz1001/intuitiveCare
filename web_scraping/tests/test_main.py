import os
import pytest
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from web_scraping.main import obter_links_pdf, baixar_pdf, criar_arquivo_zip

BASE_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
PASTA_TESTE = "tests/tmp"

@pytest.fixture
def criar_pasta_teste():
    os.makedirs(PASTA_TESTE, exist_ok=True)
    yield
    # Remove os arquivos após o teste
    for arquivo in os.listdir(PASTA_TESTE):
        os.remove(os.path.join(PASTA_TESTE, arquivo))
    os.rmdir(PASTA_TESTE)

def test_obter_links_pdf():
    url1, url2 = obter_links_pdf(BASE_URL)
    assert url1.endswith(".pdf"), "O link do Anexo I não é um PDF!"
    assert url2.endswith(".pdf"), "O link do Anexo II não é um PDF!"

def test_baixar_pdf(criar_pasta_teste):
    caminho_teste = os.path.join(PASTA_TESTE, "teste.pdf")
    baixar_pdf("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", caminho_teste)
    
    assert os.path.exists(caminho_teste), "O arquivo PDF não foi baixado!"
    assert os.path.getsize(caminho_teste) > 0, "O arquivo PDF está vazio!"

def test_criar_arquivo_zip(criar_pasta_teste):
    pdf1 = os.path.join(PASTA_TESTE, "anexo1.pdf")
    pdf2 = os.path.join(PASTA_TESTE, "anexo2.pdf")

    with open(pdf1, "w") as f: f.write("teste1")
    with open(pdf2, "w") as f: f.write("teste2")

    caminho_zip = os.path.join(PASTA_TESTE, "arquivos.zip")
    criar_arquivo_zip([pdf1, pdf2], caminho_zip)

    assert os.path.exists(caminho_zip), "O arquivo ZIP não foi criado!"
    assert os.path.getsize(caminho_zip) > 0, "O arquivo ZIP está vazio!"

pytest.main()
