####### ESTRUCTURA DE DATOS #######
#   LISTA  es una entructura de datos dentro de un objeto (variable) - son dinámicas ->consume memoria
#   puede contener elementos del mismo tipo o de distintos tipos
#   >>> accedo a los elementos con los indices
#   >>> puedo usar METODOS:
#       mi_lista.append(lo que agrego) -> para agregar un elemento en la siguiente posicion al ultimo
#       mi_lista.pop(indice del elem que quiero eliminar) -> elimino un elemento de la lista
#   >>> recorrer elementos de las listas con for
#       for elemento in objetos: ***desde el primer elem hasta el ultimo de la lista***
#           print(elemento)   
#   >>> puedo utilizar los slices (mi_lista[0:3:-1])

####### TUPLAS #######
#   Es un tipo de objeto similar a las LISTAS pero estático (es INMUTABLE)
#   no se pueden agregar ni quitar elementos   
#   >>>los trabajamos igual que las listas, pero en parentesis
#       una_tupla = (1,3,4,5)

####### DICCIONARIOS ####### 
#   los datos se encierran entre llaves
#   es una estructura de datos de LLAVES (nombre del key) y VALORES
#   >>> no accedo a traves del índice, sino a traves de las llaves -> el nombre de su "indice", el lugar que contiene un elemento
#       cada elemento se delimita por comas    
#   >>> puedo recorrer el diccionario:
#       -->metodo .keys() del diccionario: para devolver las llaves utilizadas
#           for unTipo in nombre_del_diccionario.keys() 
#               print(unTipo)
#       -->metodo .value() del diccionario: para devolver el valor que guardan las llaves
#           for unTipo in nombre_del_diccionario.value()
#               print(pais)
#       -->metodo .item() del diccionario: para devolver el nombre de la llave + el valor de la llave
#           for unTipo, otroTipo in nombre_del_diccionario.item()
#               print(unTipo + otroTipo) <-- todo tiene que ir como string

def run ():
    print("##### PRIMERA PRUEBA #####")
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }

    print("vamos a mostrar el contenido con 3 print:")
    print("elemento llave1: "+ str(mi_diccionario["llave1"]))
    print("elemento llave2: "+ str(mi_diccionario["llave2"]))
    print("elemento llave3: "+ str(mi_diccionario["llave3"]))

    print("\nacá vamos a usar un for para mostrar los items")
    for nombre, valor in mi_diccionario.items():
        print("en la llave " + nombre + " encontramos el valor: " + str(valor))


    print("\n\n##### SEGUNDA PRUEBA #####\n")
    familia_nakasone = {
        "Marcelo": ["febrero", 18, 66],
        "Mercedes": ["marzo", 7, 65],
        "Julieta": ["noviembre", 12, 93],
        "Eliana": ["marzo", 26, 96],
        "Keiko": ["febrero", 27, 98],
        "Keisuke": ["mayo", 6, 2003],
    }

    print("qué personas componen el objeto familia_nakasone:")
    for persona in familia_nakasone.keys():
        print(persona)

    print("\nqué mes, día y año de nacimiento tiene cada persona de familia_nakasone")
    for mes, dia, anio in familia_nakasone.values():
        print(str(dia) + "/" + mes + "/" + str(anio))

    print("\nla info dentro de familia_nakasone") #esta parte no anda :(
    print("****este no anda :( ****")
    #for persona, mes, dia, anio in familia_nakasone.items():
       # print(persona + ":" + mes + " de " + str(dia) + " del " + str(anio))
    #for persona in familia_nakasone.keys():
        #for mes, dia, anio in familia_nakasone.values():
            #print("la fecha de nacimiento de " + persona + " es "
                #+ str(dia) + " de " + mes + " del " + str(anio))

if __name__ == "__main__":
    run()
