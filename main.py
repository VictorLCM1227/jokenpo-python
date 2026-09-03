# main

from tela_de_login import arquivoExiste, CriarArquivo, login, criar_conta
from utilidades import menu, cabecalho, menuInicial
from random import randint
from rich import print
from funcoes import jogador_pedra, jogador_papel, jogador_tesoura
from time import sleep

arq = 'dados.txt'

if not arquivoExiste(arq):
    CriarArquivo(arq)

jogadas = ['PEDRA', 'PAPEL', 'TESOURA']


while True:
    escolha_inicial = menuInicial('JOKENPÔ', ['Sair', 'Login', 'Criar conta', 'Ranking'])

    if escolha_inicial == 1:
        cabecalho('SAINDO...')
        break

    elif escolha_inicial == 2:
        login()

    elif escolha_inicial == 3:
        criar_conta()


    escolha_menu = menu('JOKENPÔ', ['PEDRA', 'PAPEL', 'TESOURA'])

    pc = randint(1, 3)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!!!')
    print()
    print(f'Você escolheu: {jogadas[escolha_menu - 1]}')
    print(f'Computador escolheu: {jogadas[pc - 1]}')
    print()
    print('Você', end=' ')

    match escolha_menu:
        
        case 1:
            print(jogador_pedra(pc))

        case 2:
            print(jogador_papel(pc))

        case 3:
            print(jogador_tesoura(pc))

    while True:
        continuar = input('Deseja continuar? [S/N] ').lower().strip()
        if continuar in 'sn':
            break
        print('Opção inválida. Somente Sim ou Não')
    if continuar == 'n':
        break

print()
print('Obrigado por jogar!!!')
print('<< VOLTE SEMPRE >>')