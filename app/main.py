from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def raiz():
    return{"mensagem" : "API FastAPI funcionada"}

@app.get("/health")
def healt():
    return {"status" : "ok"}

@app.get("/soma")
def soma(a: int, b: int):
    return {"Resultado:" : a + b}

# @app.get("/sub")
# def sub(a: int, b: int):
#     return {"Resultado:" : a - b}

class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False

@app.post("/tarefas")
def criar_tarefa(tarefa : Tarefa):
    return {
        "mensagem" : "Tarefa recebida com sucesso",
        "dados" : tarefa
    }