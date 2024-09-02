import pandas as pd

datos = pd.read_excel('counties.xlsx')
datos.drop_duplicates()
datos.dropna(axis=0, how='any')

caracteres = [')','(','?',';',':','.','&','%','$','#','"','_','-', ' ']
i = 0
for d in datos['county']:
    for c in caracteres:
        if c in d:
            datos['county'] = datos['county'].str.replace(c,'')
    i+=1

datos.to_excel('datoslimpios.xlsx')