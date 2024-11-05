#a = [1, 2, 3]
#b = [1, 2, 3]
#print(a == b) 

#c = a
#print(a is c) 

#nr_bloques = 3
#nr_filas = 3

"""for i in range(3):
    for h in range(3):
        for j in range(3):
            print("*")
        print()
    print()"""

#lista = [1, 2, 3]
#lista.extend([5, 6, 7])
#print(lista);

# Diccionario original
mi_dict = {'a': 1, 'b': 2}

# Diccionario con el que queremos actualizar
otro_dict = {'b': 3, 'c': 4}

# Usamos el método update()
mi_dict.update(otro_dict)

print(mi_dict)
