import os
import glob
import pandas as pd

pasta = 'data'
arquivos_json = glob.glob(os.path.join(pasta,'*.json'))


#Reading dataframes
dataframes = [pd.read_json(arquivo) for arquivo in arquivos_json]
df_concat = pd.concat(dataframes,ignore_index=True)
print(df_concat.to_markdown())
