ligado = True

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def calcagua(maquina, cafe):
    valor = maquina - cafe
    return valor


def calcleite(maquina, leite):
    valor = maquina - leite
    return valor


def calcafe(maquina, cafe):
    valor = maquina - cafe
    return valor


def calcmoeda(real, cinc, vint, umdez):
    valor = real + (0.50 * cinc) + (0.25 * vint) + (0.10 * umdez)
    return valor


print('Máquina de café kamônica!')

umreal = float(input('Digite quantas moedas de 1 real você colocará na máquina: '))
umcinc = float(input('Digite quantas moedas de 50 centavos você colocará na máquina: '))
vint = float(input('Digite quantas moedas de 25 centavos você colocará na máquina: '))
umdez = float(input('Digite quantas moedas de 10 centavos você colocará na máquina: '))

valortotal = calcmoeda(umreal, umcinc, vint, umdez)
print(f'O valor de dinheiro que você colocou foi de {valortotal:.2f} reais')

while ligado:

    escolha = str(input('Escolha 1 para café puro, 2 para café com leite e 3 para capuccino: '))
    if escolha == '1':
        aguacafe = MENU['espresso']['ingredients']['water']
        aguamaq = resources['water']
        resources['water'] = calcagua(aguamaq, aguacafe)
        if calcagua(aguamaq, aguacafe) <= 0:
            print('Nao tem água suficiente.')
            break
        elif valortotal < 0.10:
            print('Você não possui dinheiro suficiente. Máquina encerrada.')
            break

        restoagua = (resources['water'])

        # Não tem leite né!

        cafecafe = MENU['espresso']['ingredients']['coffee']
        cafemaq = resources['coffee']
        resources['coffee'] = calcafe(cafemaq, cafecafe)
        restocafe = (resources['coffee'])
        if calcafe(cafemaq, cafecafe) <= 0:
            print('Nao tem café suficiente.')
            break

        valortotal = valortotal - 0.10

        print(f'Sobrou {restoagua} ml de água e {restocafe} ml de café.')
        print(f'Sobrou a quantia de {valortotal:.2f} reais.')
        print('Aproveite seu Café!')

    elif escolha == '2' and valortotal:
        aguacafe = MENU['latte']['ingredients']['water']
        aguamaq = resources['water']
        resources['water'] = calcagua(aguamaq, aguacafe)
        restoagua = (resources['water'])
        if calcagua(aguamaq, aguacafe) <= 0:
            print('Nao tem água suficiente. Máquina desligada.')
            break
        elif valortotal < 0.50:
            print('Você não possui dinheiro suficiente. Máquina encerrada.')
            break

        leitecafe = MENU['latte']['ingredients']['milk']
        leitemaq = resources['milk']
        resources['milk'] = calcleite(leitemaq, leitecafe)
        restoleite = (resources['milk'])
        if calcleite(leitemaq, leitecafe) <= 0:
            print('Nao tem leite suficiente. Máquina desligada.')
            break

        cafecafe = MENU['latte']['ingredients']['coffee']
        cafemaq = resources['coffee']
        resources['coffee'] = calcafe(cafemaq, cafecafe)
        restocafe = (resources['coffee'])
        if calcafe(cafemaq, cafecafe) <= 0:
            print('Nao tem café suficiente. Máquina desligada.')
            break

        valortotal = valortotal - 0.50

        print(f'Sobrou {restoagua} ml de água, {restoleite} ml de leite, e {restocafe} g de café.')
        print(f'Você tem {valortotal:.2f} na máquina')
        print('Aproveite seu Latte!')

    elif escolha == '3' and valortotal:
        aguacafe = MENU['cappuccino']['ingredients']['water']
        aguamaq = resources['water']
        resources['water'] = calcagua(aguamaq, aguacafe)
        restoagua = (resources['water'])
        if calcagua(aguamaq, aguacafe) <= 0:
            print('Nao tem água suficiente. Máquina desligada.')
            break
        elif valortotal < 1.25:
            print('Você não possui dinheiro suficiente. Máquina encerrada.')
            break

        leitecafe = MENU['cappuccino']['ingredients']['milk']
        leitemaq = resources['milk']
        resources['milk'] = calcleite(leitemaq, leitecafe)
        restoleite = (resources['milk'])

        cafecafe = MENU['cappuccino']['ingredients']['coffee']
        cafemaq = resources['coffee']
        resources['coffee'] = calcafe(cafemaq, cafecafe)
        restocafe = (resources['coffee'])
        if calcafe(cafemaq, cafecafe) <= 0:
            print('Nao tem café suficiente. Máquina desligada.')
            break

        valortotal = valortotal - 1.25

        print(f'Sobrou {restoagua} ml de água, {restoleite} ml de leite, e {restocafe} g de café.')
        print(f'Sobrou a quantia de {valortotal:.2f} reais.')
        print('Aproveite seu Cappuccino!')

    elif escolha == 'off':
        print('Máquina desligada! Até a próxima!')
        ligado = False

    elif escolha == 'report':
        print(f'A máquina tem a quantia de {valortotal} reais.')
        for produto, preco in resources.items():
            print(f'O prdduto {produto}: {preco} ml/g')

# função para fazer café pode retornar os valores subtraídos para o dicionário?
