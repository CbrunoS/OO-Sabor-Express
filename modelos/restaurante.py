class Restaurante:
    restaurantes = []

    def __init__(self, id: int, nome: str, categoria: str, endereco: str):
        self._id = id
        self._nome = nome.title()
        self._categoria = categoria
        self._endereco = endereco

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._endereco}'
    
    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def endereco(self):
        return self._endereco