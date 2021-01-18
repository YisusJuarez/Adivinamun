# Algoritmo de procesamiento de numeor propuest
import time

def adivina_num(codigo):
    print ("Tienes que adivinar un numero de", 4, "cifras distintas") 
    inicio_de_tiempo = time.time()
    propuesta = input("¿Que codigo propones?: ")
    intentos = 1
    while propuesta != codigo:
        intentos = intentos + 1
        aciertos = 0
        coincidencias = 0

        # recorremos la propuesta y verificamos si es correcta
        for i in range(4):
            if propuesta[i] == codigo[i]:
                aciertos = aciertos + 1
            elif propuesta[i] in codigo:
                coinidencias = coincidencias + 1
        print ("Tu propuesta (", propuesta, ") tiene", aciertos, \
              "aciertos y ", coincidencias, "coincidencias.")
        # pedimos siguiente propuesta*
        propuesta = input("Propón otro codigo: ")
    tiempo_final = time.time()
    tiempo_total = tiempo_final - inicio_de_tiempo
    print ("Felicitaciones! Has adivinado el codigo en", intentos, "intentos.\nTomo %d segundos." % (tiempo_total))
    return tiempo_total
