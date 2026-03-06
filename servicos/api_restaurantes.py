from modelos.restaurante import Restaurante
import requests

def obter_dados_restaurantes():
    url = "https://fakerestaurantapi.runasp.net/api/Restaurant"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        dados = response.json()
    except requests.RequestException as e:
        print(f'Erro ao acessar API: {e}')
        return []

    restaurantes = []

    for item in dados:

        restaurante = Restaurante(
            item["restaurantID"],
            item["restaurantName"],
            item["type"],
            item["address"]
        )

        restaurantes.append(restaurante)

    return restaurantes