#dejo dos espacios entre función y función
def palindromo (una_palabra):
    #acá vamos a eliminar todos los espacios entre palabras con REPLACE
    una_palabra=una_palabra.replace(" ","")
    #acá pasamos todas las letras a minusculas, para que lea todo igual
    una_palabra=una_palabra.lower()
    #acá vamos ainvertir la palabra, manejando como slyces e invirtiendo el orden de cada letra (desde principio a final, en -1)
    palabra_invertida = una_palabra[::-1]
    if una_palabra == palabra_invertida: 
        return True
    else:
        return False


#funcion principal
def run():
    frase = input("escribe una palabra o frase que sea palíndromo: ")
    es_palindromo = palindromo(frase)
    if es_palindromo == True:
        print("es palindromo")
    else: 
        print("no es palindromo")


#entry point:
#punto de entrada de un programa de python
#el programa hace la lectura del archivo y cuando llega a ésta funcion
#invoca la función principal
if __name__ == '__main__':
    run()




#######################################################
# NOTAS
# Slices: cortar en "revanadas" las cadenas de caracteres con los índices
# INDICES: [primer elem al que me refiero : elemento final al que me refiero : pasos en los que toma cada indice]

# Métodos: funciones especiales para un tipo de dato(objeto) en particular (objetos)
# ejemplos: 
### .upper() -> poner todo en mayus
### .capitalize() -> poner en mayuscula la primer letra
### .strip() -> elimina espacios basura al principio o al final de la palabra
### .lower() -> pone en minuscula todas las letras
### .replace("una letra", "letra a cambiar") -> elijo un caracter y lo reemplazo por otro caracter
