def conversor (dato_moneda, valor_moneda_a_convertir):
    pesos = input("Dinero en "+ dato_moneda + ": ")
    pesos = float(pesos)
   # valor_dolar = 213
    valor_moneda_convertida = pesos/valor_moneda_a_convertir
    valor_moneda_convertida = round(valor_moneda_convertida, 2)
    valor_moneda_convertida = str(valor_moneda_convertida)
    print("tienes $" + valor_moneda_convertida + " dólares")

menu = """""""""
Bienvenido al conversor de monedas 💰💰

1- pesos argentinos a dolares
2- dolares a pesos argentinos

Elige una opcion: 
"""

opcion = input(menu)

if opcion == "1":
    conversor("pesos argentinos", 206)
elif opcion == "2":
    conversor("dolares", 0.0094)
else:
    print("ingrese una opcion valida")


# def suma(num_a, num_b):
#     print('se suman dos numeros')
#     # resultado = num_a+num_b
#     return num_a+num_b
# sumatoria = suma(1,4)
# print(sumatoria) 