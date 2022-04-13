""" 16.Realizá un programa que permita ingresar la cantidad de inscriptos a una conferencia
 y la cantidad de asientos disponibles en el auditorio. Debes indicar si alcanzan los asientos,
 Si los asientos no alcanzaran indicar cuántos faltan para que todos los inscriptos puedan sentarse.  """

personas_inscriptas = int(input("Ingresa la cantidad de personas que van a participar => "))
cantidad_sillas = int(input("Ingresa la cantidad de silla => "))

if personas_inscriptas > cantidad_sillas:
    sillas_faltante= personas_inscriptas - cantidad_sillas
    print(f"Faltan {sillas_faltante} sillas ")
else:
    print("los asientos son suficientes")
    sillas_sobrantes = cantidad_sillas - personas_inscriptas
    print(f"Sobran {sillas_sobrantes} sillas ")