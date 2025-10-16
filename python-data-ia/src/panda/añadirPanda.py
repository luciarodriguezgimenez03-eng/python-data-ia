import pandas as pd

df_nueva = pd.DataFrame(columns=['Ciudad', 'Poblacion', 'Limpia', 'Año'])

df_nueva=df_nueva._append({'Ciudad': 'Barcelona', 'Poblacion' : 520000, 'Limpia': True, 'Año':980},
                          ignore_index=True)

print(df_nueva)