# funcoes

def jogador_pedra(pc):
    if pc == 1:
        return '[yellow]Empatou![/]'
    elif pc == 2:
        return '[red]Perdeu[/]!'
    else:
        return '[green]Venceu![/]'

def jogador_papel(pc):
    if pc == 1:
        return '[green]Venceu![/]'
    elif pc == 2:
        return '[yellow]Empatou![/]'
    else:
        return '[red]Perdeu![/]'

def jogador_tesoura(pc):
    if pc == 1:
        return '[red]Perdeu![/]'
    elif pc == 2:
        return '[green]Venceu![/]'
    else:
        return '[yellow]Empatou![/]'


    
