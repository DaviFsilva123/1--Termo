# 1. Cadastro de Funcionários:
# ○ Armazene o nome, setor e o status dos treinamentos (NR-10, NR-35 e
# Brigada).

# 2. Verificação de EPI (NR-6):
# ○ O sistema deve receber o setor do funcionário.
# ○ Se o setor for "Elétrica", liste a obrigatoriedade de luvas de alta tensão e
# botas dielétricas.
# ○ Se o setor for "Trabalho em Altura", liste o cinturão de segurança e
# talabarte.
# 3. Alerta de Reciclagem:
# ○ Crie uma função que receba o ano do último treinamento da Brigada de
# Incêndio.
# ○ Se o treinamento tiver mais de 2 anos, exiba a mensagem: "Treinamento
# Vencido! Encaminhar para reciclagem."
# ○ Caso contrário, exiba: "Treinamento Válido."
# 4. Relatório Geral:
# ○ Exiba na tela um resumo com o total de funcionários cadastrados e quantos
# estão com treinamentos em dia.

# Requisitos funcionais (RF):
# O sistema deve armazenar o nome, setor e os status de treinamento dos funcionários.
# Se o funcionário trabalhar no setor de elétrica, o sistema deve listar os equipamentos obrigatórios (luvas de alta tensão e botas dielétricas). Se o funcionário trabalhar no setor de "trabalho em altura", o sistema deve listar os equipamentos obrigatórios(Cinturão de segurança e talabarte).
# Requiquisitos não funcionais (RNF):
# Um sistema que receba o ano do último treinamento de Brigada de incêndio. Se o treinamento tiver mais de 2 anos o sistema deve exibir uma mensagem (Treinamento vencido! Encaminhar para a reciclagem. Sepossuir menos de 2 anos exiba a mensagem (Treinamento válido.))
# Um sistema que exiba na tela um resumo com total de funcionários cadastrados e quantos estão com treinamentos em dia.


import time


def identificacao_funcionario():
    print("status de conformidade dos funcionários de uma empresa.")
    time.sleep(1)
    nome_funcionarios = input(">>> Qual o nome do funcionário que está se apresentando? ")
    time.sleep(1)
    status_treinamento_usuario = input(">>> Qual seria seu status de treinamento? ")
    time.sleep(1)
    setor_funcionarios = input(">>> Qual o setor do funcionário que está se apresentando? ")
    time.sleep(1)

    if setor_funcionarios == "NR10":
        print("Utilize luvas de alta tensão e botas de eletricidade para evitar acidentes!")
    elif setor_funcionarios == "NR35":
        print("Utilize cinturão de segurança e talabarte para evitar acidentes!")
    else:
        print("Isto que você está informando não é um setor válido. Encerrando sistema!")

    return nome_funcionarios, status_treinamento_usuario, setor_funcionarios
    
while True:
    identificacao_funcionario()
    time.sleep(1)
    ano_treinamento = int(input(">>> Qual o ano do seu último treinamento de Brigada de Incêndio? "))
    time.sleep(1)
    if ano_treinamento <= 2022:
        print("Treinamento Válido.")
    else:
        print("Treinamento Vencido! Encaminhar para reciclagem.")

    



