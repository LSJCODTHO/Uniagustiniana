# # Bloque while
#
# password = '123456'
# intentos = 3
# contador = 0
#
# while contador < intentos:
#     clave = input('Ingrese su clave : ')
#     if clave == password:
#         print('Bienvenido')
#         break
#     else:
#         print('Clave incorrecta')
#     contador += 1
# else:
#     print('Ha superado el numero de intentos')
#
# print('**********Fin del Programa********')

# Funciones para realizar las operaciones
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: división por cero"
    return num1 / num2

# Diccionario que mapea las opciones a las funciones
operaciones = {
    1: ("Sumar", suma),
    2: ("Restar", resta),
    3: ("Multiplicar", multiplicacion),
    4: ("Dividir", division)
}

while True:
    print("""
    ******************* Bienvenido al menú CSC ****************
    Por favor elija una de las opciones relacionadas a continuación:

    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    0. Salir 
    """)

    opcion = int(input("Ingrese la opción del menú: "))

    if opcion == 0:
        print("************** Fin de la Aplicación ***********")
        break
    elif opcion in operaciones:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        nombre_operacion, funcion = operaciones[opcion]
        resultado = funcion(num1, num2)
        print(f"El resultado de {nombre_operacion} es: {resultado}")
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
