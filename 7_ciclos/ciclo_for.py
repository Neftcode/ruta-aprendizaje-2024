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
        print(f"{x}: El número es par")
    else:
        print(f"{x}: El número es impar")

# Programa que separa un texto según el patrón dado y cuenta el número de oraciones e imprime cada una
print("Programa que separa un texto según el patrón dado y cuenta el número de oraciones e imprime cada una")
cadena = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas \"Letraset\", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum."
# print(cadena)
vector_de_oracion = cadena.split('.')

print(f"Total de oraciones: {len(vector_de_oracion)}")

cont = 1
for oracion in vector_de_oracion:
    print(f"{cont}. {oracion}")
    cont+=1
