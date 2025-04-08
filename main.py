# Analise_de_dados

a = 'Analise_de_Dados'

print('ola mundo!',a)

"""-------------------------"""
import pandas as pd

print("versao do pandas =",pd.__version__)

# biblioteca de datasets
import kagglehub

# Download latest version ( baixando DATASETS da alura)
path = kagglehub.dataset_download("murilomorgado/dados-alura-python-para-data-science")

# mostrando o link para download
print("Path to dataset files:", path)


# exibindo os dados do dataset-telecon
dados_churn = pd.read_json("dataset-telecon.json")
print(dados_churn)