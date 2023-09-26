# For
import random

saludo = 'hola'
for char in saludo:
    print(char)

# For Numero
for i in str(random.randrange(0, 100)):
    print(i)

# For Range
for i in range(10):
    print(i)

# Validación de credenciales
max_intentos = 3
password = 'hola'
for ciclo in range(max_intentos):
    pw = input('Ingresa la contraseña : ')
    if pw == password:
        print('Lo Lograste')
        break
    else:
        print('siga intentando')
else:
    print('Acceso Bloqueado')
