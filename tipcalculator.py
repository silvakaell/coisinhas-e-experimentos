account_original = float(input("Insira o valor da conta: "))
person = float(input(("Insira a quantidade de pessoas que irá pagar: ")))
percentage = float(input("Insira a porcentagem:"))

#esse é o valor em números da porcentagem, que tenho de adicionar no valor original
account_add = account_original * percentage/100

account_final = round(account_original + account_add, 2)

valor_per_person = round(account_final/person, 2)

print(f"O valor total será de {account_final}, e cada pessoa deverá pagar {valor_per_person}")
