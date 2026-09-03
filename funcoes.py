# funcoes

def resultado_jogada(jogador, pc):

    if jogador == pc:
        return 'empate'

    if (
        jogador == 1 and pc == 3 or
        jogador == 2 and pc == 1 or
        jogador == 3 and pc == 2
    ):
        return 'vitoria'

    return 'derrota'


def mensagem_resultado(resultado):

    if resultado == 'vitoria':
        return '[green]Você venceu![/]'

    elif resultado == 'derrota':
        return '[red]Você perdeu![/]'

    elif resultado == 'empate':
        return '[yellow]Empatou![/]'


def nome_jogada(numero):

    jogadas = {
        1: 'PEDRA',
        2: 'PAPEL',
        3: 'TESOURA'
    }

    return jogadas[numero]