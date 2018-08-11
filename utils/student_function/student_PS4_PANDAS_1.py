## Ejercicio del estudiante

import pandas as pd
import numpy as np

df=pd.read_csv("data/PS4_1.csv" , parse_dates=True) 
    

def ps4_1(df):
    df.index = pd.to_datetime(df.Date)#eliminar
    del(df["Date"]) #eliminar
    del(df["Unnamed: 1"]) #eliminar
    
    registros= df.shape[0]
    cols= len(df.columns)
    menor= df.columns[-1]
    memoria= df.memory_usage().sum()
    maximo=df['Maisonneuve_1'].max()
    
    r=[registros,cols,menor,memoria,maximo] #respuesta
    
    
    
    return r