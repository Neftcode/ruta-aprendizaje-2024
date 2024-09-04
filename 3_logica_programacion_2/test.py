edad = int(input("Ingrese su edad (recomendado 16): "))

# Ejemplo de operador lógico mayor que (>)
print("\nEjemplo de operador lógico mayor que (>):")
print(f"{edad}>18: {edad>18}")
print(f"{edad}>16: {edad>16}")
print(f"{edad}>10: {edad>10}")

# Ejemplo de operador lógico menor que (<)
print("\nEjemplo de operador lógico menor que (<):")
print(f"{edad}<18: {edad<18}")
print(f"{edad}<16: {edad<16}")
print(f"{edad}<10: {edad<10}")

# Ejemplo de operador lógico Mayor o igual que (>=)
print("\nEjemplo de operador lógico Mayor o igual que (>=):")
print(f"{edad}>=18: {edad>=18}")
print(f"{edad}>=16: {edad>=16}")
print(f"{edad}>=10: {edad>=10}")

# Ejemplo de operador lógico Menor o igual que (<=)
print("\nEjemplo de operador lógico Menor o igual que (<=):")
print(f"{edad}<=18: {edad<=18}")
print(f"{edad}<=16: {edad<=16}")
print(f"{edad}<=10: {edad<=10}")

# Ejemplo de operador lógico Es Igual (==)
print("\nEjemplo de operador lógico Es Igual (==):")
print(f"{edad}==16: {edad==16}")
print(f"{edad}==20: {edad==20}")

# Ejemplo de operador lógico Distinto/Diferente (!=)
print("\nEjemplo de operador lógico Distinto/Diferente (!=):")
print(f"{edad}!=16: {edad!=16}")
print(f"{edad}!=20: {edad!=20}")

# Ejemplo de operador lógico Negación/Operador No (! not)
print("\nEjemplo de operador lógico Negación/Operador No (! not):")
respuesta = edad>=16
print(f"respuesta = {edad}>=16")
print(f"respuesta = {respuesta}")
print(f"not respuesta = {not respuesta}")

# Ejemplo de operador lógico Y (&& and)
print("\nEjemplo de operador lógico Y (&& and):")
#edad = 20
genero = 'M'
vive = "Chaguaní"

print(f"edad = {edad}")
print(f"genero = '{genero}'")
print(f"vive = \"{vive}\"")

resultado = (edad==16) and (genero=='M') and (vive=="Chaguaní")
print(f"resultado = ({edad}==16) and ('{genero}'=='M') and (\"{vive}\"==\"Chaguaní\")")
print(f"resultado = {resultado}")

# Ejemplo de operador lógico O (|| or)
print("\nEjemplo de operador lógico O (|| or):")
#edad = 20
genero = 'F'
vive = "Bogotá"

print(f"edad = {edad}")
print(f"genero = '{genero}'")
print(f"vive = \"{vive}\"")

resultado = edad==20 or genero=='F' or vive=='Bogotá'
print(f"resultado = {edad}==20 and '{genero}'=='F' and \"{vive}\"==\"Bogotá\"")
print(f"resultado = {resultado}")

# Ejemplo de una condicional
print("\nEjemplo de una condicional:")

"""
if ("realizo una pregunta o validación"):
    # aquí ejecuto la acción por ser verdadero
else:
    # aquí ejecuto la acción por ser falso
"""

"""
if ("¿está lloviendo?"):
    print("Plan ver película")
else:
    print("Salgo al parque")
"""

print(f"if ({edad}<18):")
print("    Es menor de edad")
print("else:")
print("    Es mayor de edad")

print("\nResultado:")

if (edad<18):
    print("Es menor de edad")
else:
    print("Es mayor de edad")
