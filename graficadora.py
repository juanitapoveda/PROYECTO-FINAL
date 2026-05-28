def evaluar_funcion_matematica(nombre_funcion, x):
    # definimos 3 funciones fijas para evaluar
    if nombre_funcion == "lineal": # f(x) 2x+1
        return 2 * x + 1
    elif nombre_funcion == "cuadratica": #f(x) x**2
        return x * x
    elif nombre_funcion == "cubica": # f(x) x ** 3
        return x * x * x
    else: # si no se selecciona ninguna de estas no se hace nada
        return None

def escalar(valor, val_min, val_max, nuevo_min, nuevo_max):
    # para graficar convertiremos el rango de la funcion en filas de la consola

    # Si todos los valores de Y son iguales, es decir que es constante, el programa siempre se quedara en la misma linea
    if val_max == val_min:
        return nuevo_min
    
    # aca vamos a escalar la funcion, usando una regla de 3, por lo que primero: 
    # Se dividen los rangos de la funcion para sacar su mitad
    # Se multiplica esa mitad por el rango de nuestras filas, asi sabremos que proporcionalmente cada asterisco se ubica ahi
    # despues se le sumara el minimo de nuestro rango, es decir su inicio para desplazarla
    return (valor - val_min) / (val_max - val_min) * (nuevo_max - nuevo_min) + nuevo_min


def graficar(nombre_funcion, x_min=-5, x_max=5, ancho=60, alto=20): # creamos la funcion donde definimos los valore sde x que se recorren, de ancho existen 60 columnas y de alto 20 filas.

    xs = []  # guardar los valores del eje x  (columnas)
    ys = []  # y guardar los resultados del eje y (altura)
    
    # calculamos cuánta distancia decimal debe haber entre cada una de las 60 columnas, es decir que valores de x nescesitamos exactamente para graficar nuestro rango
    # (x_max - x_min), corresponde al rango
    # (ancho - 1), corresponde al espacio que tenemos para graficar el rango
    paso_x = (x_max - x_min) / (ancho - 1)
    
    # creamos un ciclo que de una vuelta por cada columna de la pantalla, en este caso definimos 60
    for i in range(ancho):
        # calculamos el valor de x dependiendo de la columna en la que esta, al valor minimo se le suma el valor de la cuolumna y eso se multiplica por la distancia entre cada punto encontrada anteriormente
        x_actual = x_min + i * paso_x
        xs.append(x_actual)  # guardamos el valor encontrado en la lista de x
        
        # evaluamos la función matemática elegida y guardamos el resultado de Y
        resultado_y = evaluar_funcion_matematica(nombre_funcion, x_actual) # llamamos a la funcion
        ys.append(resultado_y) # se agregan los valores encontrados a la listas de y

# encontrar los valores mas bajos y altos de x, como el techo y el piso para adaptarlos a las filas
    # empezamos con el caso base de la lista
    y_min = ys[0]
    y_max = ys[0]
    
    # abrimos un ciclo para recorrer los resultados de Y buscando el valor más alto y el más bajo
    for y in ys:
        if y < y_min: 
            y_min = y  # piso al ser el valor minimp por graficar
        if y > y_max: 
            y_max = y  # techo al ser el valor maximo por graficar

# creamos un lugar para nuestra grafica
    hoja = []  
    
    # creamos un cliclo para crear los 20 renglones donde graficaremos
    for f in range(alto):
        fila = []  # creamos una lista vacia para las filas
        for c in range(ancho): # creamos otro ciclo para poder dejar los 60 espacios vacios de las columnas
            fila.append(" ")  # agregamos los 60 espacios " " 
        hoja.append(fila)   # Guardamos el renglón terminado en la hoja principal, es decir que agregamos en total 20 renglones a nuestra hoja

 # colocar los corazones para graficar pada punto
 
    # recorremos las 60 columnas de izquierda a derecha con un ciclo
    for i in range(ancho):
        # Convertimos el resultado matemático Y a una escala de filas entre 0 y 19
        fila_dibujada = escalar(ys[i], y_min, y_max, 0, alto - 1) # aca usamos el valor escalado anteriormente con cada una de las 60 columnas
        
        # aca volteamos los valores, ya que para la consola el techo es 0 y la fila 19 es el piso, por lo que volteamos los valores
        fila_volteada = (alto - 1) - int(fila_dibujada)
        
        # Si la coordenada calculada es válida, cambiamos el espacio por un asterisco
        if 0 <= fila_volteada < alto:
            hoja[fila_volteada][i] = "♥"  # el programa va hasta la hoja en blanco, selecciona la fila y en la columna en la que itere pone un corazon

    
    # Imprimimos el nombre de la funcion que se grafico
    print('Gráfica de f(x) =', nombre_funcion)
    
    # Recorremos cada uno de los 20 renglones de nuestra hoja
    for fila in hoja:
        # usamos join para unir cada una de las filas creadas sin que esten separadas
        print("".join(fila))
        
    # imporimimos un igual por cada columna que tenemos
    print("=" * ancho)