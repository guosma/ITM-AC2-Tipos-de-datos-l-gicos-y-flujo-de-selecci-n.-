"""17.Realizá un programa que permita ingresar una edad (entre 1 y 120 años) y un género 
('F' para mujeres, 'M' para hombres). En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido),
 informar tal situación. Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan
 con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse."""




edad = int(input("ingrese una edad => "))
genero = input("""
Ingrese sigun corresponda 
"F" para mujer 
      o 
"M" para hombre
=> """ ).upper()
datos_correctos = False
GENEROS = ["F", "M"]
EDAD_MUJER_JUBILARSE = 60
EDAD_HOMBRE_JUBILARSE = 65

while not datos_correctos:
    if 1< edad < 120 and genero in GENEROS:
        datos_correctos = True
    else:
        print("Los datos son incorrectos Vuelva a igresarlos")

        edad = int(input("ingrese una edad => "))
        genero = input("""
        Ingrese sigun corresponda 
        "F" para mujer 
            o 
        "M" para hombre
        => 
        """ ).upper()

if genero == GENEROS[0] and edad >= EDAD_MUJER_JUBILARSE:
    print("esta en edad de juvilarse ")
elif genero == GENEROS[1] and edad >= EDAD_HOMBRE_JUBILARSE:
    print("esta en edad de juvilarse ")
else:
    print(" NO esta en edad de juvilarse ")


 


