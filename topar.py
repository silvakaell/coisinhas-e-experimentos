topar = {}

is_on = True

print("PROGRAMA DE DIÁRIO DE TRABALHO!")

while is_on:
    name = input('Insira o nome da pessoa: ')
    day = input("Insira a data de trabalho: ")
    ocup = input("Insira o procedimento: ")

    topar[name] = [{day: ocup}]

    resp = input('Deseja continuar? S/N: ').upper()
    if resp == "N":
        is_on = False
    elif resp ==  "P":
        print(topar)

print(topar)
