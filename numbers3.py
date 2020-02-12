list = ['green', 'red', 'blue']
# print(dir(list))

# Elemento appened | Agregar
# Elemento insert  | Inserta elementos determinados
# Elemento pop     | Elimina el ultimo objeto
# Elemento sort    | Ordena alfabeticamente
# Elemento count   | Contar
# list.extend(('violet', 'black', 'white', 'orange'))
# print(list)
print("Uso del elemento insert")
list.insert(1, 'violet')
print(list)
list.insert(len(list), 'violeeet')
print(list)
list.pop()
print(list)
print("Uso del elemento sort")
list.sort()
print(list)
print(list.index('violet'))