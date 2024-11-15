import os

# Nome do arquivo para simular o banco de dados
DB_FILE = "clientes.txt"

# Função para inicializar o arquivo do "banco de dados"
def inicializar_banco():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as db:
            db.write("idcliente,nome,limite\n")  # Cabeçalho do arquivo

# Função para listar todos os clientes
def listar_clientes():
    print("\nClientes cadastrados:")
    with open(DB_FILE, "r") as db:
        linhas = db.readlines()[1:]  # Ignora o cabeçalho
        if not linhas:
            print("Nenhum cliente cadastrado.")
        for linha in linhas:
            idcliente, nome, limite = linha.strip().split(",")
            print(f"ID: {idcliente}, Nome: {nome}, Limite: {limite}")

# Função para exibir os detalhes de um cliente específico
def exibir_cliente():
    listar_clientes()
    idcliente = input("\nDigite o ID do cliente para ver os detalhes: ")
    cliente = buscar_cliente(idcliente)

    if cliente:
        print("\nDetalhes do cliente:")
        print(f"ID: {cliente['idcliente']}")
        print(f"Nome: {cliente['nome']}")
        print(f"Limite: {cliente['limite']}")
    else:
        print("Cliente não encontrado.")

# Função para buscar cliente por ID
def buscar_cliente(idcliente):
    with open(DB_FILE, "r") as db:
        for linha in db.readlines()[1:]:
            dados = linha.strip().split(",")
            if dados[0] == idcliente:
                return {"idcliente": dados[0], "nome": dados[1], "limite": dados[2]}
    return None

# Função para atualizar cliente
def atualizar_cliente(idcliente, novo_nome, novo_limite):
    atualizado = False
    with open(DB_FILE, "r") as db:
        linhas = db.readlines()

    with open(DB_FILE, "w") as db:
        for linha in linhas:
            dados = linha.strip().split(",")
            if dados[0] == idcliente:
                db.write(f"{idcliente},{novo_nome},{novo_limite}\n")
                atualizado = True
            else:
                db.write(linha)

    return atualizado

# Função para alterar cliente
def alterar_cliente():
    listar_clientes()
    idcliente = input("\nDigite o ID do cliente que deseja alterar: ")
    cliente = buscar_cliente(idcliente)

    if not cliente:
        print("Cliente não encontrado.")
        return

    print(f"\nDados do cliente selecionado:")
    print(f"ID: {cliente['idcliente']}, Nome: {cliente['nome']}, Limite: {cliente['limite']}")

    # Simula transação
    print("\nIniciando transação...")
    cliente_atualizado = buscar_cliente(idcliente)

    # Verifica se o registro foi alterado durante a transação
    if cliente_atualizado == cliente:
        novo_nome = input("Digite o novo nome: ")
        novo_limite = input("Digite o novo limite: ")

        if atualizar_cliente(idcliente, novo_nome, novo_limite):
            confirmacao = input("Deseja confirmar a alteração? (s/n): ").strip().lower()
            if confirmacao == "s":
                print("Alteração confirmada!")
            else:
                # Simula rollback revertendo a escrita
                atualizar_cliente(idcliente, cliente["nome"], cliente["limite"])
                print("Alteração cancelada!")
        else:
            print("Erro ao atualizar cliente.")
    else:
        print("O registro foi alterado por outro processo. Operação abortada.")

# Função para adicionar clientes (apenas para testes iniciais)
def adicionar_cliente(nome, limite):
    with open(DB_FILE, "r") as db:
        linhas = db.readlines()

    ultimo_id = int(linhas[-1].split(",")[0]) if len(linhas) > 1 else 0
    novo_id = ultimo_id + 1

    with open(DB_FILE, "a") as db:
        db.write(f"{novo_id},{nome},{limite}\n")

# Menu principal
def menu():
    inicializar_banco()

    while True:
        print("\nMenu:")
        print("1. Listar clientes")
        print("2. Ver detalhes de um cliente")
        print("3. Alterar cliente")
        print("4. Adicionar cliente")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_clientes()
        elif opcao == "2":
            exibir_cliente()
        elif opcao == "3":
            alterar_cliente()
        elif opcao == "4":
            nome = input("Digite o nome do cliente: ")
            limite = input("Digite o limite do cliente: ")
            adicionar_cliente(nome, limite)
            print("Cliente adicionado com sucesso!")
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu()
