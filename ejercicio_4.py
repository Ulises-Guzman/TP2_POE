print(".: Filtro de Inventario :.")
print()

productos = [
    {"nombre": "Resistencia", "stock": 50},
    {"nombre": "Capacitor", "stock": 5},
    {"nombre": "Diodo", "stock": 12},
    {"nombre": "Transistor", "stock": 8}
]

producto_filtrado = filter(lambda x: x["stock"] < 10, productos)
producto_reponer = list(producto_filtrado)

print("> Reponer Stock...")
print(producto_reponer)
