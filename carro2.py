vel = float(input("Insira a velocidade do carro: "))


if vel < 80:
    print("Carro na velocidade certa!")
elif 80 < vel < 100:
    preco = (vel - 80) * 5
    print(f"Sua velocidade de {vel} é acima do limite! Pagará {preco} de multa")
elif vel > 100:
    preco = (vel - 100) * 20
    print(f"Sua velocidade de {vel} é acima do limite! Pagará {preco} de multa")


