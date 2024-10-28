import math

Opcion = int(input("""Elige un ejercicio(1 al 6): Ejercicio 1: Dadas dos variables numéricas A y B, que el usuario debe
teclear, se pide realizar un programa que intercambie los valores de ambas
variables y muestre cuánto valen al final las dos variables (recuerda
la asignación).
Ejercicio 2: Programa que lea dos números, calculando y escribiendo el valor
de su suma, resta, producto y división.
Ejercicio 3: Programa que lea dos números y nos diga cuál de ellos es mayor
o bien si son iguales (recuerda usar la estructura condicional SI)
Ejercicio 4: Programa que lea tres números distintos y nos diga cuál de ellos
es el mayor (recuerda usar la estructura condicional Si y los operadores
lógicos).
Ejercicio 5: Diseñar un programa que pida por teclado tres números; si el
primero es negativo, debe imprimir el producto de los tres y si no lo es,
imprimirá la suma.
Ejercicio 6: Realizar un programa que lea un número por teclado. En caso de
que ese número sea 0 o menor que 0, se saldrá del programa imprimiendo
antes un mensaje de error. Si es mayor que 0, se deberá calcular su cuadrado
y la raíz cuadrada del mismo, visualizando el número que ha tecleado el
usuario y su resultado (“Del número X, su potencia es X y su raíz X” ). Para
calcular la raíz cuadrada se puede usar la función del paquete math sqr(X) o
con una potencia de 0,5."""))

match Opcion:
    case 1:
        #Ejercicio1
        A=int(input("Pon el valor de A"))
        B=int(input("Pon el valor de B"))
        # Intercambio de valores
        A, B = B, A

        # Mostrar los valores intercambiados
        print(f"Después del intercambio: A = {A}, B = {B}")
    case 2:
        #Ejercicio2
        A=int(input("Pon el valor de A"))
        B=int(input("Pon el valor de B"))
        suma = A+B
        resta = A-B
        multiplicar = A*B

        if A==0 or B==0:
            print("Uno de los dos numeros es igual a 0")
            division=0
        else:
            division = A/B

        print("suma:", suma, "resta:", resta," multiplicar:", multiplicar," division:", division)

    case 3:
        #Ejercicio3
        A=int(input("Pon el valor de A"))
        B=int(input("Pon el valor de B"))
        if A==B:
            print("Son iguales")
        else:
            if A>B:
                print("A es mayor a B")
            else:
                print("B es mayor que A")
    case 4:
        #Ejercicio4
        A=int(input("Pon el valor de A"))
        B=int(input("Pon el valor de B"))
        C=int(input("Pon el valor de C"))

        if C>A and C>B:
            print("C es el numero mas grande")
        else:
            if B>A and B>C:
                print("B es el numero grande")
            else:
                print("A es el numero mas grande")
    case 5:
        #Ejercicio5
        print("Ejercicio 5")
        D=int(input("Pon el valor de D"))
        E=int(input("Pon el valor de E"))
        F=int(input("Pon el valor de F"))

        if D<0:
            ej15=D*E*F
            print(ej15)
        else:
            ej25=D+E+F
            print(ej25)
    case 6:
        # Ejercicio 6
        A = int(input("Pon el valor de A: "))
        if A <= 0:
            print("error")
        else:
            # Calcular la potencia y la raíz cuadrada
            potencia = math.pow(A, 0.5)  # Elevar al cuadrado
            raiz = math.sqrt(A)        # Raíz cuadrada
            print(f"Del número {A}, su potencia es {potencia} y su raíz es {raiz}")
    case _:
        print("No has escrito una opción correcta")







