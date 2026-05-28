# creamos una lista en donde se guarden todas las operaciones echas
lista_historial = []

def agregar_historial(texto): # creamos una funcion que guarde todas las operaciones realizadas
    lista_historial.append(texto)

def mostrar_historial(): # creamos una funcion para mostrar el historial
    if len(lista_historial) == 0: # si no hay nada en el historial se le dice al usuario
        print("No hay operaciones registradas aún.")
    else:
        # creamos un ciclo para enlistar el historial
        numero = 1 # lo iniciamos en 1
        for i in lista_historial: # vamos recorriendo toda la lista del historial mientras la enumeramos
            print(str(numero) + ". " + str(i))
            numero += 1 # vamos sumando de a 1 para que la numeracion aumente

def limpiar_historial(): # creamos una funcion para dejar el historial vacio
    lista_historial.clear()