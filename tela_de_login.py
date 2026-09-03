#tela de login

from utilidades import menu, cabecalho

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

class Jogador:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.vitorias = 0
        self.derrotas = 0
        self.empates = 0
        self.partidas = 0
        self.taxa_de_vitorias = 0

#def login():
    # pedir nome e senha e autenticar os dados no doas.txt


def criar_conta():
    # pedir nome, senha, cadastrar os dados no txt apos verificar se já existe ou não um jogador com esse nome
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')



resposta = menu('<< BEM VINDO!!! >>', ['Sair', 'Já tenho conta', 'criar conta'])

if resposta == 1:
    cabecalho('SAINDO...')
elif resposta == 2:
    cabecalho('TELA DE LOGIN')
elif resposta == 3:
    cabecalho('CRIAR NOVA CONTA')