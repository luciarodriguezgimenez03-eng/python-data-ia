import csv

fichero_trabajo=''

with open('C:\\Users\\USUARIO\\prueba.csv' , newline='') as temporal:
    data = csv.reader(temporal, delimiter=";")
    fichero_trabajo = list(data)

for i in range(1, len(fichero_trabajo)):
    for j in range(len(fichero_trabajo[i])):
        print(fichero_trabajo[0][j] + ' : ', fichero_trabajo[i][j])
