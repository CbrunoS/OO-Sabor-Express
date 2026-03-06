from fastapi import FastAPI, Query
from servicos.api_restaurantes import obter_dados_restaurantes
from utils.buscas import buscar_por_categoria, buscar_por_nome

app = FastAPI()


@app.get("/")
def home():
    return {"mensagem": "API do OO-Sabor Express funcionando"}


@app.get("/restaurantes")
def listar_restaurantes():
    restaurantes = obter_dados_restaurantes()

    return [
        {
            "id": restaurante.id,
            "nome": restaurante.nome,
            "categoria": restaurante.categoria,
            "endereco": restaurante.endereco,
        }
        for restaurante in restaurantes
    ]


@app.get("/restaurantes/buscar")
def buscar_restaurantes_por_categoria(categoria: str = Query(...)):
    restaurantes = obter_dados_restaurantes()
    resultados = buscar_por_categoria(restaurantes, categoria)

    return [
        {
            "id": restaurante.id,
            "nome": restaurante.nome,
            "categoria": restaurante.categoria,
            "endereco": restaurante.endereco,
        }
        for restaurante in resultados
    ]

@app.get("/restaurantes/buscar-nome")
def buscar_restaurantes_por_nome(nome: str = Query(...)):
    restaurantes = obter_dados_restaurantes()
    resultados = buscar_por_nome(restaurantes, nome)

    return [
        {
            "id": restaurante.id,
            "nome": restaurante.nome,
            "categoria": restaurante.categoria,
            "endereco": restaurante.endereco,
        }
        for restaurante in resultados
    ]

@app.get("/restaurantes/{restaurante_id}")
def obter_restaurante_por_id(restaurante_id: int):
    restaurantes = obter_dados_restaurantes()

    for restaurante in restaurantes:
        if restaurante.id == restaurante_id:
            return {
                "id": restaurante.id,
                "nome": restaurante.nome,
                "categoria": restaurante.categoria,
                "endereco": restaurante.endereco,
            }
        
        return {"erro": "Restaurante não encontrado"}