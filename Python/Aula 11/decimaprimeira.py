# Tinker

# Componentes principais

# tk : a janela 
# label : Texto em rotulo
# Button: um botão de clique
# Entry: Um campo de entrada de texto

# Biblioteca
# import tkinter as tk
# from tkinter import messagebox

# # 1.Criar janela principal
# janela = tk.Tk()
# janela.configure(bg="white")
# janela.title("Minha Primeira Janela em GUI")
# janela.geometry("1680x800") #Largura e Altura

# # 2.Criar a função que vai executar (evento)
# def mostrar_mensagem():
#     messagebox.showinfo("Sucesso", "Você clicou no botão! :>")

# # 3.Criar componentes (widgets)
# lbl_titulo = tk.Label(janela, text="Bem-vindo à aula de Tkinter!", 
# font=("Arial", 30, "bold"), bg="#FAFAFA")
# btn_clique = tk.Button(janela, text="Clique aqui :>", font=("Arial", 30), bg="#080808", fg="White", command=mostrar_mensagem)

# # 4.Posicionar os componetes
# lbl_titulo.pack(pady=20) #pady (y) posicionar verticalmente
# btn_clique.pack(padx=20) #padx (x) posicionar horizontalmente


# # 5. Rodar o loop da interface
# janela.mainloop()


import tkinter as tk
from tkinter import messagebox

# 1. Configurar evento

def solcitar_informacoes():
    # .get() serve para buscar o texto que foi digitado
    nome_usuario = campo_nome.get()
    idade_usuario = campo_idade.get()
    if nome_usuario == "":
        messagebox.showwarning("Aviso", "Por-favor digite seu nome")
    else:
        messagebox.showinfo("Saudações, querido aluno", f"olá {nome_usuario} Seja bem-vindo ao mundo das interfaces gráfica. E sua idade é {idade_usuario}")

    
# 2. Configuração de janela
app = tk.Tk()
app.title("Tela de usuário")
app.geometry("300x300")


# 3.Componentes
lbl_idade_usuario = tk.Label(app, text="Digite sua idade").grid (row=0, column=3, padx=10, pady=10)


campo_idade = tk.Entry(app, font=("Arial", 17))
campo_idade.grid(row=1, column=3, pady=15)

lbl_nom_usuario = tk.Label(app, text="Digite seu nome")
lbl_nom_usuario.grid(row=2, column=0, pady=15)

campo_nome = tk.Entry(app, font=("Arial", 17))
campo_nome.grid(row=3, column=0, pady=15)

btn_cadastrar = tk.Button(app, text="Cadastrar", command=solcitar_informacoes)
btn_cadastrar.grid(row=4, column=0, pady=15)

btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
btn_fechar.grid(row=1, column=0, pady=5)
# 4.Rodar Interface
app.mainloop()























