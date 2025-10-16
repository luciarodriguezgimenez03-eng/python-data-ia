import csv


with open("info.txt", "w") as file:
    file.write("1,12345678A,Ana Torres,Paseo de la Reforma 123,987654321\n")
    file.write("2,23456789B,Carlos Gomez,Av. Libertador 456,876543219\n")
    file.write("3,34567890C,Rita Alvarez,Calle Falsa 789,765432198\n")

with open("info.txt", "r") as file:
    lines = file.readlines()


for line in lines:
    fields = line.strip().split(',')
    id_ = fields[0]
    id_document = fields[1]
    name = fields[2]
    address = fields[3]
    phone = fields[4]

    print(f"ID: {id_} | DOCUMENTO: {id_document} | NOMBRE: {name} | DIRECCIÓN: {address} | TELÉFONO: {phone}")
