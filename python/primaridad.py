def es_primo(numero):
    contador = 0
    
    for i in range(1, numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i ==0:
            contador += 1
    if contador == 0:
        return True
    else: 
        return False

def run():
    numero = int(input("ingresa un numero: "))
    if es_primo(numero): #puedo agregar == True
        print("es Primo")
    else: 
        print("no es primo")

if __name__ == '__main__':
    run()


    ###TAREA: hacer un código más eficiente