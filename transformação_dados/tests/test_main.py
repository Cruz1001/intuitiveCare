import os
import pytest
import pandas as pd
import zipfile
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from transformação_dados.main import extrair_tabelas, salvar_csv, compactar_csv

PDF_PATH = "transformação_dados/arquivos/anexo1.pdf"
CSV_TEST_PATH = "transformação_dados/arquivos/teste_tabelas.csv"
ZIP_TEST_PATH = "transformação_dados/arquivos/teste_arquivos.zip"

PAGINA_INICIAL = 3
PAGINA_FINAL = 5  

@pytest.fixture
def limpar_arquivos():
    yield
    if os.path.exists(CSV_TEST_PATH):
        os.remove(CSV_TEST_PATH)
    if os.path.exists(ZIP_TEST_PATH):
        os.remove(ZIP_TEST_PATH)

def test_extrair_tabelas():
    tabelas = extrair_tabelas(PDF_PATH, PAGINA_INICIAL, PAGINA_FINAL)
    assert isinstance(tabelas, list), "A função deve retornar uma lista"
    assert len(tabelas) > 0, "Nenhuma tabela foi extraída do PDF"

def test_salvar_csv(limpar_arquivos):
    tabelas = extrair_tabelas(PDF_PATH, PAGINA_INICIAL, PAGINA_FINAL)
    csv_path = salvar_csv(tabelas, CSV_TEST_PATH)
    
    assert csv_path is not None, "A função deve retornar o caminho do arquivo CSV"
    assert os.path.exists(csv_path), "O arquivo CSV não foi criado"
    
    df = pd.read_csv(csv_path)
    assert not df.empty, "O arquivo CSV está vazio"

def test_compactar_csv(limpar_arquivos):
    tabelas = extrair_tabelas(PDF_PATH, PAGINA_INICIAL, PAGINA_FINAL)
    csv_path = salvar_csv(tabelas, CSV_TEST_PATH)
    zip_path = compactar_csv(csv_path, ZIP_TEST_PATH)
    
    assert zip_path is not None, "A função deve retornar o caminho do ZIP"
    assert os.path.exists(zip_path), "O arquivo ZIP não foi criado"
    
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        assert CSV_TEST_PATH.split("/")[-1] in zipf.namelist(), "O CSV não está dentro do ZIP"


pytest.main()
