import random #funciones que sirven para trabajar con la alietoriedad. usamos el MODULO

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("elige un numero del 1 al 100: "))
    contador = 0
    while numero_elegido != numero_aleatorio:
        if numero_elegido< numero_aleatorio:
            print("busca un numero más grande")
        else: 
            print("busca un numero más pequeño")
        numero_elegido = int(input("\ningresa otro número: "))
        contador +=1
    print("¡GANASTE!")
    print("te ha costado " + str(contador) + " intentos")


if __name__ == "__main__":
    run()



#DESAFIO: podemos hacer un juego con vidas?