# main

from utilidades import menu
from random import randint
from rich import print
from funcoes import jogador_pedra, jogador_papel, jogador_tesoura
from time import sleep

jogadas = ['PEDRA', 'PAPEL', 'TESOURA']


while True:
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