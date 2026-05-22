#if: "se" a condição for verdadeira.
#elif: "Senão, se" (usado para mútiplas condições).
# else: "Senão" (executa se nenhuma das anteriores for verdadeira).

#Exemplo 1
print("Verificar Maioridade")
idade = int(input("Digite sua idade"))

if idade >= 18:
    print("Você é Adulto")
elif idade >= 16:
    print("Você não é adulto, mas pode votar")
else:
    print("Você é adolescente")

    #Sinais de > Maior e >= Maior igual
    #Sinais de < Menor e <= Menor e igual
    #Sinais de == Igual

#Exemplo 2
print("loja")
print("Bem-Vindo ao sistema do Davi")
print("Opções:")
print(" 1 - Sapatos")
print(" 2 - Roupas")
print(" 3 - Perfumes")

escolha = int(input("Digite sua escolha através do número das opções:"))
if escolha == 1:
    print("Você quer comprar sapatos, OK")
    Valor1 = float(input("Digite o Valor do produto: "))
    Quantidade1 = int(input("Digite a quantidade desejada: "))
    total = Valor1 * Quantidade1 
    print("Sua compra de sapatos foi um total de: ", total)
elif escolha == 2:
    print("Você quer comprar roupas, OK")
    Valor2 = float(input("Digite o Valor do produto: "))
    Quantidade2 = int(input("Digite a quantidade desejada: "))
    total = Valor2 * Quantidade2
    print("Sua compra de roupas foi um total de: ", total)
elif escolha == 3:
    print("Você escolheu o Perfumes")
    Valor3 = float(input("Digite o Valor do produto: "))
    Quantidade3 = int(input("Digite a quantidade desejada: "))
    total = Valor3 * Quantidade3
    print("Sua compra de perfumes foi um total de: ", total)
else:
    print("Obrigado por utilizar o sistema")

# Exemplo 3
print("Escolha uma opção para iniciar o sistema")
print("Series = S")
print("Filmes = F")
categoria = input("Digite sua categoria")
if categoria == "S":
    print("você escolheu por Séries")
elif categoria == "F":
    print("Você escolheu por Filmes")
else:
    print("Obrigado por escolher uma das categorias")

# Exercício 1 
# Crie um algoritimo que simule uma cauculadora e que por opção de escolha permita calcular os operadores.
# Ex : Ao escolher a opção 1, ele irá calcula a soma e assim por diante








