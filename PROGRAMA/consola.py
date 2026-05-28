# importamos los archivos donde se encuentran nuestras funciones
import operaciones_basicas
import operaciones_cientificas
import graficadora
import historial

# definimos una funcion que inicie la calculadora
def ejecutar_calculadora():
    opcion = 0 # creamos la variable de opcion 
#creamos un ciclo para que el menu se muestre mientras la opcion no sea 7
    while opcion != "7": 
        print("\n" + "=" * 40)
        print("   CALCULADORA CIENTÍFICA GRAFICADORA")
        print("=" * 40)
        print("1. Operaciones básicas")
        print("2. Operaciones científicas")
        print("3. Evaluar función")
        print("4. Graficar función en consola")
        print("5. Ver historial de operaciones")
        print("6. Limpiar historial")
        print("7. Salir")
        print("=" * 40)

        opcion = input("Seleccione una opción: ").strip() # el usuario ingresa una opcion y se limpia de espacios con strip

        # MENU DE OPERACIONES BASICAS
        
        if opcion == "1": # si el usuario selecciona la opcion 1, se le mostrara el menu de las operaciones basicas
            print("\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Potencia") # se muestran las opciones dando saltos de linea con /n
            opc_basica = input("Seleccione una operación: ").strip()  # el usuario selecciona un opcion del menu de operaciones basicas y se limpian espacios
            
            if opc_basica in ["1", "2", "3", "4", "5"]: # si la opcion esta entre las 5 opciones entonces se le pedira a el usuario ingresar 2 numeros
                
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                
                if opc_basica == "1": # si la opcion es uno se llama a la funcion sumar y asi dependiendo de la eleccion del usuario
                    resultado = operaciones_basicas.sumar(a, b)
                    print("Resultado: " + str(resultado)) # se imprime el resultado 
                    historial.agregar_historial("Suma: " + str(a) + " + " + str(b) + " = " + str(resultado)) # se almacena la operacion en el historial
                
                elif opc_basica == "2":
                    resultado = operaciones_basicas.restar(a, b)
                    print("Resultado: " + str(resultado))
                    historial.agregar_historial("Resta: " + str(a) + " - " + str(b) + " = " + str(resultado))
                    
                elif opc_basica == "3":
                    resultado = operaciones_basicas.multiplicar(a, b)
                    print("Resultado: " + str(resultado))
                    historial.agregar_historial("multiplicar: " + str(a) + " * " + str(b) + " = " + str(resultado))
                    
                elif opc_basica == "4":
                    resultado = operaciones_basicas.dividir(a, b)
                    print("Resultado: " + str(resultado))
                    historial.agregar_historial("Division: " + str(a) + " / " + str(b) + " = " + str(resultado))
                
                elif opc_basica == "5":
                    resultado = operaciones_basicas.potencia(a, b)
                    print("Resultado: " + str(resultado))
                    historial.agregar_historial("Potencia: " + str(a) + " ** " + str(b) + " = " + str(resultado))

            else:
                print("Opción no válida.") # si se elige una opcion fura de la lista del 1 al 5, se imprime opcion no valida

        # MENU DE OPERACIONES CIENTIFICAS
        elif opcion == "2": # si la opcion elegida por el usuario es 2, entonces se desplega el menu de operaciones cientificas
            print("\n1. Factorial\n2. Raíz cuadrada\n3. Exponencial\n4. Seno\n5. Coseno\n6. Logaritmo")
            opc_cien = input("Seleccione una operación: ").strip() # se le pide al usuario ingresar una opcion y se limpian espacios
            
            if opc_cien == "1": # dependiendo de la opcion elegida por el usuario se opera la funcion
                n = int(input("Ingrese n: "))
                resultado = operaciones_cientificas.factorial(n) 
                print("Resultado: " + str(resultado))
                historial.agregar_historial("Factorial de " + str(n) + " = " + str(resultado)) # se agrega el resultado al historial
                
            elif opc_cien == "2": # dependiendo de la opcion elegida por el usuario se opera la funcion
                n = float(input("Ingrese n: "))
                resultado = operaciones_cientificas.raiz_cuadrada(n) 
                print("Resultado: " + str(resultado))
                historial.agregar_historial("Raíz cuadrada de " + str(n) + " = " + str(resultado)) # se agrega el resultado al historial
                
            elif opc_cien == "3": # dependiendo de la opcion elegida por el usuario se opera la funcion
                n = float(input("Ingrese n: "))
                resultado = operaciones_cientificas.exponencial(n) 
                print("Resultado: " + str(resultado))
                historial.agregar_historial("Exponencial de " + str(n) + " = " + str(resultado)) # se agrega el resultado al historial
                
            elif opc_cien == "4": # dependiendo de la opcion elegida por el usuario se opera la funcion
                n = float(input("Ingrese n: "))
                resultado = operaciones_cientificas.seno(n) 
                print("Resultado: " + str(resultado))
                msg = "Seno de " + str(n) + " = " + str(resultado)
                historial.agregar_historial(msg) # se agrega el resultado al historial

            elif opc_cien == "5": # dependiendo de la opcion elegida por el usuario se opera la funcion
                n = float(input("Ingrese n: "))
                resultado = operaciones_cientificas.coseno(n) 
                print("Resultado: " + str(resultado))
                historial.agregar_historial("Coseno de " + str(n) + " = " + str(resultado)) # se agrega el resultado al historial

            elif opc_cien == "6": # dependiendo de la opcion elegida por el usuario se opera la funcion
                n = float(input("Ingrese n: "))
                resultado = operaciones_cientificas.logaritmo_natural(n) 
                print("Resultado: " + str(resultado))
                historial.agregar_historial("Logaritmo de " + str(n) + " = " + str(resultado)) # se agrega el resultado al historial
                

        # EVALUAR FUNCIONES
        elif opcion == "3":
            nombre = input("Ingrese el nombre de la función (lineal/cuadratica/cubica): ").strip().lower()
            x = float(input("Ingrese el valor de x: "))
            
            resultado = graficadora.evaluar_funcion_matematica(nombre, x)
            if resultado is not None: # si es usuario ingreso bien los datos entonces se agrega al historial
                print("f(" + str(x) + ") = " + str(resultado))
                historial.agregar_historial("Evaluación: f(" + str(x) + ") de " + str(nombre) + " = " + str(resultado))
            else: # de lo contrario no se encuentra
                print("Función no encontrada.")

        # GRAFICADORA
        elif opcion == "4":
            nombre = input("Ingrese la función a graficar (lineal/cuadratica/cubica): ").strip().lower()
            if nombre in ["lineal", "cuadratica", "cubica"]: # buscar el nombre de la funcion escrita por el usuario
                graficadora.graficar(nombre)
                historial.agregar_historial('Grafica de funcion ' + nombre)
            else:
                print("Función no encontrada.")

        # MENU DEL HISTORIAL
        elif opcion == "5":
            print("\n--- HISTORIAL ---")
            historial.mostrar_historial() # mostrar el historial

        elif opcion == "6": 
            historial.limpiar_historial()
            print("Historial limpiado.")

        elif opcion == "7": # se cierra la calculadora
            print("Cierre de la calculadora")
            
        else: # si no se ingresa una opcion existente se envia como opcion invalida
            print("Opción inválida.")

ejecutar_calculadora()