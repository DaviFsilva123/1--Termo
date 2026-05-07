numero_de_vagas = 500
import time
while True:
    print("Bem-vindo ao Shopping")
    time.sleep(1)

    forma_acesso = int(input("Qual a sua forma de acesso? \n 1-ticket \n 2-tag")) 
    if forma_acesso == 1:
        print("Você está entrado com uma vaga comum")
        time.sleep(1)
        input("Pressione o botão")
        time.sleep(1)
        print("Verificando se há vagas comuns disponiveis...")
        time.sleep(1)
        print(f"Temos o total de {numero_de_vagas} disponiveis")
        if numero_de_vagas > 0:
            horario_entrada = float(input("Você está entrando no horário:"))
            print("Seja bem-vindo, aproveite seu passeio!!")
            time.sleep(1)
            numero_de_vagas -= 1
            horario_saida = float(input("Qual horário você está saindo?:"))
            saida = horario_saida -  horario_entrada
            time.sleep(1)
            print("Você está saindo no horário:", horario_saida)
            time.sleep(1)
            if saida <= 0.25:
                print("Saida grátis!!")
            elif saida >= 3:
                print("O seu estacionamento ficou o total de 15R$")

        else:
            print("Entrada bloqueada. Permitido só entrada via tag.")
    break

if forma_acesso == 2:
    
    id_tag = float(input("Qual é o id da sua tag?"))
horario_entrada2 = float(input("Você está entrando no horario?"))
print("Seja bem-vindo ao shopping!")
time.sleep(3)
print("Registrando o ID da sua tag e seu horário de entrada...")
time.sleep(3)
print(f"Seu id é {id_tag} você está entrando no horário {horario_entrada2}")






  