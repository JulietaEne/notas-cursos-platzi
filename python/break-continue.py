def run():
    print("imprimir numeros del 0 al 100, si son multiplos de 10")
    for contador in range(101):
        if contador %10 != 0:
            continue #siempre que entro al if, salto una vuelta del ciclo sin pasar por el print
        print(contador)

    print("imprimir todos los numeros del 0 al 10, excepto el 5")
    for i in range (10):
        if i == 5:
            continue
        print(i)

    un_numero=input("ingrese un numero: ")
    un_numero = int(un_numero)
    print("imprimir numeros hasta hasta llegar al numero ingresado")
    for i in range (100000):
        print(i)
        if i == un_numero:
            break
        

if __name__ == "__main__":
    run ()