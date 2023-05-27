# Funcion para obtener los compañeros: El de edad mayor va ser el profesor y el menor su asistente

# c:int es la cantidad de compañeros que asistieron
def get_colleagues(c:int):
    
    colleagues = [] # Lista de compañeros

    # Este ciclo se ejecuta segun la cantidad de compañeros asistieron; c es el parametro de la funcion
    for x in range(c): 

        name = input("¿Cual es el nombre? ") # nombre del compañero
        age = int(input("¿Cuantos años tiene? ")) # edad del comañero

        tuple_colleagues = (name, age) # Una tupla con el nombre y edad
        colleagues.append(tuple_colleagues) # Ingresamos la tupla a la lista
    
    # Ordenamos la lista segun la edad
    colleagues.sort(key=lambda x:x[1]) 

    # Retornamos el nombre del ultimo y el nombre del primero (compañeros)
    return colleagues[-1][0], colleagues[0][0] 




if __name__ == "__main__":
    # Desempaquetamos la funcion y se la asignamos a dos funciones el profesor y el asistente
    teacher, assitant = get_colleagues(2)
    # Imprimos por consola el resultado
    print(f"El profesor(a) es {teacher} y su asistente es {assitant}")