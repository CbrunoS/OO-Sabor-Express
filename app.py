from servicos.api_restaurantes import obter_dados_restaurantes
from utils.formatador import exibir_restaurantes
from utils.buscas import buscar_por_categoria, buscar_por_nome

def menu():
    print('\nSabor Express API')
    print('1 - Listar Restaurantes')
    print('2 - Buscar por categoria')
    print('3 - Buscar por nome')
    print('4 - Sair')

def main():
    dados_api = obter_dados_restaurantes()

    while True:
        menu()
        opcao = input('Escolha uma opção:')

        if opcao == '1':
            exibir_restaurantes(dados_api)

        elif opcao == '2':
            categoria = input ('Digite a categoria: ')
            resultados = buscar_por_categoria(dados_api, categoria)

            if resultados:
                exibir_restaurantes(resultados)

            else:
                print('Nenhum restaurante encontrado.')
        
        elif opcao == '3':
            nome = input('Digite o nome do restaurante: ')
            resultados = buscar_por_nome(dados_api, nome)

            if resultados:
                exibir_restaurantes(resultados)
            else:
                print('Nenhum restaurante encontrado')
        
        elif opcao == '4':
            print('Encerrando sistema.')
            break
        
        else:
            print('Opção inválida.')

if __name__ == "__main__":
    main()