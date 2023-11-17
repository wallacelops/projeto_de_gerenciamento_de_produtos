# Funcao para carregar produtos do arquivo
def carregar_produtos():
    try:
        with open("produtos.txt", "r") as file:
            for linha_num, linha in enumerate(file, start=1):
                dados = linha.strip().split(":")
                if len(dados) == 2:
                    chave = dados[0].strip()
                    valor = dados[1].strip()
                    if chave == "ID":
                        id_produto = valor
                        produtos[id_produto] = {}
                    else:
                        produtos[id_produto].setdefault(chave, valor)
                else:
                    print(f"Formato inválido na linha {linha_num}: {linha}")
    except FileNotFoundError:
        print("Arquivo de produtos ainda não existe.")
    except Exception as e:
        print(f"Erro ao carregar produtos: {e}")

# Funcao para salvar produtos no arquivo
def salvar_produtos():
    try:
        with open("produtos.txt", "w") as file:
            for id_produto, produto in produtos.items():
                file.write(f"ID: {id_produto}\n")
                file.write(f"Nome: {produto.get('Nome', 'N/A')}\n")
                file.write(f"Especificacoes: {produto.get('Especificacoes', 'N/A')}\n")
                file.write(f"Quantidade: {produto.get('Quantidade', 'N/A')}\n")
                file.write(f"Descricao: {produto.get('Descricao', 'N/A')}\n")

                valor = produto.get('Valor')
                if valor is not None:
                    file.write(f"Valor: {formatar_valor(valor)}\n")
                else:
                    file.write("Valor: N/A\n")

                file.write("\n")
        print("Produtos salvos com sucesso!")
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
    except Exception as e:
        print(f"Erro ao salvar produtos: {e}")

def formatar_valor(valor):
    return f"R$ {valor:.2f}" if valor is not None else "N/A"

# Funcao para exibir o menu principal
def menu_principal():
    print("Boas vindas ao nosso sistema:\n")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("3 - Listar produtos cadastrados")
    print("4 - Atualizar cadastro")
    print("5 - Excluir cadastro")
    print("6 - Sair")

# Funcao para cadastrar um produto
def cadastrar_produto():
    while True:
        try:
            id_produto = input("Informe o ID do medicamento (somente números): ")
            if not id_produto.isdigit():
                raise ValueError("ID deve conter apenas números.")

            nome = input("Informe o nome do medicamento: ")
            especificacoes = input("Informe as especificacoes dos medicamentos: ")
            quantidade = int(input("Informe a quantidade dos medicamentos no estoque: "))
            descricao = input("Informe uma descricao da medicacao (opcional): ")
            valor = float(input("Informe o valor da medicacao: "))

            produtos[id_produto] = {
                "Nome": nome,
                "Especificacoes": especificacoes,
                "Quantidade": quantidade,
                "Descricao": descricao,
                "Valor": valor
            }
            salvar_produtos()
            print("Produto cadastrado com sucesso!")
            break 
        except ValueError as ve:
            print(f"Erro ao cadastrar produto: {ve}")
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}")

# Funcao para consultar um produto
def consultar_produto():
    id_produto = input("Informe o ID do produto que deseja consultar: ")
    produto = produtos.get(id_produto)
    if produto:
        print(f"ID: {id_produto}")
        for chave, valor in produto.items():
            print(f"{chave}: {valor}")
    else:
        print("Produto nao encontrado!")

# Função para listar produtos cadastrados
def listar_produtos():
    for id_produto, produto in produtos.items():
        print(f"ID: {id_produto}")
        print(f"Nome: {produto.get('Nome', 'N/A')}")
        print(f"Especificacoes: {produto.get('Especificacoes', 'N/A')}")
        print(f"Quantidade: {produto.get('Quantidade', 'N/A')}")
        print(f"Descricao: {produto.get('Descricao', 'N/A')}")

        valor = produto.get('Valor')
        if isinstance(valor, (int, float)):
            print(f"Valor: {formatar_valor(valor)}")
        else:
            print("Valor: N/A")

        print("-" * 70)

# Funcao para atualizar cadastro de um produto
def atualizar_cadastro():
    id_produto = input("Informe o ID do produto que deseja atualizar: ")
    produto = produtos.get(id_produto)
    if produto:
        print("Atualize os campos necessários:")
        nome = input(f"Nome ({produto['Nome']}): ")
        especificacoes = input(f"Especificacoes ({produto['Especificacoes']}): ")
        quantidade = input(f"Quantidade ({produto['Quantidade']}): ")
        descricao = input(f"Descricao ({produto['Descricao']}): ")
        valor = input(f"Valor ({produto['Valor']}): ")

        # Atualize os valores apenas se forem fornecidos
        if nome:
            produto['Nome'] = nome
        if especificacoes:
            produto['Especificacoes'] = especificacoes
        if quantidade:
            produto['Quantidade'] = int(quantidade)
        if descricao:
            produto['Descricao'] = descricao
        if valor:
            produto['Valor'] = float(valor)

        salvar_produtos()
        print("Cadastro atualizado com sucesso!")
    else:
        print("Produto nao encontrado!")

# Funcao para excluir cadastro de um produto
def excluir_cadastro():
    id_produto = input("Informe o ID do produto que deseja excluir: ")
    if id_produto in produtos:
        del produtos[id_produto]
        salvar_produtos()
        print("Cadastro excluído com sucesso!")
    else:
        print("Produto nao encontrado!")

