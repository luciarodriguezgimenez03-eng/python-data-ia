from peewee import *

data_base=PostgresqlDatabase('postgres', user='Lucia', password='lrglrglrg56657667lrglrglrg8900',
                                      host='localhost', port=5432)
class Profesores(Model):
    maestro_id=AutoField()
    nombre=CharField()
    apellido=CharField()
    telefono=CharField()
    email = CharField(unique=True)
    class Meta:
        database = data_base
class Clases(Model):
    clase_id=AutoField()
    cod_curso=CharField()
    fecha_inicio_curso= DateField()
    fecha_fin_curso=DateField()
    horario=CharField()
    maestro_id = ForeignKeyField(Profesores)
    class Meta:
        database=data_base




if __name__=="__main__":
    if not Profesores.table_exists() and not Clases.table_exists():
        data_base.create_tables([Profesores, Clases])
    elif not Profesores.table_exists():
        Profesores.create_table()
    elif not Clases.table_exists():
        Clases.create_table()

maestro = Profesores(nombre='Paula',
                     apellido='Gutierrez',
                     telefono='876 56 56 56',
                     email='pgutierrez@gamil.com')
if Profesores.select().where(Profesores.email==maestro.email).exists():
    print("Profesor ya existe")
else:
    maestro.save()




for profesor in Profesores.select():
    print('Nombre:{}-Apellido:{}-Teléfono{}-Email{}'.format(profesor.nombre, profesor.apellido, profesor.telefono, profesor.email))


