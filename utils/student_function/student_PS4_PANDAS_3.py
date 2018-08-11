## Ejercicio del estudiante

import pandas as pd
import datetime
def fix_century(x): #ayuda 
        year = x.year - 100 if x.year > 1989 else x.year
        return datetime.date(year, x.month, x.day)

data=pd.read_csv('data/PS4_2.data', sep='\s+', parse_dates = [[0,1,2]])
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)
data["Yr_Mo_Dy"] = pd.to_datetime(data["Yr_Mo_Dy"])
data = data.set_index('Yr_Mo_Dy')

def ps4_3(data):

    data.loc[:,'month']=data.index.month

    january_winds = data.query('month == 1')

    r=january_winds.loc[:,'RPT':"MAL"].mean().values

    return r