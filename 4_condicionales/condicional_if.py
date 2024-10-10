# Programa que determina la clasificación de la una nota utilizando el condicional IF
print("--- Programa que determina la clasificación de la una nota utilizando el condicional IF ---\n")
nota = float(input("Ingrese su nota entre 1.0 y 5.0 incluyente: "))

# Validar si la nota ingresada está entre 1.0 y 5.0 incluyente
if ( (nota < 1.0) or (nota > 5.0) ):
    print("Error")
else:
    if (nota >= 3.3):
        print("APROBÓ")
    else:
        print("REPROBÓ")

    # Condicional if concatenado o extendido
    """
    Clasificación de notas:
    1.0 - 2.0 -> "Muy mal"
    2.1 - 3.2 -> "Mal"
    3.3 - 3.9 -> "Regular"
    4.0 - 4.5 -> "Sobresaliente"
    4.6 - 5.0 -> "Excelente"
    """

    if (nota>=1.0 and nota<=2):
        print("Muy mal")
    elif (nota>=2.1 and nota<=3.2):
        print("Mal")
    elif (nota>=3.3 and nota<=3.9):
        print("Regular")
    elif (nota>=4.0 and nota <=4.5):
        print("Sobresaliente")
    else:
        print("Excelente")

print("\n\nFin del programa.")