lista = [1, 2, 3, 4, 5, 6]
lista2 = [1, 2, 3, 4, 3]
mitad = len(lista2) // 2
print(mitad)

guardar = lista2[0]
index = 0
negative = -1
encontrado = False

while encontrado == False:
    while index < mitad:
        print("positivo ", lista2[index])
        print("negativo ", lista2[negative])
        if lista2[index] == lista2[negative]:
            print("Valor encontrado", lista2[index])
            encontrado = True
            break
        if len(lista2) % 2 != 0:
            valor_medio = lista2[mitad]
            if lista2[index] == valor_medio or lista2[negative] == valor_medio:
                print("Valor encontrado", valor_medio)
                encontrado = True
                break
        index += 1
    else:
        if abs(negative) >= mitad:
            break
        negative -= 1
        index = 0