
import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

while True:
    try:
        longitud = int(input("Introduce la longitud de la contraseña: "))
        if 3 <= longitud <= 40:
            print("Contraseña generada:", generar_contraseña(longitud))
        else:
            print("ELIJA UNA CONTRASEÑA DE 40 CARACTERES COMO MÁXIMO Y 3 COMO MÍNIMO")
    except ValueError:
        print("Por favor, elija la cantidad de números que desea.")
