## Projeto de Gerenciamento de Produtos - Ada Tech - VemSerTech - Ifood

### Este projeto foi desenvolvido como parte do programa VemSerTech em colaboração com o Ifood e pela Ada Tech. Os integrantes responsáveis por este projeto são:

- [Wallace Lopes](https://github.com/wallacelops)
- [Vitor Fontenele](https://github.com/fontenelevitor)
- [Amanda Lima](https://github.com/amandailg)
- [Daniele Travessa](https://github.com/DanieleTravessa)

## Descrição

Este é um sistema simples de gerenciamento de produtos em Python. Ele oferece funcionalidades básicas para cadastrar, consultar, listar, atualizar e excluir produtos. Os dados dos produtos são armazenados em um arquivo de texto (`produtos.txt`).

## Funcionalidades

### 1. Carregar Produtos

A função `carregar_produtos()` lê os dados dos produtos a partir do arquivo `produtos.txt` e os carrega em um dicionário em memória (`produtos`). Se o arquivo não existir, uma mensagem indicando que o arquivo de produtos ainda não existe será exibida.

### 2. Salvar Produtos

A função `salvar_produtos()` salva os dados dos produtos no arquivo `produtos.txt`. Cada produto é representado por um bloco de informações, incluindo ID, nome, especificações, quantidade, descrição e valor.

### 3. Formatar Valor

A função `formatar_valor(valor)` formata o valor monetário para o formato "R$ X.XX", ou exibe "N/A" se o valor não estiver presente.

### 4. Menu Principal

A função `menu_principal()` exibe o menu principal do sistema, apresentando as opções disponíveis ao usuário.

### 5. Cadastrar Produto

A função `cadastrar_produto()` permite ao usuário cadastrar um novo produto, solicitando informações como ID, nome, especificações, quantidade, descrição e valor. Os dados do produto são validados, e o produto é adicionado ao dicionário `produtos`.

### 6. Consultar Produto

A função `consultar_produto()` permite ao usuário consultar um produto específico fornecendo seu ID. Se o produto existir, suas informações serão exibidas; caso contrário, será exibida uma mensagem informando que o produto não foi encontrado.

### 7. Listar Produtos

A função `listar_produtos()` exibe uma lista de todos os produtos cadastrados, apresentando suas informações de forma organizada.

### 8. Atualizar Cadastro

A função `atualizar_cadastro()` permite ao usuário atualizar as informações de um produto existente. O usuário pode optar por atualizar campos como nome, especificações, quantidade, descrição e valor.

### 9. Excluir Cadastro

A função `excluir_cadastro()` permite ao usuário excluir um produto do sistema com base no ID fornecido.

### 10. Função Principal

A função `main()` é a função principal que inicia o programa. Ela carrega os produtos existentes, exibe o menu principal e direciona o fluxo de acordo com a escolha do usuário.

## Executando o Programa

Para executar o programa, certifique-se de ter o arquivo `produtos.txt` no mesmo diretório do script. O programa será iniciado, e você poderá interagir com o sistema através do menu principal.

Esperamos que este sistema simplificado facilite o gerenciamento básico de produtos. Sinta-se à vontade para contribuir, aprimorar e adaptar conforme suas necessidades específicas.
