print(".: Verificador de Mayúsculas Capital de letra P :.")
print()

palabra = input("Ingrese una palabra: ")

verificacion = lambda palabra : palabra.startswith("P")
print(verificacion(palabra))