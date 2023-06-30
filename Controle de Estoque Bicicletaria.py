# ---- Início das Variáveis Globais ----
lista_peca = []
codigo_peca = 0
# ------ Fim das Variáveis Globais -----

# ------ Inicio de cadastrarPeca() -----
def cadastrarPeca(codigo):
    print('\nVocê selecionou a opção de CADASTRAR PEÇA!') #Inicio do Menu Cadastrar
    print('Código do Produto: {}'.format(codigo)) #Programa gera um código
    nome = input('Por favor entre com o NOME da peça: ') #Programa solicita nome para cadastrar a peça
    fabricante = input('Por favor entre com o FABRICANTE da peça: ') #Programa solicita frabricante para cadastrar a peça
    valor = int(input('Por favor entre com o VALOR(R$) da peça: ')) #Programa solicita valor para cadastrar a peça
    #Dicionário guarda as informações inseridas em lista
    dicionario_peca = {'codigo': codigo,
                        'nome': nome,
                        'fabricante': fabricante,
                        'valor': valor}
    lista_peca.append(dicionario_peca.copy())
# ------- Fim de cadastrarPeca() -------

# ------ Inicio de consultarPeca() -----
def consultarPeca():
    print('\nVocê selecionou a opção de CONSULTAR PEÇAS!') #Inicio do Menu Consultar
    while True: #Inicio do laço Consultar
        # Menu de consulta + oções
        opcao_consultar = input('Escolha a opção desejada:\n' +
                                '1 - Consultar TODAS as Peças\n' +
                                '2 - Consultar Peças por CÓDIGO\n' +
                                '3 - Consultar Peças por FABRICANTE\n' +
                                '4 - Retornar\n' +
                                '>>> ')
        if opcao_consultar == '1': # Opção 1 - Consultar TODAS as Peças
            for peca in lista_peca:  # produto vai varrer toda a lista de produtos
                print('-------------------------')
                for key, value in peca.items():  # varrer todos os conjuntos (chave e valor) do dicionario
                    print('{}: {}'.format(key, value))
                print('-------------------------')
        elif opcao_consultar == '2': # Opção 2 - Consultar Peças por CÓDIGO
            valor_desejado = int(input('Digite o CÓDIGO da Peça: '))
            for peca in lista_peca:
                if peca['codigo'] == valor_desejado:  # valor do campo código desse dicionário é igual ao desejado
                    print('-------------------------')
                    for key, value in peca.items():  # varrer todos os conjuntos (chave e valor) do dicionario
                        print('{}: {}'.format(key, value))
                    print('-------------------------')
        elif opcao_consultar == '3': # Opção 3 - Consultar Peças por FABRICANTE
            valor_desejado = input('Digite o FABRICANTE da Peça: ')
            for peca in lista_peca:
                if peca['fabricante'] == valor_desejado:  # valor do campo código desse dicionário é igual ao desejado
                    print('-------------------------')
                    for key, value in peca.items():  # varrer todos os conjuntos (chave e valor) do dicionario
                        print('{}: {}'.format(key, value))
                    print('-------------------------')
        elif opcao_consultar == '4': # Opção 4 - Retornar
            return  # sai da função consultar e volta ao menu principal
        else: #Caso digite outra opção sem ser as disponiveis no menu
            print('Opção Inválida. Tente novamente.')
            continue  # volta ao menu de consulta
# ------- Fim de consultarPeca() -------

# ------ Inicio de removerPeca() -----
def removerPeca():
    print('\nVocê selecionou a opção de REMOVER PEÇA!') #Inicio do Menu Remover
    valor_desejado = int(input('Digite o código da peça a ser removida: '))
    for peca in lista_peca:
        if peca['codigo'] == valor_desejado:  # valor do campo código desse dicionário é igual ao desejado
            lista_peca.remove(peca)
            print('Peça removida.')
# ------- Fim de removerPeca() -------

# Inicio do programa
print('Bem Vindo ao Controle de Estoque da Bicicletaria da Mayara Castro S.A.')  # Identificador pessoal
while True: #Inicio do laço principal
    #Menu principal + oções
    menu_principal = input('Escolha a opção desejada:\n' +
                                '1 - Cadastrar Peças\n' +
                                '2 - Consultar Peças\n' +
                                '3 - Remover Peças\n' +
                                '4 - Sair\n'+
                                '>> ')
    # Organizando a ordem das "def" e declarando as variáveis para a saída no console.
    if menu_principal == '1': #1 - Cadastrar Peças
        codigo_peca = codigo_peca+1 #Codificando as peças cadastradas
        cadastrarPeca(codigo_peca)
    elif menu_principal == '2': # Opção 2 - Consultar Peças
        consultarPeca()
    elif menu_principal == '3': # Opção 3 - Remover Peças
        removerPeca()
    elif menu_principal == '4': # Opção 4 - Sair
        break #encerra o laço principal e o programa acaba o programa
    else:
        print('Opção Inválida. Tente novamente.') #Caso digite outra opção sem ser as disponiveis no menu
        continue #volta ao menu principal