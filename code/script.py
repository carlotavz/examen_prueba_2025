# code/script.py
import pandas as pd

def cargar_datos(path):
    return pd.read_csv(path, delimiter=";")

def procesar_fechas(df):
    df['dt'] = pd.to_datetime(df['dt'])
    df['year'] = df['dt'].dt.year
    return df

if __name__ == "__main__":
    df = cargar_datos("data/datos_mock.csv")
    df = procesar_fechas(df)
    print(df.head())
