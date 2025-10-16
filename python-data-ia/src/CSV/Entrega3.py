import csv

# Escribir el archivo con una sola columna
with open("datos2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["1123456789Ana Torres    Paseo de la Reforma 123987654321"])
    writer.writerow(["2234567890Carlos Gomez Av. Libertador 456    876543219"])
    writer.writerow(["3345678901Rita Alvarez Calle Falsa 789       765432198"])

# Leer el archivo como CSV
with open("datos2.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        # Extraer cada campo basado en su posición fija
        line = row[0]
        codigo = line[0:1]
        dni = line[1:9]
        nombre = line[9:19].strip()
        calle = line[19:35].strip()
        telefono = line[35:44]

    # Imprimir los datos
print(f"CODIGO: {codigo} | DNI: {dni} | NOMBRE: {nombre} | CALLE: {calle} | TELEFONO: {telefono}")
