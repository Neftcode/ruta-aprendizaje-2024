# Programa que tira una moneda y si el usuario acierta gana algo
from methods import numeroRandom, getValue, strToInt

eleccion_usuario = strToInt(getValue("Elija 1 para cara o 2 para sello: "))

numRand = numeroRandom()
print(numRand)
if (numRand<0.5):
    print("Cayó cara")
    if (eleccion_usuario==1):
        print("GANASTE")
    else:
        print("PERDISTE")
else:
    print("Cayó sello")
    if (eleccion_usuario==2):
        print("GANASTE")
    else:
        print("PERDISTE")
