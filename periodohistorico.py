print('-------------------------------------------------------------')
print('                 ACHE SEU PERÍODO HISTÓRICO!                  ')
print('-------------------------------------------------------------')

n1 = int(input('Insira a data que você quer pesquisar aqui: '))


if n1 < 476:
    print('O ano que você pesquisou é {} d.C, e fica no período da Idade Antiga!'.format(n1))
elif 476 <= n1 <= 1492:
    print('O ano que você pesquisou é {} d.C, e fica no período da Idade Média!'.format(n1))
elif 1492 <= n1 <= 1789:
    print('O ano que você pesquisou é {} d.C, e fica no período da Idade Moderna!'.format(n1))
elif 1789 <= n1 <= 2021:
    print('O ano que você pesquisou é {} d.C, e fica no período da Idade Contemporânea!'.format(n1))
elif n1 > 2021:
    print('O ano que você pesquisou é {} d.C, e fica no período do futuro!'.format(n1))
