# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox,ttk
# def registrar_operador():
#     nome_operador = ent_nome_operador.get()
#     turno_operador = cmb_turno.get()
#     if nome_operador =="" and turno_operador == "":
#          messagebox.showwarning("Atenção", "Preencha todos os campos")
#     else:
#          messagebox.showinfo("Bem-Vindo", f"Operador {nome_operador} Registrando no turno {turno_operador}")

# janela = tk.Tk()
# janela.title = ("Registro de Operador")
# janela.geometry("500x500")

# lbl_titulo_registro_de_operador = tk.Label(janela, text="Bem-Vindo a tela cadastral", font=("Arial", 14), fg = "black", bg= "white")
# lbl_titulo_registro_de_operador.grid(row=1, column=1, pady=10, padx=10)

# lbl_nome_operador = tk.Label(janela, text="Digite o nome do operador", font=("Arial", 14))
# lbl_nome_operador.grid(row=3, column=1, pady=10, padx=10)

# ent_nome_operador = tk.Entry(janela, font=("Arial", 14))
# ent_nome_operador.grid(row=3, column=2, pady=10, padx=10)

# btn_cadastrar_operador = tk.Button(janela, text="Cadastrar", font=("Arial",10), width=7,height=1, command=registrar_operador)
# btn_cadastrar_operador.grid(row=5, column=1, pady=10, padx=10)

# lbl_turno_operador = tk.Label(janela, text="Escolha seu turno", font=("Arial",14))
# lbl_turno_operador.grid(row=4, column=1, pady=10, padx=10)

# cmb_turno = ttk.Combobox(janela, values=["A", "B", "C"], state="readonly", width=40,height=40)
# cmb_turno.grid(row=4, column=2, pady=10, padx=10)

# btn_fechar =tk.Button(janela,text=" Fechar Janela",font=("Arial",10),width=10,height=1, command=janela.destroy)
# btn_fechar.grid (row=5,column=2,padx=10,pady=10)

# janela.mainloop()

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox
# def calcular_producao():
#     pecas_produzidas = ent_pecas_produzidas.get()
#     if pecas_produzidas == "":
#         messagebox.showwarning("Atenção", "Preencha o campo de peças produzidas")
#     else:
#         total_pecas_turno = int(pecas_produzidas) * 8
#         messagebox.showinfo("Produção Calculada", f"Em um turno de 8 horas, serão produzidas {total_pecas_turno} peças.")
# janela = tk.Tk()
# janela.title = ("Cáuculo de Produção")
# janela.geometry("500x500")

# lbl_pecas_produzidas = tk.Label(janela, text="Digite a quantidade de peças produzidas em 1 hora:", font=("Arial", 14) )
# lbl_pecas_produzidas.grid(row=1, column=1, pady=10, padx=10)

# ent_pecas_produzidas = tk.Entry(janela, font=("Arial", 14))
# ent_pecas_produzidas.grid(row=2, column=1, padx=10, pady=10)

# btn_calcular_producao = tk.Button(janela, text="Calcular", font=("Arial", 10), width=7, height=1, command=calcular_producao)
# btn_calcular_producao.grid(row=3, column=1, pady=10, padx=10)

# btn_fechar =tk.Button(janela,text=" Fechar Janela",font=("Arial",10),width=10,height=1, command=janela.destroy)
# btn_fechar.grid (row=5,column=2,padx=10,pady=10)

# janela.mainloop()

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# def converter_pressao():    
#     pressao_bar = ent_pressao_bar.get()
#     if pressao_bar == "":
#         messagebox.showwarning("Atenção", "Preencha o campo de pressão em Bar")
#     else:
#         pressao_psi = float(pressao_bar) * 14.5
#         messagebox.showinfo("Pressão Convertida", f"{pressao_bar} Bar é equivalente a {pressao_psi:.2f} PSI.")

# janela = tk.Tk()
# janela.title = ("Conversor de Unidade")
# janela.geometry("500x500")

