from random import randint

corpo = [
    '''
    +-----+
    |     |
          |
          |
          |
          |
          |
          |
===========''',
    '''
    +-----+
    |     |
    O     |
          |
          |
          |
          |
          |
===========''',
    '''
    +-----+
    |     |
    O     |
    |     |
          |
          |
          |
          |
===========''',
    '''
    +-----+
    |     |
    O     |
   /|     |
          |
          |
          |
          |
===========''',
    '''
    +-----+
    |     |
    O     |
   /|\\    |
          |
          |
          |
          |
===========''',
    '''
    +-----+
    |     |
    O     |
   /|\\    |
   /      |
          |
          |
          |
===========''',
    '''
    +-----+
    |     |
    O     |
   /|\\    |
   / \\    |
          |
          |
          |
=========='''
]

palavras = ['banana', 'abacaxi', 'laranja', 'melancia', 'uva',
            'morango', 'kiwi', 'manga', 'pessego', 'caju']


def get_palavra(p_lista):
    return p_lista[randint(0, len(p_lista) - 1)]


def display(corpo, letras_erradas, letras_certas, palavra):
    print(corpo[len(letras_erradas)])
    print()

    print('Letras erradas:', ' '.join(letras_erradas))
    print()

    lacuna = ['_' if letra not in letras_certas else letra for letra in palavra]
    print(' '.join(lacuna))
    print()


def get_chute(letras_digitadas):
    """Garante que o usuário digite apenas uma letra que ainda não foi usada"""
    while True:
        chute = input('Chute: ').lower().strip()

        if len(chute) != 1:
            print('\033[7;31mDigite apenas uma letra.\033[m')
        elif chute in letras_digitadas:
            print('\033[7;32mVocê já escolheu essa letra. Escolha outra.\033[m')
        elif chute not in 'abcdefghijklmnopqrstuvwxyz':
            print('Digite apenas letras.')
        else:
            return chute


def jogar_novamente():
    return input('Quer jogar novamente? (sim ou não) ').lower().startswith('s')


print('-- C A R R A S C O --')
letras_erradas = ''
letras_certas = ''
palavra_secreta = get_palavra(palavras)
jogo_terminado = False

while True:
    display(corpo, letras_erradas, letras_certas, palavra_secreta)

    chute = get_chute(letras_erradas + letras_certas)

    if chute in palavra_secreta:
        letras_certas += chute

        p_completa = True
        for letra in palavra_secreta:
            if letra not in letras_certas:
                p_completa = False
                break

        if p_completa:
            print(f'Parabéns! Você acertou a palavra secreta: {palavra_secreta}!')
            jogo_terminado = True
    else:
        letras_erradas += chute

        if len(letras_erradas) == len(corpo) - 1:
            display(corpo, letras_erradas, letras_certas, palavra_secreta)
            print(f'Você perdeu! A palavra era {palavra_secreta}.')
            jogo_terminado = True

    if jogo_terminado:
        if jogar_novamente():
            letras_erradas = ''
            letras_certas = ''
            jogo_terminado = False
            palavra_secreta = get_palavra(palavras)
        else:
            break
