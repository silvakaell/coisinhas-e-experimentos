import random
from time import sleep

starwars = random.randint(1, 11)

print('-=' * 20)
print('Vou selecionar para você um filme da saga Star Wars. Aguarde: ')
print('-=' * 20)


opcao = False

while not opcao:
    print('PROCESSANDO.....')
    sleep(2)
    starwars = random.randint(1, 11)
    if starwars == 1:
        print('O filme escolhido foi Episódio 1: Ameaça Fantasma.')
    elif starwars == 2:
        print('O filme escolhido foi Episódio 2: Ataque dos Clones.')
    elif starwars == 3:
        print('O filme escolhido foi Episódio 3: Vingança dos Sith.')
    elif starwars == 4:
        print('O filme escolhido foi Episódio 4: Uma Nova Esperança.')
    elif starwars == 5:
        print('O filme escolhido foi Episódio 5: O Império Contra Ataca.')
    elif starwars == 6:
        print('O filme escolhido foi Episódio 6: Retorno de Jedi.')
    elif starwars == 7:
        print('O filme escolhido foi Episódio 7: O Despertar da Força.')
    elif starwars == 8:
        print('O filme escolhido foi Episódio 8: Os Últimos Jedi.')
    elif starwars == 9:
        print('O filme escolhido foi Episódio 9: A Ascensão Skywalker.')
    elif starwars == 10:
        print('O filme escolhido foi Han Solo.')
    elif starwars == 11:
        print('O filme escolhido foi Rogue One.')
    o = str(input('Deseja selecionar outro filme? S/N: ')).strip().upper()[0]
    if o == 'N':
        opcao = True
    elif o == 'S':
        opcao = False
    else:
        o = str(input('Comando incorreto. Deseja continuar? S/N: '))
        if o == 'N':
            opcao = True
        elif o == 'S':
            opcao = False
        else:
            opcao = True
            print('Comando incorreto. O programa será encerrado.')

print('=' * 20)

print('Bom filme!')