# lbl_pressao_bar = tk.Label(janela, text="Digite a pressão em Bar:", font=("Arial", 14))
# lbl_pressao_bar.grid(row=1, column=1, pady=10, padx=10)  

# ent_pressao_bar = tk.Entry(janela, font=("Arial", 14))
# ent_pressao_bar.grid(row=2, column=1, pady=10, padx=10)

# btn_converter_pressao = tk.Button(janela, text="Converter", font=("Arial", 10), width=7, height=1, command=converter_pressao)
# btn_converter_pressao.grid(row=3, column=1, pady=10, padx= 10)

# btn_fechar =tk.Button(janela,text=" Fechar Janela",font=("Arial",10),width=10,height=1, command=janela.destroy)
# btn_fechar.grid (row=5,column=2,padx=10,pady=10)

# janela.mainloop()

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox

# def calcular_media():
#     nota1 = ent_nota1.get()
#     nota2 = ent_nota2.get()
#     nota3 = ent_nota3.get()
#     if nota1 == "" or nota2 == "" or nota3 == "":
#         messagebox.showwarning("Atenção", "Preencha todos os campos de notas")
#     else:
#         media = (float(nota1) + float(nota2) + float(nota3)) / 3
#         messagebox.showinfo("Média Calculada", f"A média das notas é: {media:.2f}")

# janela = tk.Tk()
# janela.title = ("Média de Qualidade")
# janela.geometry("500x500")

# lbl_nota1 = tk.Label(janela, text="Digite a primeira nota de inspeção (0 a 10):", font=("Arial", 14))
# lbl_nota1.grid(row=1, column=1, pady=10, padx=10)

# lbl_nota2 = tk.Label(janela, text="Digite a segunda nota de inspeção (0 a 10):", font=("Arial", 14))
# lbl_nota2.grid(row=2, column=1, pady=10, padx=  10)

# lbl_nota3 = tk.Label(janela, text="Digite a terceira nota de inspeção (0 a 10):", font=("Arial", 14))
# lbl_nota3.grid(row=3, column=1, pady=10, padx=10)

# ent_nota1 = tk.Entry(janela, font=("Arial", 14))
# ent_nota1.grid(row=1, column=2, pady=10, padx=10)

# ent_nota2 = tk.Entry(janela, font=("Arial", 14))
# ent_nota2.grid(row=2, column=2, pady=10, padx=10)

# ent_nota3 = tk.Entry(janela, font=("Arial", 14))        
# ent_nota3.grid(row=3, column=2, pady=10, padx=10)

# btn_calcular_media = tk.Button(janela, text="Calcular Média", font=("Arial", 10), width=12, height=1, command=calcular_media)
# btn_calcular_media.grid(row=4, column=1, pady=10, padx=10)

# btn_fechar =tk.Button(janela,text=" Fechar Janela",font=("Arial",10),width=10,height=1, command=janela.destroy)
# btn_fechar.grid (row=5,column=2,padx=10,pady=10)

# janela.mainloop()

# Foco: if, elif, else e operadores lógicos
# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox

# def calcular_temperatura():
#     temperatura_motor = float(ent_temperatura_motor.get())

#     if temperatura_motor < 40:
#         messagebox.showinfo("Temperatura do Motor", "Baixa carga")
#     elif temperatura_motor >= 40 and temperatura_motor <= 70:
#         messagebox.showinfo("Temperatura do Motor", "Normal")
#     elif temperatura_motor > 70:
#         messagebox.showinfo("Temperatura do Motor", "ALERTA: Resfriamento Ativado!")

# janela = tk.Tk()
# janela.title = ("Termostato Inteligente")
# janela.geometry("500x500")

# lbl_temperatura_motor = tk.Label(janela, text="Insira a temperatura atual do motor abaixo:", font=("Arial", 14))
# lbl_temperatura_motor.grid(row=1, column=1, pady=10, padx=10)

