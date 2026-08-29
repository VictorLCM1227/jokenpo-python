# funcoes

def jogador_pedra(pc):
    if pc == 1:
        return 'Empatou!'
    elif pc == 2:
        return 'Perdeu!'
    else:
        return 'Venceu!'

def jogador_papel(pc):
    if pc == 1:
        return 'Venceu!'
    elif pc == 2:
        return 'Empatou!'
    else:
        return 'Perdeu!'

def jogador_tesoura(pc):
    if pc == 1:
        return 'Perdeu'
    elif pc == 2:
        return 'Venceu!'
    else:
        return 'Empatou!'


    
