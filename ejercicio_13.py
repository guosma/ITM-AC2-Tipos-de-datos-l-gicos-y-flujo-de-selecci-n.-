"""13.Realizá un programa para ingresar tres números enteros e indique cuál de ellos es el mayor y su valor. [EC]"""

def mayor(numero1, numero2,numero3=0):
    
    if numero3 < numero1 > numero2:
        _mayor = numero1
    elif numero2 > numero3:
        _mayor = numero2
    else:
        _mayor = numero3
    return _mayor

def main():
    num1 = int(input('ingrese el premer numero => '))
    num2 = int(input('ingrese el segundo numero => '))
    num3 = int(input('ingrese el tercer numero => '))
    print(f"El numero mayor es => {mayor(num1, num2, num3)} ")

print("Calculemos cul es el numero mas grande...")
main()