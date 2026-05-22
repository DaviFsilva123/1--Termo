numero_de_vagas = 500
valor_fixo3horas = 15
horario_entrada = 0

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
        time.sleep(1)
        print("Você está saindo no horário:", horario_saida)
        time.sleep(1)
        perca_ticket = float(input("Você ainda possui um ticket? \n 1-não \n 2-sim")) 
        if perca_ticket == 1:
            print("Você deve pagar uma taxa de R$50")
            break
        else:
            ticket_horas = horario_saida - horario_entrada
        if ticket_horas <= 0.25:
            print("Saida grátis!!")
        elif ticket_horas <= 3:
            print("O valor que deve ser pago é", valor_fixo3horas)
        elif ticket_horas > 3:
            valor_extra = ticket_horas - 3
            valor_ticket_extra = (valor_extra * 3) +15
            print(f"O valor extra que deve ser pago é {valor_ticket_extra}")
        else:
            print("Entrada bloqueada. Permitido só entrada via tag.")

    if forma_acesso == 2:
        ticket_horas2 = 0
        

        id_tag = float(input("Qual é o id da sua tag?"))
        horario_entrada2 = float(input("Você está entrando no horario?"))
        print("Seja bem-vindo ao shopping!")
        time.sleep(1)
        print("Registrando o ID da sua tag e seu horário de entrada...")
        time.sleep(1)
        print(f"Seu id é {id_tag} você está entrando no horário {horario_entrada2}")
        print(f"Temos {numero_de_vagas} disponiveis")
        horario_saida = float(input("Qual horário você está saindo?:"))
        saida = horario_saida - horario_entrada
        if saida <= 0.25:
            print("Saída grátis!")
        elif saida <=3:
            valor_fixo3horas_tag = (valor_fixo3horas *0.1) - valor_fixo3horas
            print(f"O valor a ser pago é R${valor_fixo3horas_tag}")
        else:
            valor_extra = saida - 3
            valor_ticket_extra = (valor_extra * 3) + 15
            valor_tag = valor_ticket_extra - (valor_ticket_extra*0.1)
            print(f"O valor extra que deve ser pago é {valor_tag}")
     
    numero_de_vagas -= 1
    
  