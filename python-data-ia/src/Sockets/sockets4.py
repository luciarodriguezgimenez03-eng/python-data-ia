from fastapi import FastAPI
app = FastAPI(title="SOMOS seg DAM", description="Se estudian Apis", version="1.0.1")

songs = [
    {
        "Id": 1,
        "Titulo": "asdasda",
        "Cantante": "Alan",
        "duracion": 240

    },
    {
        "Id": 2,
        "Titulo": "akjhdasd",
        "Cantante": "Cris",
        "duracion": 280

    }
]

@app.get('/')
def index():
    return ('Hola desde el servidor')
@app.get('/songs')
def index():
    return songs
@app.get('/seleccion/{id}')
def busco(id:int):
    for selecto in songs:
        if selecto['id'] == id:
            return selecto