"""
14.Para entrar a la montaña rusa Infierno en las alturas se requiere:
tener al menos 7 años y medir más de 1,50 metros. 
Completá el siguiente cuadro a mano según los requisitos y luego haz el
programa que permita, según las edades y estaturas ingresadas por el usuario, obtener los
mismos resultados según los siguientes datos: [EC]

1) INPUT DE Nombre Edad Altura
2) OBTENER TRUE O FALSE
3) MOSTRAR RESULTADO
"""

nombre = input("ingrese el nombre")
edad = int(input("Ingrese la edad => "))
altura = float(input("Ingrese la Altura => "))

if edad >= 7 and altura > 1.50:
    print("Puede entrar a la montaña rusa Infierno en las alturas")
else:
    print("No cumple con los requicitos ")



















"""
Nombre Edad Altura ¿Entra al juego ?(V/F)
Juan    5   1.45
María   7   1.23
Luis    8   1.51
Ana     9   1.39

P   Q   (P and Q)
V   V       V
V   F       F   
F   V       F
F   F       F
"""