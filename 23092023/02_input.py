# Entrada por consola

numero_identificacion = int(input("Escriba su numero de identificacion : "))

nombre_empleado = str(input("Escriba su Nombre Completo : "))

# Entradas dinamicas

edad = int(input(f"Hola {nombre_empleado} identificion No {numero_identificacion}, ingrese su edad por favor : "))

if edad >= 18:
    print(f"{nombre_empleado} usted es Mayor de edad")
else:
    print(f"{nombre_empleado} Usted es Menor de Edad")
