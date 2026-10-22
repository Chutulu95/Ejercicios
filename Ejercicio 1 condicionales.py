# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

altura = int(input("Ingrese su altura sin puntos para determinar su posicion: "))

if 130 <= altura <= 220:
    if altura <= 160:
        print("Tu posicion es Base, ¡felicidades!")   
    elif 160 <= altura <= 179:
        print("Tu posicion es Escolta, ¡felicidades!")
    elif 179 <= altura <= 199:
        print("Tu posicion es Alero, ¡felicidades!")
    elif altura >= 200:
        print("Tu posicion es Ala-Pívot o Pívot, ¡felicidades!")
else:
     print("Pone una altura real para jugar baloncesto, intenta otra vez o busca otro deporte")
               