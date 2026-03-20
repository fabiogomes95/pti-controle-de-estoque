#Autor: Fabio Gomes da Silva
#Date: 01/03/2026
#Programa de Controle de Estoque

estoque = [] # Lista do estoque onde vamos armazenar os dados do programas

# função para cadastrar o produto ao escolher a opção 1!
def cadastrar_produto(): # nome da função
   codigo = input("Digite o código do produto: ") # Pede o código do produto
   for produto in estoque: # Laço de repetição para verificar se tem "id" repetido na minha lista estoque
       if produto["id"] == codigo: # Verifica o id da lista com o id recem digitado
           print("Produto já cadastrado") # Caso já tem uma id igual, é impresso essa mensagem
           return # finaliza o laço e volta pro programa normal
   nome  = input("Digite o nome do produto: ") # Pede o nome do produto
   preco = float(input ("Digite o preço do produto: ")) # Pede o preço
   quantidade = int(input("Digite a quantidade: ")) # Pede a Quantidade
   if preco < 0 or quantidade < 0: # Veirica se o preço ou a quantidade é menor que 0
       print("Preço e quantidade não podem ser nagativos")  # imprime na tela avisando que eles não podem ser negativos
       return # finaliza o if e retorna para o laço principal
   novo_produto = {"id":codigo, "nome": nome, "preco": preco,"qtd": quantidade} #criação de um dicionaro para acessar as infos
   estoque.append(novo_produto) #adiciona o dicionario a nossa lista inicial "estoque"
   print("Produto cadastrado!") #informa que o produto foi cadastrado


#função para calcular total de produtos armazenados
def calcular_total(): # Nome da função
   total_estoque = 0 # Iniciando uma nova variavel com 0 para somar posteriomente
   for produto in estoque: # Laço de repetição para acessar o valor na lista estoque
       total_estoque = total_estoque + produto["qtd"] #soma da nossa variavel nova com o valor obitido da nossa lista/dicionario
   print("O valor total é:", total_estoque) # Imprime o valor total


#função para listar os produtos (um extra)
def listar_produtos(): #nome da função
   for produto in estoque: #laço de repetição para listar cada item da lista/dicionario
       print(f"{produto['qtd']} {produto['nome']} no valor de: R${produto['preco']:.2f} id do produto: {produto['id']}") #imprime cada info em sequencia


#laço de repetição onde vamos escolher uma das opções desejadas
while True:
   print("Bem vindo a GestãoTotal, escolha uma das opções:")
   print("1 - Cadastrar produto")
   print("2 - Calcular o Total de Produtos em Estoque")
   print("0 - Sair")
   opcao = input("Escolha uma opção: ") # Verifica as opções informadas
   if opcao == '1': # Se == 1 puxa a função "cadastrar_produto"
       cadastrar_produto()
   elif opcao == '2': # Se == 2 puxa a função "calcular_total e listar_produtos"
       calcular_total()
       listar_produtos()
   elif opcao == '0': # Se == 0, se despede e encerra o programa
       print("Obrigado por usar o GestãoTotal, até logo :)")
       break
   else: #retorna uma opçao invalida
       print("Opção Invalida, tente novamente!")
