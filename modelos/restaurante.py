from modelos.avaliacao import Avaliacao


class Restaurante:
    restaurantes = []

    def __init__(self, nome: str, categoria: str):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'{self._nome} | {self._categoria}'

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def categoria(self) -> str:
        return self._categoria

    @property
    def ativo(self) -> str:
        return '✅' if self._ativo else '❌'

    def alternar_estado(self) -> None:
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente: str, nota: float) -> None:
        if not 0 < nota <= 5:
            raise ValueError('A nota deve estar entre 1 e 5.')

        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'

        soma = sum(avaliacao.nota for avaliacao in self._avaliacoes)
        quantidade = len(self._avaliacoes)
        return round(soma / quantidade, 1)

    @classmethod
    def listar_restaurantes(cls) -> None:
        print(
            f'{"Nome do restaurante".ljust(25)} | '
            f'{"Categoria".ljust(20)} | '
            f'{"Avaliação".ljust(10)} | '
            f'Status'
        )

        for restaurante in cls.restaurantes:
            print(
                f'{restaurante.nome.ljust(25)} | '
                f'{restaurante.categoria.ljust(20)} | '
                f'{str(restaurante.media_avaliacoes).ljust(10)} | '
                f'{restaurante.ativo}'
            )