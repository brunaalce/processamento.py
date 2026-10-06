import pandas as pd
import os

def carregar_e_analisar(caminho_arquivo):
    """Lê um arquivo CSV ou Excel e exibe um resumo básico."""
    if not os.path.exists(caminho_arquivo):
        print(f"Atenção: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None

    try:
        if caminho_arquivo.endswith('.csv'):
            df = pd.read_csv(caminho_arquivo)
        elif caminho_arquivo.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(caminho_arquivo)
        else:
            print("Formato de arquivo não suportado.")
            return None

        print(f"Sucesso! {len(df)} linhas carregadas.")
        print("\nPrimeiras linhas do arquivo:")
        print(df.head())
        return df
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return None

if __name__ == "__main__":
    # Exemplo de uso
    arquivo = "dados.xlsx"
    carregar_e_analisar(arquivo)
