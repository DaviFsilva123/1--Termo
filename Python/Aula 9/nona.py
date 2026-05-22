# EXERÍCIO 1
# ERRADO 

# idade = input("Digite sua idade: ")
# if idade >= 18:
#     print("Você é maior de idade.")

# CORRIGIDO

# idade = float(input("Digite sua idade:"))
# if idade >= 18:
#     print("Você é maior de idade.")
# else:
#    print ("Você é menor de idade")

# EXERCÍCIO 2
# ERRADO

# nome = "Mariana"
# print("Seja bem-vinda, nome!")

# CORRIGIDO
# nome = "Mariana"
# print("Seja bem-vinda", nome)

# EXERCÍCIO 3
# ERRADO

# numero = 10
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco")

# CORRIGIDO

# numero = float(input("Qual o número você deseja?"))
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco")

# EXERCÍCIO 4
# ERRADO

# usuario = "aluno123"
# if usuario == "aluno123"
#     print("login realizado com sucesso")

# CORRIGIDO
  
# usuario = input("Qual o nome do usuário?")
# if usuario == "aluno123":
#     print("login realizado com sucesso")
# else:
#     print("Login não foi realizado")

# EXERCÍCIO 5
# ERRADO
# clima = ""ensolarado"
# if clima = "chuvoso":
# print("leve o guarda-chuva!")

# CORRIGIDO

# clima = input("Qual o clima atual?")

# if clima == "chuvoso":
#     print("Leve o guarda-chuva!")
# elif clima == "ensolarado":
#     print("dia ensolarado!")
# else:
#     print("tenha um ótimo dia")

# EXERCÍCIO 6
# ERRADO

# pontos = 50
# print("Parabéns! Você fez" + pontos + " pontos.")

# CORRIGIDO

# pontos = 50
# print("Parabéns! Você fez", pontos, "pontos")

# EXERCÍCIO 7
# ERRADO
# nota = 9.5
# if nota >= 7:
#   print("Aprovado")
# elif nota >= 9:
#   print("Excelente!")

# CORRIGIDO
# nota = float(input("Qual nota você tirou na prova?"))

# if nota == 7:
#     print("Aprovado")
# elif nota >= 8:
#     print("Excelente!")
# elif nota < 7:
#     print("Você ficou abaixo da média")

# EXERCÍCIO 8
# ERRADO
# for i in range(5):
#     print(i)

# CORRIGIDO
# for i in range(6):
#     print(i)

# EXERCÍCIO 9
# ERRADO

# tentativas = 1
# while tentativas <= 3:
#   print("Tentando conectar...")

# CORRIGIDO
# tentativas = float(input("Qual o numero de tentativas"))
# while tentativas <= 3:
#     print("Tentando conectar...")
#     tentativas = tentativas +1

# EXERCÍCIO 10
# ERRADO
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

# CORRIGIDO

# senha = ""
# while senha != "python123":
#     senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")