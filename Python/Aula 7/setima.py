# # ATIVIDADE 1

# print("Registro de veiculo")
# modelo_veiculo = input("Informe o modelo do veículo?")
# placa_veiculo = input("Informe a placa de seu veículo?")
# print(f"Veiculo {modelo_veiculo} de placa {placa_veiculo} registrado no sistema. Boa viagem")

# # ATIVIDADE 2

# print("Cauculo de autonomia")
# capacidade_tanque = float(input("Digite a capacidade do tanque em litros"))
# consumo_medio = float(input("Digite o consumo do caminhâo em km/l"))
# distancia_total = capacidade_tanque * consumo_medio
# print(f"Capacidade {capacidade_tanque} do tanque e sua distancia media é {consumo_medio} em média KM/L e o total é {distancia_total}")

# # ATIVIDADE 3

# print("Convensor de moeda (frete internacional)")
# valor_frete = float(input("Valor frete em dolar"))
# conversor_real = float(input("Valor da taxa em reais"))
# total_converasao = valor_frete * conversor_real
# print(f"O valor do frete foi {valor_frete} e a taxa aplicada foi de {conversor_real} e o total do frete {total_converasao}")

# ATIVIDADE 4

# print("Media de entregas")
# rota1 = int(input("Digite a primeira rota em horas"))
# rota2 = int(input("Digite a segunda rota em horas"))
# rota3 = int(input("Digite a terceira rota em horas"))
# media_rota = (rota1 + rota2 + rota3) /3
# print(f"A media de entregas das rotas realizadas foi de {media_rota:.2f}")

# ATIVIDADE 5

# print("Monitor de carga")
# peso_caminhao = float(input("Informe o peso da caminhão em Tonenadas"))
# if peso_caminhao <= 10:
#     print("Carga leve")
# elif peso_caminhao < 25:
#     print("Carga padrão")
# elif peso_caminhao >= 25:
#     print("ALERTA: Ecesso de peso!")
# else:
#     print("Digite outro valor")

# ATIVIDADE 6

# print("classificador de destino")
# print("Codigos de carga = N para norte = S para sul e outros internacionais")
# codigo_carga = input("Iserir o código da carga em N ou S ou O")
# if codigo_carga == "N":
#     print("Região Norte")
#     # lower() #texto minusculo
# elif codigo_carga == "S":
#     print("Região Sul")
# else:
#     print("Região internacional")   

# # ATIVIDADE 7

# print("Libertação de saída")
# checklist = input("O checklist foi realizado (concluido ou nao concluido)")
# motorista = input("O motorista foi identificado (sim ou não)")
# if checklist == "concluido" and motorista == "sim":
#     print("inicio da rota - boa viagem")
# else:
#     print("voltar a realizar o checklist")
 
# ATIVIDADE 8

# print("cauculo de atrasos")
# entregas_agendadas = int(input("Quantidade de entregas agendadas"))
# entregas_atraso = int(input("Quantidade de entregas com atraso"))
# total = entregas_atraso / entregas_agendadas
# if total > 0.1:
#     print("Necessário Otimizar Rotas")
# else:
#     print("Logística Eficiente")

# ATIVIDADE 9

# print("Validação de Calibragem - Pressão dos Pneus")
# carga_pressao = float(input("Digite e medida da pressão em PSI dos Pneus"))
# if carga_pressao <= 100:
#     print("Abaixo do recomendado")
# elif carga_pressao >=110:
#     print("Acima do recomendado") 
# else:
#     print("Dentro do padrão recomendado")

# ATIVIDADE 10

# import time
# print("Contagem de Embarque")
# for embarque in range(5,0,-1):
#     time.sleep
#     print(f"Embarque e, :) {embarque}")

# ATIVIDADE 11

# print("Somatoria de frete acumulado")
# faturamento = 0 
# frete = 1
# while frete != 0:
#     frete = float(input("digite o valor do frete ou 0 para encerrar"))
#     faturamento += frete 
#     print(F"Faturamento total foi de {faturamento}")

# ATIVIDADE 12

# print("Monitoramento de Frota - Quilometragem")
# maior_km = 0
# for i in range(1,6):
#     km = float(input(f"Digite a quilometragem do veículo {i}"))
#     if km > maior_km:
#         maior_km = km
# print(f"A maior quilometragem registrada foi de {maior_km} km")


# var = 0
# print("Monitoramento de Frota - Km - Versão 2.0")
# veiculo1 = int(input("Informe a KM do veiculo 1"))
# for km in range(2,6):
#     veiculos = float(input(f"Informe a KM do veiculo{km}registrada"))
#     var = var + veiculos
#     print(f"A maior KM foi de {var}")

# ATIVIDADE 13

# print("Sistema de Rastreio")
# erros = 0
# tentativas = 3

# while erros != 3:
#     codigo = input("Insira o código de acesso")
#     if codigo != "track99":
#         erros = erros + 1
#         tentativas = tentativas - 1
#         print(f"Codigo incorreto você possui {tentativas}")
#     else:
#         break
#     if erros == 3:
#         print("Rastreamento bloqueado!")
#     else:
#         print("Acesso liberado :)")


# print("Sistema de Rastreio - Versão 2")
# acesso_negado = 0
# while acesso_negado != 3:
#     codigo = input("Digite o código de acesso do rastreador")
#     if codigo != "track99":
#         acesso_negado = acesso_negado + 1
#         print("Acesso Negado :(")
#         print("Rastreamento Bloqueado! ")
#     elif codigo:
#         print("Acesso Liberado")
#         break~

# ATIVIDADE 14

# print("Gerenciador de Combustível")
# tanque = 500
# while True:
#     print("1 - Abastecer")
#     print("2 - Retirar")
#     print("3 - Sair")
#     opcao = input("Escolha uma opção")
#     if opcao == "1":
#         valor = float(input("Quantidade a abastecer"))
#         tanque += valor
#         print(f"Tanque atual: {tanque}")
#     elif opcao == "2":
#         valor = float(input("Quantidade a retirar"))
#         if valor > tanque:
#             print("Quantidade indisponível")
#         else:
#             tanque -= valor
#             print(f"Tanque atual {tanque}")
#     elif opcao == "3":
#         print("Encerrando o Sistema")
#         break
# else:
#         print("Opção Inválida")
#         if tanque < 50:
#             print("Reserva Critica")

#  ATIVIDADE 15

# print("Relatório de Inspeção de Pneus")
# contagem = 0
# total = 5
# for pneu in range(1,6):
#     medida = float(input(f"Medida do sulco do pneu {pneu} em mm"))
#     if medida >= 1.6:
#         contagem = contagem + 1
#         print("Pneu aprovado e adicionado a contagem :)")
#     else:
#         print("Pneu fora das medidas regulares não foi adicionado a contagem")
#         pass 
#     porcentagem = (contagem / total) * 100
#     print(f"Tiveram {contagem} pneus aprovados hoje com uma taxa de {porcentagem}% de conformidade")?