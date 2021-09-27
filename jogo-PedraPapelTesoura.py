from random import choice
from os import system
from time import sleep


valores = ['PEDRA', 'PAPEL', 'TESOURA']

while True:

    print('~'*55)
    print('BEM VINDO(A) AO JOGO DO PEDRA, PAPEL E TESOURA DO RANY!')
    print('~'*55,'\n')

    maquina = choice(valores)

    # print('-'*40)
    print('Escolha um número para sua opção desejada:')
    print('1 - PEDRA')
    print('2 - PAPEL')
    print('3 - TESOURA')
    print('-'*20)
    usuario = int(input())
    print('A máquina escolheu: ', maquina)

    # USUÁRIO JOGANDO PEDRA:
    if usuario == 1 and maquina == valores[0]:
        print('\nEMPATE!')
    elif usuario == 1 and maquina == valores[1]:
        print('\nPAPEL ENVOLVE PEDRA, VOCÊ PERDEU!')
    elif usuario == 1 and maquina == valores[2]:
        print('\nPEDRA QUEBRA TESOURA, VOCÊ GANHOU!')
    
    # USUÁRIO JOGANDO PAPEL:
    elif usuario == 2 and maquina == valores[0]:
        print('\nPAPEL ENVOLVE PEDRA, VOCÊ GANHOU!')
    elif usuario == 2 and maquina == valores[1]:
        print('\nEMPATE!')
    elif usuario == 2 and maquina == valores[2]:
        print('\nTESOURA CORTA PAPEL, VOCÊ PERDEU!')

    # USUÁRIO JOGANDO TESOURA:
    elif usuario == 3 and maquina == valores[0]:
        print('\nPEDRA QUEBRA TESOURA, VOCÊ PERDEU!')
    elif usuario == 3 and maquina == valores[1]:
        print('\nTESOURA CORTA PAPEL, VOCÊ GANHOU!')
    elif usuario == 3 and maquina == valores[2]:
        print('\nEMPATE!')

    else:
        print('\nInforme a opção correta!')

    sleep(4)
    system('cls')