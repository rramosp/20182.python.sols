## Ejercicio del estudiante

import pandas as pd

def ps4_2():
    df=pd.read_csv("data/PS4_1.csv" , parse_dates=True)
    df.index = pd.to_datetime(df.Date)
    del(df["Date"])
    del(df["Unnamed: 1"])
    
    r=[]
    Berri_media=df['Berri1'].mean()
    Berri_std=df['Berri1'].std()
    Berri_max= df['Berri1'].max()
    Berri_min= df['Berri1'].min()
    Berri_75=df['Berri1'].quantile(0.75)
    
    Maiso1_media= df['Maisonneuve_1'].mean()
    Maiso1_std= df['Maisonneuve_1'].std()
    Maiso1_max= df['Maisonneuve_1'].max()
    Maiso1_min= df['Maisonneuve_1'].min()
    Maiso1_75= df['Maisonneuve_1'].quantile(0.75)
    
    
    Maiso2_media= df['Maisonneuve_2'].mean()
    Maiso2_std= df['Maisonneuve_2'].std()
    Maiso2_max= df['Maisonneuve_2'].max()
    Maiso2_min= df['Maisonneuve_2'].min()
    Maiso2_75= df['Maisonneuve_2'].quantile(0.75)
    
    
    Brebeuf_media= df['Brebeuf'].mean()
    Brebeuf_std= df['Brebeuf'].std()
    Brebeuf_max= df['Brebeuf'].max()
    Brebeuf_min= df['Brebeuf'].min()
    Brebeuf_75= df['Brebeuf'].quantile(0.75)
    
    r+=[Berri_media,Berri_std, Berri_max,Berri_min, Berri_75]
    r+=[Maiso1_media,Maiso1_std,Maiso1_max,Maiso1_min,Maiso1_75]
    r+=[Maiso2_media,Maiso2_std,Maiso2_max,Maiso2_min ,Maiso2_75 ]
    r+=[Brebeuf_media,Brebeuf_std,Brebeuf_max,Brebeuf_min,Brebeuf_75 ]
    
    return r
    