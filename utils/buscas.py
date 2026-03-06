def buscar_por_categoria(restaurantes, categoria):
    resultados = []

    for restaurante in restaurantes:
        if restaurante.categoria.lower() == categoria.lower():
            resultados.append(restaurante)
    
    return resultados

def buscar_por_nome(restaurantes, nome):
    resultados = []

    for restaurante in restaurantes:
        if nome.lower() in restaurante.nome.lower():
            resultados.append(restaurante)            

    return resultados