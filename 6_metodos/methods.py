import random

# Método que SI recibe parámetros y SI retorna valor
def parImpar(numero):
    return numero%2==0

# Método para crear un número aleatorio entre 0 y 1
def numeroRandom():
    return random.random()

# Método para capturar un valor al usuario
def getValue(txt):
    return input(txt)

# Método para parsear de str a int
def strToInt(str):
    return int(str)

# Método para parsear de str a float
def strToFloat(str):
    return float(str)