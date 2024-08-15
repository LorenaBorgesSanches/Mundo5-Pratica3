import pandas as pd
import numpy as np

file_path = './picoWeb.csv'
dataSet = pd.read_csv(file_path, sep=';', engine='python', encoding='utf-8', quotechar='\'', )

print("Informações gerais sobre o conjunto de dados:")
print(dataSet.info())

print("\nPrimeiras N linhas do arquivo:")
print(dataSet.head())

print("\nÚltimas N linhas do arquivo:")
print(dataSet.tail())

dataSetCopy = dataSet.copy()

dataSetCopy['Calories'] = dataSetCopy['Calories'].fillna(0)

print("\nConjunto de dados após substituir valores nulos em 'Calories':")
print(dataSetCopy)

dataSetCopy['Date'] = dataSetCopy['Date'].fillna('1900/01/01')

print("\nConjunto de dados após substituir valores nulos em 'Date':")
print(dataSetCopy)


# O erro apresentado é que '20201226' não é uma data válida.
# 1900/01/01 é sim uma data válida e não causa exceção.
# Mas vou deixar o código conforme orientado na missão.

try:
    dataSetCopy['Date'] = pd.to_datetime(dataSetCopy['Date'], format='%Y/%m/%d')
except ValueError as e:
    print(f"\nErro ao converter 'Date': {e}")

dataSetCopy['Date'] = dataSetCopy['Date'].replace('1900/01/01', np.nan)

# Não há mudança, uma vez que o probema não é o '1900/01/01'
try:
    dataSetCopy['Date'] = pd.to_datetime(dataSetCopy['Date'], format='%Y/%m/%d')
except ValueError as e:
    print(f"\nErro ao converter 'Date': {e}")

print("\nConjunto de dados após transformar 'Date' para datetime:")
print(dataSetCopy)

dataSetCopy['Date'] = dataSetCopy['Date'].replace('20201226', pd.to_datetime('20201226', format='%Y%m%d'))
dataSetCopy['Date'] = pd.to_datetime(dataSetCopy['Date'])

print("\nConjunto de dados após a última transformação de 'Date':")
print(dataSetCopy)

dataSetCopy = dataSetCopy.dropna(subset=['Date'])

print("\nDataframe final após todas as transformações:")
print(dataSetCopy)
