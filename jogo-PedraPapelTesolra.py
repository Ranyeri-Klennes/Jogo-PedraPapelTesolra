from random import randint
import os 

maquina = randint(1,4)

while True:
    # - ler opção do usuário (1-pedra, 2-papel, 3-tesoura) e mostrar opção selecionada;
    print('Escolha um número para sua opção desejada:')
    print('1 - PEDRA')
    print('2 - PAPEL')
    print('3 - TESOURA')
    print('-'*20)
    voce = int(input())
    print('-'*20)
    
    os.system('cls')

    # - programa sortear algum número, mostrar na tela e comparar com o do usuário;
    # - comparar vocees que são melhores que os outros;
    # - mostrar mensagem de resultado.
    if voce == 1 and maquina == 1:
        print('Você e a máquina escolheram PEDRA!')
        print('EMPATE!')
        print('-'*20)
    elif voce == 1 and maquina == 2:
        print('Você escolheu PEDRA!')
        print('A máquina escolheu PAPEL!')
        print('PAPEL envolve a PEDRA!')
        print('VOCÊ PERDEU!')
        print('-'*20)
    elif voce == 1 and maquina == 3:
        print('Você escolheu PEDRA!')
        print('A máquina escolheu TESOURA!')
        print('PEDRA quebra a TESOURA!')
        print('VOCÊ GANHOU!')
        print('-'*20)

    elif voce == 2 and maquina == 2:
        print('Você e a máquina escolheram PAPEL!')
        print('EMPATE!')
        print('-'*20)
    elif voce == 2 and maquina == 1:
        print('Você escolheu PAPEL!')
        print('A máquina escolheu PEDRA!')
        print('PAPEL envolve a PEDRA!')
        print('VOCÊ GANHOU!')
        print('-'*20)
    elif voce == 2 and maquina == 3:
        print('Você escolheu PAPEL!')
        print('A máquina escolheu TESOURA!')
        print('PAPEL é picado pela TESOURA!')
        print('VOCÊ PERDEU!')
        print('-'*20)

    elif voce == 3 and maquina == 3:
        print('Você e a máquina escolheram TESOURA!')
        print('EMPATE!')
        print('-'*20)
    elif voce == 3 and maquina == 1:
        print('Você escolheu TESOURA!')
        print('A máquina escolheu PEDRA!')
        print('PEDRA quebra a TESOURA!')
        print('VOCÊ PERDEU!')
        print('-'*20)
    elif voce == 3 and maquina == 2:
        print('Você escolheu TESOURA!')
        print('A máquina escolheu PAPEL!')
        print('PAPEL é picado pela TESOURA!')
        print('VOCÊ GANHOU!')
        print('-'*20)
    else:
        print('ok')