# Aprender como capturar valores, parsear y diferentes métodos de impresión.

# Declarar variable según el usuario.
# Para capturar un valor en consola, se utiliza
# el método input()
num_1_capturado = input("Número 1: ")
num_2_capturado = input("Número 2: ")

# Convertir un tipo de dato a otro (String -> Int)
# Para convertir (parsear) una cadena en número, se utiliza
# el método int()
num_1_parseado = int(num_1_capturado)
num_2_parseado = int(num_2_capturado)

# Declaro una tercer variable y le almaceno
# el valor de la sumatoria
resultado = num_1_parseado + num_2_parseado
# Imprimir una cadena
print("El resultado de la sumatoria es:")
# Imprimir un número
print(resultado)
# Imprimir una concatenación: método 1
print(f"Método 1: El resultado de la sumatoria entre {num_1_parseado} y {num_2_parseado} es: {resultado}.")
# Imprimir una concatenación: método 2
print("Método 2: El resultado de la sumatoria entre",num_1_parseado,"y",num_2_parseado,"es:",resultado,".")
# Imprimir una concatenación: método 3
print("Método 3: El resultado de la sumatoria entre " + str(num_1_parseado) + " y " + str(num_2_parseado) + " es: " + str(resultado) + ".")

print("Hola {num_1_parseado}, {num_2_parseado}".format("/d", "/b"))