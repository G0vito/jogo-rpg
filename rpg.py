from time import sleep
import sys
def animafrase(frase):
    for letra in list(frase):
        sys.stdout.write(letra)
        sleep(0.17)
    sys.stdout.flush()

print('''
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
''')
animafrase (''' Acordas ..... Olhas à tua volta ...  Não consegues entender onde estás, nem quem tu és, mas aos poucos vais te conseguindo lembrar.
Olhas á tua volta e entendes que estas numa sala bem bonita e estás deitado numa cama bem suave.
Levantas-te e começas á procura de alguém. 
Quando te aproximas da porta, vês alguém a aproximar-se. 
Como não sabes quêm é, voltas para dentro do quarto e agarras numa espada que está perto da tua cama.
O individo entra no teu quarto vês que é uma equipa de guerreiras, o lider, dirigindo-se a ti, diz: Lembras-te do teu nome SOLDADO? ''')
sleep(3)
print()
personagem = input('Qual o teu Nome?')
print()
sleep(2)
animafrase(f'É isso! Eu sou o {personagem}')
animafrase(''' E... E... eu sou um...''')
sleep(2)
animafrase('''

    [1]Guerreiro
    [2]Curandeiro
    [3]Arqueiro
''')
escolha1 = input('Eu sou um:')
animafrase('...')
sleep(3)
tipo = ''
if escolha1 == '1':
    animafrase('Eu sou um Guerreiro')
    tipo='Guerreiro'
elif escolha1 == '2':
    animafrase('Eu sou um Curandeiro')
    tipo='Curandeiro'
elif escolha1 == '3':
    animafrase('Eu sou um Arqueiro')
    tipo='Arqueiro'
sleep(2)
print()
animafrase('Ficas paralisado durante um bocadinho enquanto as tuas memorias vão voltando')
sleep(2)
animafrase('...')
animafrase('de repente dás um salto e corres para a janela.')
sleep(2)
animafrase('atavés da janela vês que estás em plena guerra....')
sleep(2)
animafrase(f'Recordas-te que á poucos dias atrás eras um {tipo} na guerra e que foste baleado e que por isso foste trazido para o local onde estás neste momento')
sleep(1)
animafrase('''Agora podes escolher entre:
     [1]Ficares até recuperares e depois voltares para a tua familia
     [2]Voltar para a guerra
''')
escolha2 = input('Eu vou:')
if escolha2 == '1':
    animafrase('OBRIGADO POR TERES LUTADO AO NOSSO LADO... ESPERO VOLTAR A VER-TE')
elif escolha2 == '2':
    animafrase('É UM PRAZER QUE VOLTES A LUTAR AO NOSSO LADO...')