import pandas as pd

df = pd.read_csv("C:/Users/pablo/Desktop/proyecto_final/2017PurchasePricesDec.csv")

#print(df.head())
#print(df.info())

mask = df.isna().any(axis=1)          # Series booleana por fila
rows_mask= df[mask]               #solo filas con nulos

print(rows_mask)

columns = df.columns

#cambie el tipo de dato 'object' a 'string'
for column in columns:
    if df[column].dtype == 'object':
        df[column]=df[column].astype('string')

df=df.dropna()

print(df.info())

#como era una fila con 3 columnas de valor nulo, considere eliminarla ya que no afectaria el analisis.
    
