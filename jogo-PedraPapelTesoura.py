from random import choice

valores = ['PEDRA', 'PAPEL', 'TESOURA']

while True:
    maquina = choice(valores)

    print('-'*40)
    print('Escolha um número para sua opção desejada:')
    print('1 - PEDRA')
    print('2 - PAPEL')
    print('3 - TESOURA')
    print('-'*40)
    usuario = input()
    print('A máquina escolheu: ', maquina)

    if usuario == 1 and maquina == valores[1]:
        print('EMPATE!')
    if usuario == 1 and maquina == valores[2]:
        print('PAPEL ENVOLVE PEDRA, VOCÊ GANHOU!')
    if usuario == 1 and maquina == valores[3]:
        print('TESOURA CORTA PAPEL, VOCÊ PERDEU!')
    else:
        print('ok')