#ADIVINA EL NÚMERO
# modulo que va a permitir elegir numeros aleatoriamente
import random
import adivina

def gen_num():
    # Numeros válidos para generar el aleatrorio
    digitos = ('0','1','2','3','4','5','6','7','8','9')
    # Generación de código aleatorio
    codigo = ''
    for i in range(4):
        candidato = random.choice(digitos)
        # sin numeros repetidos*
        while candidato in codigo:
            print('DEBUG: candidato =', candidato)
            candidato = random.choice(digitos)
        codigo = codigo + candidato
        print('Debug: Números correctos:', codigo)
    return codigo

# INCIO DEL PROGRAMA
print ("Bienvenido/a a AdivinaElNumero Competivivo!")
print("Turno del jugador 1")
nombre1 = input("Teclea tu nombre:")
jugador1 = adivina.adivina_num(gen_num(), nombre1)
print("Turno del Jugador 2")
nombre2 = input("Teclea tu nombre:")
jugador2 = adivina.adivina_num(gen_num(), nombre2)