# ent_temperatura_motor = tk.Entry(janela, font=("Arial", 14))
# ent_temperatura_motor.grid(row=2, column=1, pady=10, padx=10)

# btn_temperatura_motor = tk.Button(janela, text="Calcular temperatura", width=19, height=1, command=calcular_temperatura)
# btn_temperatura_motor.grid(row=3, column=1, pady=10, padx=10)

# btn_fechar =tk.Button(janela,text=" Fechar Janela",font=("Arial",10),width=10,height=1, command=janela.destroy)
# btn_fechar.grid (row=5,column=2,padx=10,pady=10)

# janela.mainloop()

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# import tkinter as tk
# from tkinter import messagebox,ttk
# def classificar_lotes():
#     codigos = cmb_codigo.get()

#     if codigos == "A(alimentos)":
#         messagebox.showinfo("Alimentos", "Você escolheu a opção de alimentos")
#     elif codigos == "E(eletrônicos)":
#         messagebox.showinfo("Eletrônicos", "Você escolheu a opção eletrônicos")
#     else:
#         messagebox.showerror("ALERTA!", "Produto desconhecido")
# janela = tk.Tk()
# janela.title = ("Classificador de Lotes")
# janela.geometry("500x500")

# lbl_codigo_produto = tk.Label(janela, text="Insira o código do produto que deseja:", font=("Arial", 14))
# lbl_codigo_produto.grid(row=1, column=1, pady=10, padx=10)

# cmb_codigo = ttk.Combobox(janela, values=["A(alimentos)", "E(eletrônicos)"], state="readonly", width=40,height=40)
# cmb_codigo.grid(row=2, column=1, pady=10, padx=10)

# btn_codigo = tk.Button(janela, text="Classificar", width=12, height=1, command=classificar_lotes)
# btn_codigo.grid(row=3, column=1, pady=10, padx=10)

# btn_fechar =tk.Button(janela,text=" Fechar Janela",font=("Arial",10),width=10,height=1, command=janela.destroy)
# btn_fechar.grid (row=5,column=2,padx=10,pady=10)

# janela.mainloop()

# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# import tkinter as tk
# from tkinter import messagebox,ttk

# def verificar_seguranca():
#     sensor_porta = cmb_sensor_porta.get()
#     botao_emergencia = cmb_botao_emergencia.get()

#     if sensor_porta == "fechada" and botao_emergencia == "desligado":
#         messagebox.showinfo("Segurança Verificada", "A máquina pode iniciar.")
#     else:
#         messagebox.showwarning("Segurança Verificada", "A máquina não pode iniciar. Verifique os sensores.")   

# janela = tk.Tk()
# janela.title = ("Segurança de Operação")
# janela.geometry("500x500")

# lbl_sensor_porta = tk.Label(janela, text="Estado do sensor da porta:", font=("Arial", 14))
# lbl_sensor_porta.grid(row=1, column=1, pady=10, padx=10)

# cmb_sensor_porta = ttk.Combobox(janela, values=["fechada", "aberta"], state="readonly", width=40,height=40)
# cmb_sensor_porta.grid(row=1, column=2, pady=10, padx=10)

# lbl_botao_emergencia = tk.Label(janela, text="Estado do botão de emergência:", font=("Arial", 14))
# lbl_botao_emergencia.grid(row=2, column=1, pady=10, padx=10)

# cmb_botao_emergencia = ttk.Combobox(janela, values=["desligado", "ligado"], state="readonly", width=40,height=40)
# cmb_botao_emergencia.grid(row=2, column=2, pady=10, padx=10)

# btn_verificar_seguranca = tk.Button(janela, text="Verificar Segurança", width=19, height=1, command=verificar_seguranca)
# btn_verificar_seguranca.grid(row=3, column=1, pady=10, padx=10)

