import pandas as pd


elx=['Elche', 200000, True, 1080]
ali=['Alicante', 300000, False, 1290]
sp=['SantaPola', 100000, True, 1800]
sj=['SanJuan', 2000, False, 1905]
sv=['SanVicente', 45000, False, 1953]
mm=['MuchaMiel', 16500, True, 2001]

lista_rrss=[elx,ali,sp,sj,sv,mm]

df_rrss = pd.DataFrame(lista_rrss,
                       columns=['Ciudad', 'Poblacion', 'Limpia', 'Año'])

print(df_rrss.loc[2,'Ciudad'])
print(df_rrss.loc[3,'Poblacion'])

print(df_rrss.iloc[3])

print(df_rrss[df_rrss['Poblacion']<20000])

