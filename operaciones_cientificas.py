PI = 3.14159265358979 # definimos la variable del numero pi

def factorial(n):
    # si se ingresa un numero negativo devolvemos None porque el factorial no esta definido
    if n < 0:
        return None
    # el factorial de 0 y 1 siempre es 1
    elif n == 0 or n == 1:
        return 1
    # inicializamos el resultado en 1, si iniciara en 0, cualquier multiplicación daría 0, los factoriales nunca se multiplican por 0
    resultado = 1

    # usamos el rango de 2 a n+1 porque la funcion range siempre se detiene un numero antes del limite final
    for i in range(2, n + 1):

    # "resultado = i" es un atajo para escribir "resultado = resultado i" toma el valor acumulado que tiene la variable 'resultado' lo multiplica por el nuevo número 'i' y guarda esa nueva respuesta dentro de la misma variable 'resultado'
        resultado *= i

    return resultado

def raiz_cuadrada(x, precision=0.00001):
    
    if x < 0: # no existen raices negativas
        print("No existe raíz cuadrada de un número negativo")
        return None
    if x == 0: # la raiz de 0 es cero
        return 0.0

    aproximacion = x # primer numero con el que empieza el algoritmo
    cambio = 1.0  # inicimos esta variable almacena las variaciones de cada ciclo

    while cambio > precision: # iniciamos un ciclo que itera hasta conseguir la aproximacion buscada
        nueva = (aproximacion + x / aproximacion) / 2 # aplicamos la forma de newton rhapson
        
        # calculamos la diferencia entre la aproximación anterior y la nueva
        cambio = nueva - aproximacion
        if cambio < 0:
            cambio = cambio * -1  # lo convertimos a positivo de forma manual
            
        aproximacion = nueva  # actualizamos la aproximación para la siguiente iteracion
        
    aproximacion = round(aproximacion, 4) # aproximamos 4 decimales

    return aproximacion


def exponencial(x, terminos=50):
    
    # empezamos con 0.0, para ir acumulando los trozos de la fórmula
    resultado = 0.0 
    
    # el ciclo nos da los números 0, 1, 2, 3... Estos números (n), representan en qué parte de la fórmula matemática vamos.
    for n in range(terminos):
        
        # numerador (x elevado a la n)
        numerador = x ** n
        
        # denominador (factorial de n)
        denominador = factorial(n)
        
        # se divide para obtener el valor de este trozo en particular
        termino_actual = numerador / denominador
        
        # Agregamos este pedacito al saco total resultado = resultado + termino_actual)
        resultado += termino_actual
        
    return resultado

def seno(x, terminos=10):  #definimos nuestra funcion seno que recibe de parametro un numero x en radianes
    
    resultado = 0  #empieza el resultado en 0, en este se van a ir sumando los terminos

    for i in range(terminos):   #vamos a repetir 10 veces el ciclo
        exponente = 2 * i + 1

        potencia = x ** exponente

        factorial = 1
        for j in range(1, exponente + 1):
            factorial *= j

        signo = (-1) ** i

        resultado += signo * potencia / factorial

    return resultado


def coseno(x, terminos=20):
    
    x = x % (2 * PI)
    resultado= 0 #se crea una variable donde se irá acumulando la suma


    for n in range(terminos): #se crea un ciclo for donde se repetira el calculo 20 veces, para más precisión
        f= 1 #aqui el factorial inicia en 1
        
        for i in range(1, (2 * n) + 1):  #creamos otro for donde se calcula el factorial de 2 como en la formula de coseno
            f *= i
       
        if n == 0:  #practicamente si n es igual a 0 el factorial será 1
            f= 1

        termino = ((-1) ** n) * (x ** (2 * n)) / f  #aqui se aplica la serie de Taylor para calcular cada termino
        resultado += termino  #se suma cada valor al resultado final

    return resultado  #se retorna el resultado

def logaritmo_natural(x, terminos=100):

    if x <= 0:
        return 'ln(x) no está definido para x <= 0' #la calculadora advierte al usuario que no debe poner un valor menor o igual a 0

    if x > 2:
        return 'ERROR esta aproximación solo es válida para 0 < x <= 2' #la serie de taylor solo funciona bien en valores cercanos a 1

    resultado= 0  #se crea la variable en donde se guardaran las sumas de la serie

    for n in range(1, terminos + 1): #creamos un ciclo for 
        t= ((-1) ** (n + 1)) * ((x - 1) ** n) / n 
        resultado += t  #aqui suma el termino calculado al resultado final

    return resultado  #se retorna el resultado