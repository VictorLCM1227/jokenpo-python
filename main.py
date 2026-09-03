# main

from random import randint
from time import sleep

from rich import print

from jogador import Jogador
from usuarios import (
    arquivo_existe,
    criar_arquivo,
    criar_conta,
    login,
    salvar_jogador,
    ranking
)

from funcoes import (
    resultado_jogada,
    mensagem_resultado,
    nome_jogada
)

from utilidades import menu, cabecalho


ARQUIVO = 'dados.txt'


# Cria o arquivo caso ele ainda não exista
if not arquivo_existe():
    criar_arquivo()


while True:

    # ==========================================
    # MENU INICIAL
    # ==========================================

    escolha = menu(
        'JOKENPÔ',
        [
            'Sair',
            'Login',
            'Criar conta',
            'Ranking'
        ]
    )


    # ==========================================
    # SAIR
    # ==========================================

    if escolha == 1:

        cabecalho('SAINDO...')

        break


    # ==========================================
    # LOGIN
    # ==========================================

    elif escolha == 2:

        jogador_atual = login()

        if jogador_atual is None:
            continue


        # ======================================
        # MENU DO JOGADOR
        # ======================================

        while True:

            escolha_jogador = menu(
                f'{jogador_atual.nome.upper()}',
                [
                    'Jogar',
                    'Minhas estatísticas',
                    'Logout'
                ]
            )


            # ==================================
            # JOGAR
            # ==================================

            if escolha_jogador == 1:

                while True:

                    escolha_jogador_jogada = menu(
                        'JOKENPÔ',
                        [
                            'PEDRA',
                            'PAPEL',
                            'TESOURA'
                        ]
                    )

                    pc = randint(1, 3)


                    # Animação
                    print('JO')
                    sleep(0.5)

                    print('KEN')
                    sleep(0.5)

                    print('PÔ!!!')
                    print()


                    print(
                        f'Você escolheu: '
                        f'{nome_jogada(escolha_jogador_jogada)}'
                    )

                    print(
                        f'Computador escolheu: '
                        f'{nome_jogada(pc)}'
                    )

                    print()


                    # Descobre resultado
                    resultado = resultado_jogada(
                        escolha_jogador_jogada,
                        pc
                    )


                    # Mostra resultado
                    print(
                        mensagem_resultado(resultado)
                    )


                    # Atualiza jogador
                    jogador_atual.registrar_resultado(
                        resultado
                    )


                    # Salva no TXT
                    salvar_jogador(jogador_atual)


                    print()

                    continuar = input(
                        'Deseja continuar jogando? [S/N] '
                    ).lower().strip()


                    while continuar not in ['s', 'n']:

                        print(
                            '[red]Opção inválida. '
                            'Digite S ou N.[/]'
                        )

                        continuar = input(
                            'Deseja continuar jogando? [S/N] '
                        ).lower().strip()


                    if continuar == 'n':
                        break


            # ==================================
            # ESTATÍSTICAS
            # ==================================

            elif escolha_jogador == 2:

                cabecalho('MINHAS ESTATÍSTICAS')

                print(
                    f'Jogador: {jogador_atual.nome}'
                )

                print(
                    f'Partidas: {jogador_atual.partidas}'
                )

                print(
                    f'Vitórias: {jogador_atual.vitorias}'
                )

                print(
                    f'Derrotas: {jogador_atual.derrotas}'
                )

                print(
                    f'Empates: {jogador_atual.empates}'
                )

                print(
                    f'Taxa de vitória: '
                    f'{jogador_atual.taxa_de_vitorias:.2f}%'
                )

                input('\nPressione ENTER para continuar...')


            # ==================================
            # LOGOUT
            # ==================================

            elif escolha_jogador == 3:

                cabecalho('LOGOUT')

                break


    # ==========================================
    # CRIAR CONTA
    # ==========================================

    elif escolha == 3:

        criar_conta()


    # ==========================================
    # RANKING
    # ==========================================

    elif escolha == 4:

        cabecalho('RANKING')

        jogadores = ranking()

        if not jogadores:

            print('Nenhum jogador cadastrado.')

        else:

            print(
                'Pos.  Jogador              '
                'Vitórias  Partidas  Taxa'
            )

            print(linha := '-' * 60)

            for posicao, jogador in enumerate(
                jogadores,
                1
            ):

                print(
                    f'{posicao:<6}'
                    f'{jogador.nome:<21}'
                    f'{jogador.vitorias:<10}'
                    f'{jogador.partidas:<10}'
                    f'{jogador.taxa_de_vitorias:.2f}%'
                )

        input('\nPressione ENTER para continuar...')


print()
print('Obrigado por jogar!!!')
print('<< VOLTE SEMPRE >>')