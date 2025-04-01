import pandas as pd
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:8081", 
    "http://127.0.0.1:8081",  
    "*", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)
# Lendo o CSV
df = pd.read_csv("C:\\Users\\vinio\\OneDrive\\Área de Trabalho\\intuitiveCare\\intuitiveCare\\API\\Arquivos\\Relatorio_cadop.csv", delimiter=';')

# Modelo para as operadoras
class Operadora(BaseModel):
    Registro_ANS: int
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
async def buscar_operadoras(query: str = ""):
    if query:
        resultados = df[df['Nome_Fantasia'].str.contains(query, case=False, na=False)] 
    else:
        resultados = df

    # Convertendo os valores para strings e tratando valores nulos (NaN) para todos os campos
    operadoras = [
        Operadora(
            Registro_ANS=row['Registro_ANS'] if pd.notna(row['Registro_ANS']) else 0,
            CNPJ=str(row['CNPJ']) if pd.notna(row['CNPJ']) else '',
            Razao_Social=row['Razao_Social'] if pd.notna(row['Razao_Social']) else '',
            Nome_Fantasia=row['Nome_Fantasia'] if pd.notna(row['Nome_Fantasia']) else '',
            Modalidade=row['Modalidade'] if pd.notna(row['Modalidade']) else '',
            Logradouro=row['Logradouro'] if pd.notna(row['Logradouro']) else '',
            Numero=row['Numero'] if pd.notna(row['Numero']) else '',
            Complemento=str(row['Complemento']) if pd.notna(row['Complemento']) else '',
            Bairro=row['Bairro'] if pd.notna(row['Bairro']) else '',
            Cidade=row['Cidade'] if pd.notna(row['Cidade']) else '',
            UF=row['UF'] if pd.notna(row['UF']) else '',
            CEP=str(row['CEP']) if pd.notna(row['CEP']) else '',
            DDD=str(row['DDD']) if pd.notna(row['DDD']) else '',
            Telefone=str(row['Telefone']) if pd.notna(row['Telefone']) else '',
            Fax=str(row['Fax']) if pd.notna(row['Fax']) else '',
            Endereco_eletronico=row['Endereco_eletronico'] if pd.notna(row['Endereco_eletronico']) else '',
            Representante=row['Representante'] if pd.notna(row['Representante']) else '',
            Cargo_Representante=row['Cargo_Representante'] if pd.notna(row['Cargo_Representante']) else '',
            Regiao_de_Comercializacao=str(row['Regiao_de_Comercializacao']) if pd.notna(row['Regiao_de_Comercializacao']) else '',
            Data_Registro_ANS=str(row['Data_Registro_ANS']) if pd.notna(row['Data_Registro_ANS']) else ''
        )
        for index, row in resultados.iterrows()
    ]
    
    return operadoras
