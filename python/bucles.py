###########BUCLES########### 
#### ciclo while, el más usado ####
##EJERCICIO 1: imprimir el resultado de la potencia de 2 hasta llegar a un resultado anterior a 1000000
# def run():
#     #la variable en mayuscula es una CONSTANTE, no cambia su valor a lo largo del programa
#     LIMITE = 100000

#     contador = 0
#     #el doble ** quiere decir POTENCIA
#     potencia_2 = 2**contador
#     #"mientras la potencia de 2 sea menor al limite, se ejecuta el while"
#     while potencia_2<LIMITE:
#         print("2 elevado a " + str(contador) + 
#               " es igual a: " + str(potencia_2)) 
#         contador = contador+1
#         potencia_2 = 2**contador

##EJERCICIO 2: imprimir los numeros hasta el 100
# def run():
#     contador = 1
#     print("primer contador: " + str(contador))
#     while contador < 100:
#         contador += 1 #es como poner contador = contador +1
#         print(contador)

# if __name__ == '__main__':
#     run()


#### ciclo for, el más conocido ####
##EJERCICIO 1: imprimir del 1 al 100 (inclusive)
##EJERCICIO 2: imprimir la tabla del 5 (desde 5*1 hasta 5*10)
#a = range(100)
#print(a)
# acá a equivale al rango hasta 100 -> [0,100] No inclusive

# RANGE es una función que puede recibir más parámetros: 
# range(velor inicial, valor final-noinclivo-)
def run():
    for contador in range(1,101):#para la variable CONTADOR en el rango de 100 (imprimir)
        print(contador)

    #imprimo la tabla del 5
    print("imprimimos la tabla del 5")
    for i in range(1,11):
        print (5*i)


if __name__ == '__main__':
    run()