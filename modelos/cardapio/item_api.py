from modelos.cardapio.item_cardapio import ItemCardapio

class ItemAPI(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def aplicar_desconto(self):
        pass