###recorrer string: generar un ciclo a partir de una cadena de caracteres
###                 para ir caracter por caracter en cada vuelta del ciclo for

def run():
    print("vamos a imprimir letra por letra de la palabra ingresada")
    nombre = input("Escribe tu nombre: ")
    for caracter in nombre: #para la variable LETRA en la variable NOMBRE (imprimo cada letra en cada repeticion)
        print (caracter)

    print("vamos a imprimir letra por letra de la frase ingresada, con metodo upper")
    frase = input("escriba una frase: ")
    for caracter in frase: 
        print(caracter.upper())

if __name__ == "__main__":
    run()