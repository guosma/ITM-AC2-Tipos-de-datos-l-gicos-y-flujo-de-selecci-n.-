""" 12.Realizá un programa que permita ingresar dos números enteros 
e indique cuál de ellos es el mayor. [EC]  """

""" numeros=[]

for i in range(2):
    numero=int(input("Ingrese un numero entero => "))
    numeros.append(numero)

print(max(numeros)) """

def mayor(numero1, numero2):
    
    if numero1 > numero2:
        _mayor = numero1
    else:
        _mayor = numero2
    return _mayor

def main():
    num1 = int(input('ingrese el premer numero => '))
    num2 = int(input('ingrese el segundo numero => '))
    print(f"El numero mayor es => {mayor(num1, num2)} ")

print("Calculemos cul es el numero mas grande...")
main()