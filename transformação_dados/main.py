import tabula
import pandas as pd
import zipfile
import os

PDF_PATH = "transformação_dados/arquivos/anexo1.pdf"
CSV_PATH = "transformação_dados/arquivos/tabelas_consolidadas.csv"
ZIP_PATH = "transformação_dados/arquivos/Teste_Vinicius.zip"

PAGINA_INICIAL = 3
PAGINA_FINAL = 181


def extrair_tabelas(pdf_path, pagina_inicial, pagina_final):
    try:
        tabelas = tabula.read_pdf(
            pdf_path,
            pages=f"{pagina_inicial}-{pagina_final}",  # Processa todas as páginas juntas
            lattice=True,  # Tente mudar para False se não funcionar
            multiple_tables=True,
            silent=True
        )
        print(f"Total de tabelas extraídas: {len(tabelas)}")
        return tabelas if tabelas else []
    except Exception as e:
        print(f"Erro ao extrair tabelas: {str(e)}")
        return []


def salvar_csv(tabelas, csv_path):
    if tabelas:
        df = pd.concat(tabelas, ignore_index=True)
        df_final = df.rename(
            columns={
                "OD": "Seg. Odontológica",
                "AMB": "Seg. Ambulatorial",
                "HCO": "Seg. Hospitalar Com Obstetrícia",
                "HSO": "Seg. Hospitalar Sem Obstetrícia",
                "REF": "Plano Referência",
                "PAC": "Procedimento de Alta Complexidade",
                "DUT": "Diretriz de Utilização",
            }
        )

        df_final.to_csv(csv_path, index=False, encoding="utf-8-sig")
        print(f"\nArquivo CSV salvo em: {csv_path}")
        return csv_path
    else:
        print("Nenhuma tabela foi extraída para consolidar.")
        return None


def compactar_csv(csv_path, zip_path):
    if os.path.exists(csv_path):
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(csv_path, arcname=os.path.basename(csv_path))
        print(f"\nArquivo ZIP salvo em: {zip_path}")
        return zip_path
    else:
        print("Erro: O arquivo CSV não existe para ser compactado.")
        return None


def main():
    print("Iniciando extração de tabelas...\n")

    tabelas = extrair_tabelas(PDF_PATH, PAGINA_INICIAL, PAGINA_FINAL)

    csv_gerado = salvar_csv(tabelas, CSV_PATH)
    if csv_gerado:
        compactar_csv(csv_gerado, ZIP_PATH)


main()
