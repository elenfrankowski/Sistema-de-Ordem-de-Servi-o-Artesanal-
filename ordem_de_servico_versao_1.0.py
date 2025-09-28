#Primeira Parte: Cadastro de Materiais
materiais = []

def cadastrar_material():
    print("\n---Cadastro de Material---")
    nome = input("Nome do material: ")
    unidade = input("Unidade de medida (ex: g, m, un, ml): ")
    qtd_total = float(input(f"Quantidade total comprada ({unidade}): "))
    valor_total = float(input("Valor total pago por essa quantidade (R$): "))

    valor_unitario = valor_total / qtd_total

    material = {
        "nome": nome,
        "unidade": unidade,
        "qtd_total": qtd_total,
        "valor_total": valor_total,
        "valor_unitario": valor_unitario
    }

    materiais.append(material)
    print(f"Material '{nome}' cadastrado com sucesso!")
    print(f"Valor unitário calculado: R${valor_unitario:.4f} por {unidade}.")

#Listagem dos Materiais
def listar_materiais():
    print("\n---Lista de Materiais Cadastrados---")
    if not materiais:
        print("Nenhum material cadastrado ainda.")
    else:
        for i, mat in enumerate(materiais, start=1):
            print(f"{i}. {mat['nome']} - R${mat['valor_unitario']:.4f} por {mat['unidade']}")
            print("-------------------------------------------------")

#Menu Inicial
while True:
    print("\n---MATERIAIS---")
    print("1. Cadastrar Material")
    print("2. Listar Materiais")
    print("3. Sair")

    opcao = input("Selecione uma opção: ")

    if opcao == '1':
        cadastrar_material()
    elif opcao == '2':
        listar_materiais()
    elif opcao == '3':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente Novamente")