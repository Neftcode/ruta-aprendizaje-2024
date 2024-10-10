print("Programa que calcula si un número es par/impar\n")

# Método que NO recibe parámetros y SI retorna valor
def parImpar():
    numeroIngresado = int(input("Ingrese un numero: "))
    if (numeroIngresado % 2 == 0):
        return "Es par"
    else:
        return "Es impar"

print(parImpar())

print("\nFin del programa")