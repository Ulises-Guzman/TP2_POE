print(".: Cálculo automático de IVA :.")
print()
precio = int(input("Ingrese el precio: $"))
print()

precio_iva = lambda precio : precio + ((21 * precio)/100)

print(f"> El precio + IVA es: ${precio_iva(precio)}")