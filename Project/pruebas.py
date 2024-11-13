lista = [1, 2, 3, 4, 5, 6]
lista2 = [1, 2, 3, 4, 5]
mitad = len(lista2) // 2
print(mitad)

guardar = lista2[0]

"""for i in range(len(lista2)):
    guardar = lista2[i]
    for h in range(len(lista2)):
        if guardar  == lista2[i]:
            print(guardar)
        else:
            print("Valor no encontrado")"""
index = 0
negative = -1
encontrado = False

while encontrado == False:
    if index < mitad:
        for index in range(mitad):
            if lista2[index] == lista2[negative]:
                print("Valor encontrado", lista2[index])
                encontrado = True
                break
        else:
            negative = -1
            index += 1