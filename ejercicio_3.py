print(".: Limpieza de Nombres :.")
print()
nombres = [" juan", "María ", " peDro ", "aNa"]

lista_limpia = list(map(lambda x : x.strip(' '), nombres))
lista_limpia = list(map(lambda x : x.lower(), lista_limpia))
lista_limpia = list(map(lambda x : x.capitalize(), lista_limpia))

print(lista_limpia)