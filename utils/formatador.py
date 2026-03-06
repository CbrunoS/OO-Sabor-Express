def exibir_restaurantes(restaurantes):
    print(f'Total de restaurantes: {len(restaurantes)}\n')

    for restaurante in restaurantes:
        print(f'Nome: {restaurante._nome}')
        print(f'Categoria: {restaurante._categoria}')
        print(f'Endereço: {restaurante._endereco}')
        print("-"*30)