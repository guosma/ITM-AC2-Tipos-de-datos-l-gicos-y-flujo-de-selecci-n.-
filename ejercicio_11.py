""" 11.Realizá un programa que permita ingresar un número entero e 
indique si se trata de un número par o impar. [EC] """

numero=int(input("Ingrese un numero => "))

if numero % 2 == 0:
    print("el numero ingresado es par")
else:
    print("el numero ingresado es inpar")
