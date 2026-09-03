#tela de login

from utilidades import menu, cabecalho
from rich import print

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def login():
    nome = input('Digite seu nome: ').strip()
    senha = input('Digite sua senha: ').strip()

    try:
        with open('dados.txt', 'rt') as arquivo:
            jogadores = arquivo.readlines()

    except FileNotFoundError:
        print('[red]Arquivo de dados não encontrado![/]')
        return None

    for linha in jogadores:
        dados = linha.strip().split(';')

        if len(dados) < 7:
            continue

        if dados[0] == nome and dados[1] == senha:

            jogador = Jogador(dados[0], dados[1])

            jogador.vitorias = int(dados[2])
            jogador.derrotas = int(dados[3])
            jogador.empates = int(dados[4])
            jogador.partidas = int(dados[5])
            jogador.taxa_de_vitorias = float(dados[6])

            print(f'[green]Login realizado com sucesso! Bem-vindo, {jogador.nome}![/]')

            return jogador

    print('[red]Nome ou senha incorretos![/]')
    return None

class Jogador:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.vitorias = 0
        self.derrotas = 0
        self.empates = 0
        self.partidas = 0
        self.taxa_de_vitorias = 0

def criar_conta():
    nome = input('Digite seu nome: ').strip()
    senha = input('Digite sua senha: ').strip()

    try:
        with open('dados.txt', 'rt') as arquivo:
            jogadores = arquivo.readlines()

    except FileNotFoundError:
        print('[red]Arquivo de dados não encontrado![/]')
        return

    for linha in jogadores:
        dados = linha.strip().split(';')

        if dados and dados[0] == nome:
            print('[red]Esse nome de usuário já está cadastrado![/]')
            return

    jogador1 = Jogador(nome, senha)

    try:
        with open('dados.txt', 'at') as arquivo:
            arquivo.write(
                f'{jogador1.nome};'
                f'{jogador1.senha};'
                f'{jogador1.vitorias};'
                f'{jogador1.derrotas};'
                f'{jogador1.empates};'
                f'{jogador1.partidas};'
                f'{jogador1.taxa_de_vitorias}\n'
            )

    except Exception as erro:
        print(f'[red]Erro ao salvar a conta: {erro}[/]')
        return

    print('[green]Conta criada com sucesso![/]')