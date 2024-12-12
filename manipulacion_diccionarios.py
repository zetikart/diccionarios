diccionario = {'ip': '192.168.1.1', 'port': 8080, 'state': 'open'}

print("=============================")
print("estado principal de nuestro diccionario: ")
print(diccionario)

print("=============================")
print("borramos el estado del puerto")
del diccionario['state']
print(diccionario)

print("=============================")
print("borramos el contenido del diccionario")
diccionario.clear()
print(diccionario)
