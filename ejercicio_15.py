""" 15.Para entrar a la montaña rusa Miedo a las alturas, algo más chica y tranquila que la anterior,
alcanza con que se cumpla solamente una de las siguientes condiciones: ser mayor de 6 años o medir más de 1,50 metros. 
Realizá el mismo procedimiento que con el ejercicio anterior pero con los nuevos requisitos. [EC]  """




nombre = input("ingrese el nombre")
edad = int(input("Ingrese la edad => "))
altura = float(input("Ingrese la Altura => "))

if edad > 6 or altura > 1.50:
    print("Puede entrar a la montaña rusa Infierno en las alturas")
else:
    print("No cumple con los requicitos ")