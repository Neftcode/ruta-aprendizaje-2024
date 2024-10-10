print("Programa que calcula si un número es par/impar\n")

# Método que SI recibe parámetros y SI retorna valor
def parImpar(numero):
    return numero%2==0
    
numeroIngresado = int(input("Ingrese un numero: "))

resultado = ("Es impar", "Es par")[parImpar(numeroIngresado)]

print(resultado)

print("\nFin del programa")