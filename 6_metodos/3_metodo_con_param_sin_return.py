print("Programa que calcula si un número es par/impar\n")

# Método que SI recibe parámetros y NO retorna valor
def parImpar(numero):
    if (numero % 2 == 0):
        print("Es par")
    else:
        print("Es impar")

# Capturo el valor del usuario y parseo el valor a entero
numeroIngresado = int(input("Ingrese un numero: "))

parImpar(numeroIngresado)

print("\nFin del programa")