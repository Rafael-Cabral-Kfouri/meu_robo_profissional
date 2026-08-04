import datetime
import pandas as pd

#simulação de coleta de dados   
def coletar_dados():
    return [
        {"data": datetime.date.today(), "evento": "Processamento finalizado", "status": "Sucesso"},
    ]

#salvar em um csv
def salvar_relatorio(dados):
    df = pd.DataFrame(dados)
    df.to_csv('dados/relatorio.csv', index=False)
    print("Relatório salvo em 'dados/relatorio.csv'.")

#Execução principal
if __name__ == "__main__":
    print("Iniciando robô...")
    dados = coletar_dados()
    salvar_relatorio(dados)