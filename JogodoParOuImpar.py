from random import randint
v = 0

while True:
    jogador = int(input('Diga um número: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('P/I: ')).strip().upper()[0]
    print(f'Você disse o número {jogador}, e o computador pensou no número {computador}. O total é {total}', end=' ')
    print('Deu par' if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('O computador venceu')
            break
    elif tipo =='I':
        if total % 2 == 1:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
        print('Vamos jogar novamente hehehe')
print(f'Gamer Over !, você venceu {v} vezes')