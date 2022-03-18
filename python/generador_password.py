import random


def generar_password():
    #genero 4 listas de símbolos que voy a usar porque tenemos Mayu, minus, num, simbolos
    mayusculas = ["A", "B", "C", "D", "E", "F", "G"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g"]
    simbolos = [ "!", "#", "$", "&", "/", "?", "="]
    numeros = ["1", "2", "3", "4", "5", "6", "7"]

    #combinamos todos los caracteres anteriores
    caracteres = mayusculas + minusculas + simbolos + numeros
    #generamos una lista vacía para luego ponerle caracteres aleatorios
    password = []

    #ciclo for de 15 vueltas
    for i in range(15):
        #función .choice se elige un caracter al azar (de la lista)
        caracter_random = random.choice(caracteres)
        #función .append para meter el caracter en la última posición de la lista (caracter_random)
        password.append(caracter_random)

    #hacemos que todos los caracteres queden unidos en una sola cadena
    password = "".join(password)
    return password


def run():
    password_created = generar_password()
    print("Tu nueva contraseña es: " + str(password_created))


if __name__ == "__main__":
    run()