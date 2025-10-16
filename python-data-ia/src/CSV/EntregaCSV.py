
import csv


with open("datos.txt", "w") as file:
    file.write("112345678Luis MarcoCalle los Alamos12345678\n")
    file.write("229345678Pepe PelaAvda. los Olmos  012345678\n")
    file.write("334567891Juan RuizCalle los Rudisc 901234567\n")


with open("datos.txt", "r") as file:
    lines = file.readlines()


for line in lines:
    codigo = line[0:1]
    dni = line[1:9]
    nombre = line[9:19]
    calle = line[19:35]
    telefono = line[35:44]

    print(f"CODIGO: {codigo} | DNI: {dni} | NOMBRE: {nombre} | CALLE: {calle} | TELEFONO: {telefono}")