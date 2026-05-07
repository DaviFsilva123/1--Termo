# 1. O Laço 'for' (Repetições Detetminadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve 
# acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada UM:
# Exemplo 1
# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada [OK]")
#     print("Produção do dia finalizada!")

# # Imagine que você queira atingir uma meta de produção de 5 carros e numera-los]

# for carros in range(1, 6):
#     print(f"processando a produção de carro {carros}...")

# # Exemplo 2 
# # Contar até 4
# for i in range (5):
#     print(i)

# Exemplo 3 
# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
# tipospeças = ["Porca do eixo", "Barra Dentada", "Rolamento Vertical", "Anel Externo", "Parafuso Phillips"]

# for item in pecas:
#    print(f"Item em estoque: {item}")
# for tipos in tipospeças:
#    print(f"Tipos de itens {tipospeças}")

# # Exemplo 4

# print("Loja de roupas")
# print("Bem-vindo ao nosso sistema")
# print("Escolha uma das opções")
# print("1 - roupas")
# print("2 - marca de roupas")

# opção = int(input("digite sua opção de pesquisa: "))
# roupas = ("camiseta", "calça", "tenis", "corrente", "pusseira", "moletom")
# marcaderoupas = ["crhome herts", "balanciaga", "hellstar", "corteiz", ]

# if opção == 1:
#    for item in roupas:
#       print(f"Item em estoque: {item}")
#       print("fim da lista")
# elif opção == 2:
#    for item2 in marcaderoupas:
#     print(f"item em estoque: {item2}")
#    else:
#       print("encerrando o sistema")

# Exercício 1
# Contador de produção 

# for ciclo in range (1, 11):
#    print(f"peça n° {ciclo} processando com sucesso...")
# print("ciclo de produção concluido")

# Exercício 2

# bananas = ["banana"]
# mangas = ["mangas"]
# melancias = ["melancias"]
# abacaxi = ["abacaxi"]

# for bananas in range (1, 11):
#     print(f"bananas {bananas}")

# for mangas in range (1, 6):
#     print(f"mangas {mangas}")

# for melancias in range (1, 11):
#     print(f"melancias {melancias}")

# for abacaxi in range (1, 14):
#     print(f"abacaxi {abacaxi}")

# Exercicio 3
# tabuada = int(input("qual tabuada voce deseja?"))
# for numero in range (1, 11):
#      resultado = tabuada * numero
#      print(f"{tabuada} x {numero} = {resultado}")  

# import time 
# temperatura = 25 
# while temperatura < 40:
#     print(f"temperatura atual: {temperatura}°C. Sistema operando")
#     time.sleep(2)
#     temperatura += 3 
# print("ALERTA! Temperatura atingiu o limite. desligando o motor...")

# opcao = ""

# while opcao != "sair" and "SAIR":
#     opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ").lower()
#     if opcao != "sair" and "SAIR":
#         print(f"Dado '{opcao}' registrado no banco de dados.")
# print("sistema encerrado.")

# and e or
# and comparações verdadeirar e iguais
# or comparações verdaderiras e nao iguais

# Exercicio 4

# pressao = 0
# while pressao <100:
#     pressao = int(input("digite o outro valor da pressao"))
#     print(f"temperatura atual: {pressao}PSI. sistema operando")
# print("ALERTA! Pressão crítica atingida")

# Exercicio 5
# print("menu de series")
# print("1- series ação")
# print("2- series terror")
# print("3- series suspense")
# print("4- series romance")

# while serie == "1" or "2" or "3" or "4":
#     serie = input("qual tipo de serie você deseja assistir?")
#     if serie == "1":
#         print("você")



        