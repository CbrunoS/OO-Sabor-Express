from modelos.restaurante import Restaurante


def main():
    restaurante_lanche = Restaurante('Lanchonete', 'Hamburgueria')
    restaurante_lanche.receber_avaliacao('Gui', 2)
    restaurante_lanche.receber_avaliacao('Lais', 4)
    restaurante_lanche.receber_avaliacao('Gabi', 5)

    restaurante_pizza = Restaurante('Pizza Planet', 'Pizzaria')
    restaurante_pizza.alternar_estado()
    restaurante_pizza.receber_avaliacao('Bruno', 5)
    restaurante_pizza.receber_avaliacao('Pedro', 3)
    restaurante_pizza.receber_avaliacao('Jennifer', 4)

    restaurante_mexicano = Restaurante('El Texano', 'Mexicana')
    restaurante_mexicano.receber_avaliacao('Maria', 3)
    restaurante_mexicano.receber_avaliacao('João', 1)
    restaurante_mexicano.receber_avaliacao('Ana', 3)

    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()