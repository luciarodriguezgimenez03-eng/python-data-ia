import peewee
import datetime

data_base = peewee.PostgresqlDatabase('postgres', user='Lucia', password='lrglrglrg56657667lrglrglrg8900',
                                      host='localhost', port=5432)

class Usuario(peewee.Model):
    nombre_Usuario=peewee.CharField(unique=True)
    email_Usuario=peewee.CharField()
    fecha_Usuario=peewee.DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = data_base
        db_table = "usuarios"
if __name__=="__main__":
    if not Usuario.table_exists():
        Usuario.create_table()

    entrada_nombre_Usuario = input("Nombre Usuario: ")
    entrada_email_Usuario = input("Email Usuario: ")

    if Usuario.select().where(Usuario.nombre_Usuario==entrada_nombre_Usuario).exists():
        print("Usuario ya existe")
    else:
        new_Usuario = Usuario.create(nombre_Usuario=entrada_nombre_Usuario, email_Usuario=entrada_email_Usuario)
        new_Usuario.save()
