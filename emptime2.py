# com esse script você pode calcular o tempo perdido pelo kurapika do hunter x hunter quando ele usa o emperor time, em horas!


horas = float(input('Olá, Kurapika! Digite quantas horas você usou o Emperor Time aqui: '))

s = horas * 3600 #segundos perdidos
dp = s/24 #dias perdidos
ap = dp/365 # anos perdidos

print('Kurapika usou o Emperor Time por {} segundos, ele perdeu {} horas de vida, {} dias, e {} anos'.format(s,s, dp, ap))


