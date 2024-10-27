#importar libreria "time" y declarar variables :D

import time
nombre=input("tu nombre: ")
print("hola, "+nombre," adivina")
print(" ")
time.sleep(1)
print("comienza a adivinar")
time.sleep(0.5)
palabra="PYTHON"
tupalabra=" "
vidas=5

#Ciclo while y ciclo for 

while vidas > 0:
    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("*",end="")
            fallas+=1
    if fallas==0:
        input()
        print("")
        print("ganaste")
        input()
        break

    tuletra=input("introduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("NO, TE EQUIVOCASTE")
        print("tu tienes ",+vidas," vidas")
    if vidas== 0:
        print("perdiste")
else:
    input()
    print("Felicidades! JAJAJA")
    input()

#Proyecto 2, un proyecto bastante simple para practicar el uso de los ciclos "for" y "while"
#Era necesaria la libreria time para que fuese mas sencilla de entender la sintaxis, asi que, antes de empezar a escribir busqué informacion sobre si era necesario usar alguna libreria para este codigo.