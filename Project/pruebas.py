lista = [1, 2, 3, 4, 5, 6]
lista2 = [1, 2, 3, 4, 5]

guardar = lista2[0]

"""for i in range(len(lista2)):
    guardar = lista2[i]
    for h in range(len(lista2)):
        if guardar  == lista2[i]:
            print(guardar)
        else:
            print("Valor no encontrado")"""
index = 0

while True:
    if lista2[index] == lista2[-(index + 1)]:
        print("Valor encontrado ", lista2[index])
        break
    else:
        index += 1