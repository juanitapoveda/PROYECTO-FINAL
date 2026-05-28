def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    
    if b == 0:
        return 'ERROR: b no puede ser 0'
    else:
        return a / b

def potencia(base, exponente):
    
    exponente = int(exponente)
    resultado = base # creamos la variable inicial del resultado
    if exponente == 0: # todo numero elevado a 0 es 1
        return 1
    elif exponente == 1: # todo numero elevado a 1 es igual a si mismo
        return base
    else:
        for i in range (1, exponente):
            resultado *= base
            
    return resultado
    
