class Avaliacao:
    def __init__(self, cliente: str, nota: float):
        self._cliente = cliente
        self._nota = nota

    @property
    def cliente(self) -> str:
        return self._cliente

    @property
    def nota(self) -> float:
        return self._nota