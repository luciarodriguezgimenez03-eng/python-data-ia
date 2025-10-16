from peewee import *

data_base=PostgresqlDatabase('postgres', user='Lucia', password='lrglrglrg56657667lrglrglrg8900',
                                      host='localhost', port=5432)
class Profesores(Model):
    maestro_id=AutoField()
    nombre=CharField()
    appelido=CharField()
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

