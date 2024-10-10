# Programa que cuenta los números del 1 al 10. Cuando llegue a 10, sale a buscar.
print("1. Programa que cuenta los números del 1 al 10. Cuando llegue a 10, sale a buscar.\n")

for i in range(1, 11, 1):
    print(i)
    if (i==10):
        print("¡SALGO A BUSCAR YA!")

# Programa que determina y muestra si un número es par o impar en el rango de 0 a 100.
print("2. Programa que determina y muestra si un número es par o impar en el rango de 0 a 100.\n")

for x in range(1, 101, 1):
    if (x%2 == 0):
        print(f"{x}: El numero es par")
    else:
        print(f"{x}: El numero es impar")