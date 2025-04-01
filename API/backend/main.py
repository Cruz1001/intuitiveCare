import pandas as pd
from fastapi import FastAPI, Query
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

CSV_PATH = "..\\Arquivos\\Relatorio_cadop.csv"


df = pd.read_csv(CSV_PATH, delimiter=';')

def tratar_valor(valor):
    if pd.isna(valor):
        return ""
    return str(int(valor)) if isinstance(valor, (int, float)) and not isinstance(valor, bool) else str(valor)

df = df.fillna("").astype(str)

class Operadora(BaseModel):
    Registro_ANS: str
    CNPJ: str
    Razao_Social: str
    Nome_Fantasia: str
    Modalidade: str
    Logradouro: str
    Numero: str
    Complemento: str
    Bairro: str
    Cidade: str
    UF: str
    CEP: str
    DDD: str
    Telefone: str
    Fax: str
    Endereco_eletronico: str
    Representante: str
    Cargo_Representante: str
    Regiao_de_Comercializacao: str
    Data_Registro_ANS: str

@app.get("/buscar-operadoras", response_model=List[Operadora])
async def buscar_operadoras(query: str = Query("", min_length=0)):
    """Retorna uma lista de operadoras filtradas pelo Nome Fantasia."""
    resultados = df[df['Nome_Fantasia'].str.contains(query, case=False, na=False)] if query else df
    return [Operadora(**{col: tratar_valor(valor) for col, valor in row.items()}) for row in resultados.to_dict(orient="records")]
