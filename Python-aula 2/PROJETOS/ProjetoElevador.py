# O sistema de elevador do prédio
# O prédio possui  10 andares, sendoo térreo o andar 0. O elevador pode se mover para cima e para baixo, e tem a capacidade de transportar até 5 pessoas
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

# Levantamento de Requisitos
# Requisitos funcionais (RF):
# - O elevador deve se mover para cima e para baixo.
# - Precisa possuir um sistema que conte andares de 0 a 10.
# - O elevador deve transportar até 5 pessoas.
# - O elevador pode ser chamado de qualquer andar do andar 0 até o andar 10.
# - O elevador precisa se mover do ponto em que foi chamado até o destino quem chamou.
# Requisitos não fincional (RNF):
# - Exibir mensagens indicando o andar atual.
# - Exibir o número de pessoas no elevador.
# - As ações realizadas (Subindo, descendo, parando).
import time

while True:
    print("Seja bem-vindo ao elevador!")

    time.sleep(1)
    andar_atual = float(input("Qual o seu andar atual? "))

    time.sleep(2)
    input("Aperte o botão para abrir a porta do elevador! ")

    print("A capacidade maxima do elevador são 5 pessoas")

    time.sleep(1)
    print("Elevador chegando... ")

    time.sleep(1)
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    quantidade_pessoas = float(input("Qual a quantidade de pessoas que vão se locomover?"))

    if quantidade_pessoas <= 5:
        print("Entre e fique a vontade.")
    else:
        print("capacidade maxima atingida!! Chame o elevador novamente.")
        continue

        time.sleep(1)
    print(f"você está no andar {andar_atual} e {quantidade_pessoas} irão se locomover.")

    time.sleep(1)
    andar_desejado1 = float(input("Para qual andar você deseja ir?"))

    if andar_desejado1 > andar_atual:
        print("Subindo")

        time.sleep(1)
    elif andar_desejado1 < andar_atual:
        print("Descendo")

        time.sleep(1)
    print(f"Te levando até o andar {andar_desejado1}... ")

    time.sleep(1)
    print("Você chegou ao seu destino!")

    
