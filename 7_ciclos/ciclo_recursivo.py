# Programa que recibe un número natural del usuario y realiza cuenta regresiva hasta 0, mencionando en cada iteración si es número par o impar.
print("Programa que recibe un número del usuario y realiza cuenta regresiva hasta 0, mencionando en cada iteración si es número par o impar.\n")

def parImpar(num: int):
    """
    Función que recibe un número entero y calcula si es par o impar

    :param int num: número entero
    :returns bool: True/False
    """
    return num%2==0

def cuentaReg(num: int):
    """
    Función que recibe un número natural y muestra al usuario la cuenta regresiva hasta cero y menciona en cada iteración si el número es par o impar.
    
    :param int num: número natural desde donde se realizará la cuenta regresiva
    """
    for i in range(num, -1, -1):
        print(f"{i} es número {("impar", "par")[parImpar(i)]}.")

try:
    natural = int(input("Escribe un número natural (positivo): "))
except Exception as e:
    print(f"\nError: {e}.\nNo ingresaste un número natural.")
    exit()

if (natural>=0):
    cuentaReg(natural)
else:
    print("\nEl número no es natural.")