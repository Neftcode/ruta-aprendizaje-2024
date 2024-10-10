print("Programa que calcula si un número es par/impar\n")

# Método que NO recibe parámetros y NO retorna valor
def parImpar():
    numeroIngresado = int(input("Ingrese un numero: "))
    if (numeroIngresado % 2 == 0):
        print("Es par")
    else:
        print("Es impar")

parImpar()

print("\nFin del programa")