import pandas as pd
archivo = '/Users/javier/GIT/Boletas_emitir/valores.xlsx'

df = pd.read_excel(archivo, sheet_name='Sheet1' ,header=None)


for i in range (9):

    x = df.loc[i,0]
    print(str(x))
