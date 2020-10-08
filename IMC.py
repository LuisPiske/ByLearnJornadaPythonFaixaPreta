def imc(peso,altura):
    return peso / altura**2

peso = float(input('Entre com o seu peso: '))
altura = float(input('Entre com o seu altura: '))


print('O seu IMC vale: ' +str((imc(peso,altura))))
