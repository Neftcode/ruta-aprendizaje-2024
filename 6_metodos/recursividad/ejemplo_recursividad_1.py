def imprimir(algo):
    print(algo)

def suma(a,b,contador):
    if (contador==3):
        return
    c = a+b
    txt = f"La suma de {a}+{b}={c}"
    imprimir(txt)
    suma(c,a,contador+1)

print("Antes de entrar al ciclo\n")
suma(4, 7, 0)
print("\nAcabo de salir del ciclo")