# Funcao principal
def main():
    carregar_produtos()
    while True:
        menu_principal()
        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            consultar_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            atualizar_cadastro()
        elif opcao == "5":
            excluir_cadastro()
        elif opcao == "6":
            print("Encerrando o programa!")
            break
        else:
            print("Opcao inválida. Tente novamente.")

if __name__ == "__main__":
    produtos = {}
def carregar_produtos():
    try:
        with open("produtos.txt", "r") as file:
            for linha_num, linha in enumerate(file, start=1):
                dados = linha.strip().split(":")
                if len(dados) >= 2:
                    chave = dados[0].strip()
                    valor = dados[1].strip()
                    if chave == "ID":
                        id_produto = valor
                        produtos[id_produto] = {}
                    else:
                        produtos[id_produto][chave] = valor
                else:
                    print(f"Formato inválido na linha {linha_num}: {linha}")
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Erro ao carregar produtos: {e}")

# Função para salvar produtos no arquivo
def salvar_produtos():
    try:
        with open("produtos.txt", "w") as file:
            for id_produto, produto in produtos.items():
                file.write(f"ID: {id_produto}\n")
                file.write(f"Nome: {produto['Nome']}\n")
                file.write(f"Especificacoes: {produto['Especificacoes']}\n")
                file.write(f"Quantidade: {produto['Quantidade']}\n")
                file.write(f"Descricao: {produto['Descricao']}\n")
                file.write(f"Valor: {produto['Valor']}\n")
                file.write("\n")
    except Exception as e:
        print(f"Erro ao salvar produtos: {e}")

def formatar_valor(valor):
    return f"R$ {valor:.2f}"

# Função para exibir o menu principal
def menu_principal():
    print("Boas vindas ao nosso sistema:\n")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("3 - Listar produtos cadastrados")
    print("4 - Atualizar cadastro")
    print("5 - Excluir cadastro")
    print("6 - Sair")

# Função para cadastrar um produto
def cadastrar_produto():
    try:
        id_produto = input("Informe o ID do medicamento: ")
        nome = input("Informe o nome do medicamento: ")
        especificacoes = input("Informe as especificacoes dos medicamentos: ")
        quantidade = int(input("Informe a quantidade dos medicamentos no estoque: "))
        descricao = input("Informe uma descricao da medicacao (opcional): ")
        valor = float(input("Informe o valor da medicacao: "))

        produtos[id_produto] = {
            "Nome": nome,
            "Especificacoes": especificacoes,
            "Quantidade": quantidade,
            "Descricao": descricao,
            "Valor": valor
        }
        salvar_produtos()
        print("Produto cadastrado com sucesso!")
    except ValueError:
        print("Erro ao cadastrar produto. Certifique-se de inserir um valor válido para a quantidade e o preço.")

# Função para consultar um produto
def consultar_produto():
    id_produto = input("Informe o ID do produto que deseja consultar: ")
    produto = produtos.get(id_produto)
    if produto:
        print(f"ID: {id_produto}")
        for chave, valor in produto.items():
            print(f"{chave}: {valor}")
    else:
        print("Produto nao encontrado!")

# Função para listar produtos cadastrados
def listar_produtos():
    for id_produto, produto in produtos.items():
        print(f"ID: {id_produto}")
        print(f"Nome: {produto.get('Nome', 'N/A')}")
        print(f"Especificacoes: {produto.get('Especificacoes', 'N/A')}")
        print(f"Quantidade: {produto.get('Quantidade', 'N/A')}")
        print(f"Descricao: {produto.get('Descricao', 'N/A')}")

        valor = produto.get('Valor')
        if valor is not None:
            if isinstance(valor, (int, float)):
                print(f"Valor: {formatar_valor(valor)}")
            elif isinstance(valor, str):
                print(f"Valor: {valor}")
            else:
                print("Valor: N/A")
        else:
            print("Valor: N/A")

        print("-" * 70)

# Função para atualizar cadastro de um produto
def atualizar_cadastro():
    id_produto = input("Informe o ID do produto que deseja atualizar: ")
    produto = produtos.get(id_produto)
    if produto:
        print("Atualize os campos necessários:")
        nome = input(f"Nome ({produto['Nome']}): ")
        especificacoes = input(f"Especificacoes ({produto['Especificacoes']}): ")
        quantidade = input(f"Quantidade ({produto['Quantidade']}): ")
        descricao = input(f"Descricao ({produto['Descricao']}): ")
        valor = input(f"Valor ({formatar_valor(produto['Valor'])}): ")

        # Atualize os valores apenas se forem fornecidos
        if nome:
            produto['Nome'] = nome
        if especificacoes:
            produto['Especificacoes'] = especificacoes
        if quantidade:
            produto['Quantidade'] = int(quantidade)
        if descricao:
            produto['Descricao'] = descricao
        if valor:
            produto['Valor'] = float(valor)

        salvar_produtos()
        print("Cadastro atualizado com sucesso!")
    else:
        print("Produto nao encontrado!")

# Função para excluir cadastro de um produto
def excluir_cadastro():
    id_produto = input("Informe o ID do produto que deseja excluir: ")
    if id_produto in produtos:
        del produtos[id_produto]
        salvar_produtos()
        print("Cadastro excluído com sucesso!")
    else:
        print("Produto nao encontrado!")

# Função principal
def main():
    carregar_produtos()
    while True:
        menu_principal()
        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            consultar_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            atualizar_cadastro()
        elif opcao == "5":
            excluir_cadastro()
        elif opcao == "6":
            print("Encerrando o programa!")
            break
        else:
            print("Opcao inválida. Tente novamente.")

if __name__ == "__main__":
    produtos = {}
    main()
