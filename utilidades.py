# Utilidades

from rich import print
from rich.table import Table

def linha(tamanho=30):
    return '-' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

def leiaNatural(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('[red]ERRO: Por favor, digite um número inteiro válido.[/]')
            continue
        except KeyboardInterrupt:
            print('[red]Usuário preferiu não digitar esse número.[/]')
            return 0
        else:
            if numero >= 0:
                return numero
            print('[red]ERRO: Por favor, digite um número maior ou igual a zero.[/]')
            continue

def menu(titulo, lista):
    cabecalho(titulo.upper())
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    while True:
        opc = leiaNatural('Sua opção: ')
        if 1<= opc <= 3:
            break
        print('[red]Erro: Opção inválida![/]')
    return opc

