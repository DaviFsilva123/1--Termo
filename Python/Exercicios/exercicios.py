#Exercício - Crie uma aplicação que faça o cálculo de idade de pessoas.
# Deve perguntar o nome da pessoa e o ano de nascimento


import tkinter as tk
from tkinter import messagebox
def caucular_idade():
    ano_de_nascimento = int(ent_ano_de_nascimento.get())
    nome_usuario = ent_nome_usuario.get()
    if nome_usuario == "" and ano_de_nascimento == "":
        messagebox.showwarning("Aviso", "Porfavor, digite seu nome")
    else:
        messagebox.showinfo("Seja Bem-Vindo", f"olá {nome_usuario}, você tem {2026-ano_de_nascimento} anos de idade")

janela = tk.Tk()
janela.title("Cauculo de idade")
janela.geometry("500x500")

lbl_nome_usuario = tk.Label(janela, text="insira seu nome?")
lbl_nome_usuario.grid(row=1,column=2, padx=10, pady=10)

lbl_ano_de_nascimento = tk.Label(janela, text="Insira seu ano de nascimento?")
lbl_ano_de_nascimento.grid(row=1,column=1,padx=10,pady=10)

ent_nome_usuario = tk.Entry(janela, font="arial")
ent_nome_usuario.grid(row=2,column=2,padx=10,pady=10)

ent_ano_de_nascimento = tk.Entry(janela, font="arial")
ent_ano_de_nascimento.grid(row=2,column=1,padx=10,pady=10)

btn_cadastrar = tk.Button(janela, text="Cadastrar", command=caucular_idade)
btn_cadastrar.grid(row=5,column=1,padx=10,pady=10)

janela.mainloop()