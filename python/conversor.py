pesos = input("Dinero en pesos: ")
pesos = float(pesos) 
valor_dolar = 213
dolares_que_tenemos = pesos/valor_dolar
dolares_que_tenemos = round(dolares_que_tenemos, 2)
dolares_que_tenemos = str(dolares_que_tenemos)
print("tienes $" + dolares_que_tenemos + " dólares")
print("ahora probamos de dolares a pesos")
dolares_que_tenemos = input("Dinero en dolares: ")
dolares_que_tenemos = float(dolares_que_tenemos)
valor_peso = 1/valor_dolar
pesos_finales = dolares_que_tenemos/valor_peso
pesos_finales = round(pesos_finales,2)
pesos_finales = str(pesos_finales)
print("tienes $"+pesos_finales+"pesos")
