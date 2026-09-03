# Utilidades

from rich import print


def linha(tamanho=40):
    return '-' * tamanho


def cabecalho(txt):

    print(linha())
    print(txt.center(40))
    print(linha())


def leia_natural(msg):

    while True:

        try:
            numero = int(input(msg))

        except ValueError:

            print(
                '[red]ERRO: Digite um número inteiro válido.[/]'
            )

            continue

        except KeyboardInterrupt:

            print(
                '\n[red]Programa interrompido pelo usuário.[/]'
            )

            return 0

        if numero >= 0:
            return numero

        print(
            '[red]ERRO: Digite um número maior ou igual a zero.[/]'
        )


def menu(titulo, lista):

    cabecalho(titulo.upper())

    for numero, item in enumerate(lista, 1):

        print(f'{numero} - {item}')

    print(linha())

    while True:

        opcao = leia_natural('Sua opção: ')

        if 1 <= opcao <= len(lista):
            return opcao

        print('[red]Erro: Opção inválida![/]')