CREATE TABLE PlanosSaude (
    Registro_ANS INT PRIMARY KEY,
    CNPJ VARCHAR(18) NOT NULL,
    Razao_Social VARCHAR(255) NOT NULL,
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(100),
    Logradouro VARCHAR(255),
    Numero VARCHAR(20),
    Complemento VARCHAR(255),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP VARCHAR(10),
    DDD CHAR(2),
    Telefone VARCHAR(20),
    Fax VARCHAR(15),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(255),
    Regiao_de_Comercializacao VARCHAR(255),
    Data_Registro_ANS DATE
);

CREATE TABLE ContasContabeis (
    DATA DATE NOT NULL,
    REG_ANS INT,
    CD_CONTA_CONTABIL VARCHAR(50) NOT NULL,
    DESCRICAO VARCHAR(255) NOT NULL,
    VL_SALDO_INICIAL MONEY NOT NULL,
    VL_SALDO_FINAL MONEY NOT NULL
);
