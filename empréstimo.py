print('-=' * 20)
print('ANALISADOR DE EMPRÉSTIMOS')
print('-=' * 20)

v = float(input('Insira o valor da casa, em reais: '))
a = float(input('Insira em quantos anos você pretende pagar a casa: '))
s = float(input('Insira o valor do seu salário, em reais: '))

p = v / (a * 12)
m = s * 30 / 100

if p <= m:
    print(
        'Para pagar seu empréstimo de {:.2f} reais em {} anos, a prestação será de {:.2f} reais. O valor mínimo '
        'deve ser de {:.2f} reais. '
        'Seu empréstimo foi aprovado!'.format(v, a, p, m))
else:
    print('Para pagar seu empréstimo de {:.2f} reais em {} anos, a prestação será de {:.2f} reais. O valor mínimo '
          'deve ser de {:.2f} reais. Seu empréstimo '
          'infelizmente não foi aprovado'.format(v, a, p, m))
