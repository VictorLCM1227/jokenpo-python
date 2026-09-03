# usuarios

from rich import print
from jogador import Jogador


ARQUIVO = 'dados.txt'


def arquivo_existe():

    try:
        with open(ARQUIVO, 'rt'):
            return True

    except FileNotFoundError:
        return False


def criar_arquivo():

    try:
        with open(ARQUIVO, 'wt'):
            pass

    except Exception as erro:
        print(f'[red]Erro ao criar arquivo: {erro}[/]')


def carregar_jogadores():

    jogadores = []

    try:

        with open(ARQUIVO, 'rt') as arquivo:

            for linha in arquivo:

                linha = linha.strip()

                if not linha:
                    continue

                dados = linha.split(';')

                if len(dados) != 7:
                    continue

                jogador = Jogador(
                    dados[0],
                    dados[1]
                )

                jogador.vitorias = int(dados[2])
                jogador.derrotas = int(dados[3])
                jogador.empates = int(dados[4])
                jogador.partidas = int(dados[5])
                jogador.taxa_de_vitorias = float(dados[6])

                jogadores.append(jogador)

    except FileNotFoundError:
        return []

    return jogadores


def salvar_jogador(jogador):

    jogadores = carregar_jogadores()

    for i, jogador_salvo in enumerate(jogadores):

        if jogador_salvo.nome == jogador.nome:
            jogadores[i] = jogador
            break

    else:
        jogadores.append(jogador)

    try:

        with open(ARQUIVO, 'wt') as arquivo:

            for jogador in jogadores:

                arquivo.write(
                    f'{jogador.nome};'
                    f'{jogador.senha};'
                    f'{jogador.vitorias};'
                    f'{jogador.derrotas};'
                    f'{jogador.empates};'
                    f'{jogador.partidas};'
                    f'{jogador.taxa_de_vitorias:.2f}\n'
                )

    except Exception as erro:

        print(f'[red]Erro ao salvar jogador: {erro}[/]')


def criar_conta():

    print()
    nome = input('Digite seu nome: ').strip()
    senha = input('Digite sua senha: ').strip()

    if not nome or not senha:
        print('[red]Nome e senha não podem estar vazios![/]')
        return

    jogadores = carregar_jogadores()

    for jogador in jogadores:

        if jogador.nome == nome:

            print(
                '[red]Esse nome de usuário já está cadastrado![/]'
            )

            return

    novo_jogador = Jogador(nome, senha)

    jogadores.append(novo_jogador)

    salvar_jogador(novo_jogador)

    print('[green]Conta criada com sucesso![/]')


def login():

    print()

    nome = input('Digite seu nome: ').strip()
    senha = input('Digite sua senha: ').strip()

    jogadores = carregar_jogadores()

    for jogador in jogadores:

        if jogador.nome == nome and jogador.senha == senha:

            print(
                f'[green]Login realizado com sucesso! '
                f'Bem-vindo, {jogador.nome}![/]'
            )

            return jogador

    print('[red]Nome ou senha incorretos![/]')

    return None


def ranking():

    jogadores = carregar_jogadores()

    jogadores.sort(
        key=lambda jogador: jogador.taxa_de_vitorias,
        reverse=True
    )

    return jogadores