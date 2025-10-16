import csv

fichero_trabajo=''

with open('C:\\Users\\USUARIO\\prueba.csv' , newline='') as temporal:

    data = csv.reader(temporal,delimiter=";")

    fichero_trabajo=list(data)

print(fichero_trabajo)