# btn_fechar =tk.Button(janela,text=" Fechar Janela",font=("Arial",10),width=10,height=1, command=janela.destroy)
# btn_fechar.grid (row=5,column=2,padx=10,pady=10)

# janela.mainloop()

# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# import tkinter as tk
# from tkinter import messagebox

# def calcular_descarte():

#     total_pecas = ent_total_pecas.get()
#     pecas_defeituosas = ent_pecas_defeituosas.get()

#     if total_pecas == "" or pecas_defeituosas == "":
#         messagebox.showwarning("Atenção", "Preencha todos os campos")
#     else:
#         descarte_percentual = (float(pecas_defeituosas) / float(total_pecas)) * 100
#     if descarte_percentual > 5:
#         messagebox.showinfo("Cálculo de Descarte", "Revisar Processo")
#     else:
#         messagebox.showinfo("Cálculo de Descarte", "Processo Otimizado")

# janela = tk.Tk()
# janela.title = ("Cálculo de Descarte")
# janela.geometry("500x500")

# lbl_total_pecas = tk.Label(janela, text="Digite o total de peças produzidas:", font=("Arial", 14))
# lbl_total_pecas.grid(row=1, column=1, pady=10, padx=10)

# ent_total_pecas = tk.Entry(janela, font=("Arial", 14))
# ent_total_pecas.grid(row=1, column=2, pady=10, padx=10)

# lbl_pecas_defeituosas = tk.Label(janela, text="Digite o total de peças defeituosas:", font=("Arial", 14))
# lbl_pecas_defeituosas.grid(row=2, column=1, pady=10, padx=10)

# ent_pecas_defeituosas = tk.Entry(janela, font=("Arial", 14))
# ent_pecas_defeituosas.grid(row=2, column=2, pady=10, padx=10)

# btn_calcular_descarte = tk.Button(janela, text="Calcular Descarte", width=19, height=1, command=calcular_descarte)
# btn_calcular_descarte.grid(row=3, column=1, pady=10, padx=10)

# btn_fechar =tk.Button(janela,text=" Fechar Janela",font=("Arial",10),width=10,height=1, command=janela.destroy)
# btn_fechar.grid (row=5,column=2,padx=10,pady=10)

# janela.mainloop()

# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.

# import tkinter as tk
# from tkinter import messagebox

# def validar_medida():
#     medida_peca = ent_medida_peca.get()

#     if medida_peca == "":
#         messagebox.showwarning("Atenção", "Preencha o campo de medida da peça")
#     else:
#         medida = float(medida_peca)
#     if medida < 9.8:
#             messagebox.showinfo("Validação de Medida", "A peça está abaixo da tolerância.")
#     elif medida > 10.2:
#         messagebox.showinfo("Validação de Medida", "A peça está acima da tolerância.")
#     else:
#         messagebox.showinfo("Validação de Medida", "A peça está dentro da tolerância.")

# janela = tk.Tk()
# janela.title = ("Validação de Medida")    
# janela.geometry("500x500")

# lbl_medida_peca = tk.Label(janela, text="Digite a medida da peça em mm:", font=("Arial", 14))
# lbl_medida_peca.grid(row=1, column=1, pady=10, padx=10)

# ent_medida_peca = tk.Entry(janela, font=("Arial", 14))
# ent_medida_peca.grid(row=1, column=2, pady=10, padx=10)

# btn_validar_medida = tk.Button(janela, text="Validar Medida", width=19, height=1, command=validar_medida)
# btn_validar_medida.grid(row=2, column=1, pady=10, padx=10)

# btn_fechar =tk.Button(janela,text=" Fechar Janela",font=("Arial",10),width=10,height=1, command=janela.destroy)
# btn_fechar.grid (row=5,column=2,padx=10,pady=10)

# janela.mainloop()

# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

import tkinter as tk

janela = tk.Tk
janela.title = ("Contagem Regressiva de Setup")
janela.geometry("500x500")

btn_iniciar_contagem = tk.Button(janela)

