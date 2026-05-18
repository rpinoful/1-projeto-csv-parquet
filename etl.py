import os
import glob
import pandas as pd

# funções:
# 1 - Função que le e consolida o dataframe
# 2 - Função que transforma
# 3 - Função que carrega e salva no formato requerido


pasta = 'data'
def extract(pasta:str)-> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta,'*.json'))
    #Reading dataframes
    dataframes = [pd.read_json(arquivo) for arquivo in arquivos_json]
    #concating dataframes
    df_concat = pd.concat(dataframes,ignore_index=True)
    print(df_concat.to_markdown())
    return df_concat





