# Programa que calcular el factorial de un número 
def factorial(numero):
    if (numero==1):
        return 1
    
    return numero*factorial(numero-1)

n = 5
restultado = factorial(n)
print(f"El factorial de {n} es: {restultado}")