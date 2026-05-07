# manipulacao_arquivos = input("Manipulação de arquivos de texto com PYTHON")
# print(manipulacao_arquivos.upper() ) #Maiúscula
# print(manipulacao_arquivos.lower()) #Minúscula
# print(manipulacao_arquivos.strip()) #Remover espaços em branco
# print(manipulacao_arquivos.split()) #divide string em uma lista de palavras
# print(manipulacao_arquivos.replace("Python","Java")) #Substitui python por java
# print(manipulacao_arquivos.count("a")) #Conta quantas vezes a letra "a" aparece na string
# print(manipulacao_arquivos.upper().count("PYTHON")) # Conta quantas vezes a letra "PYTHON" aparece na string e converte para maiúsculas
# print(manipulacao_arquivos.strip().count("python")) # Conta quantas vezes a letra "python" aparece na string, removendo os espaços em branco
# print(manipulacao_arquivos.find("Python")) # Mostra a posição em caracteres da primeira vez em que a palavra citada "python" aparece
# print(manipulacao_arquivos.title()) # Converte a primeira letra de cada palavra para maiúscula
# print(manipulacao_arquivos.swapcase()) # Converte as letras maiúsculas para minúsculas e vice-versa
# print(manipulacao_arquivos.center(50, "*")) # Centraliza a string e preenche com "*" até atingir 50 caracteres
# print(manipulacao_arquivos.startswith("    Manipulação")) # Verifica se a string começa com "    Manipulação"


# Exercicio 1:
# Crie um algoritmo onde peça para inserir uma frase e deixa-a formatada com maiuscula e acrescente uma contagem de cada frase.

# print("insira uma frase")
# frase = input("Qual frase você deseja inserir?")
# print(frase.upper())
# print(frase.count(""))

# Manipilação de arquivos
# Escrevendo em um arquivo
# with open("arquivo.txt", "w") as exemplo:  
#     exemplo.write("Exemplo de Clean code - Aula 8\n")
#     exemplo.write("Continuando a escrever no arquivo\n")
  
# with open ("arquivo.py", "w") as python:
#     python.write('print("Exemplo de arquivo Python")')

# # Lendo arquivo
# with open ("arquivo.py", "r") as exemplo:
#     conteudo = exemplo.read()
#     print(conteudo)

# with open ("arquivo.py","a") as python:
#     python.write('\nprint("Continuando a escrever no arquivo Python")')
#     python.write('\nprint("Mais uma linha no arquivo Python")')
# import os
# Criando um diretótio
# os.mkdir("teste")

# Renomear pastas
# os.rename("teste", "Aulas")

# os.rmdir("Aulas")
# os.mknod("teste.txt")
# os.touch("aula.txt")
# print(os.listdir())
# print(os.listdir(".."))
# print(os.listdir("C:\\"))

# Exercicio 2:
# Crie um algoritmo para criação de um arquivo que irá desligar o computador.

# with open ("desligar.bat", "w") as desligar:
#     desligar.write('shutdown /s /t 120 /c "cestou rala peito" ')

# with open ("cancelartrabalho.bat", "w") as cancelar:
#     cancelar.write('shutdown /a /c "vc cancelou, vai continuar trabanhando vagabundo"')


#Exercicio 4
import os 
os.mkdir("aula")
os.rename("aula", "AULA")
print(os.listdir("aula"))




































