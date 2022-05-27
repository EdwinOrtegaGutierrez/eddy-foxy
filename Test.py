myList = [3, 1, 4, 6, 2, 5]

def listNumberUp(publicList):
    numeroMayor = 0
    # ECONTRAR EL MAYOR
    for i in range(len(publicList)):
        if publicList[i] > numeroMayor:
            numeroMayor = publicList[i]
    return str(numeroMayor)

print(f'El número mayor de la lista {myList} es {listNumberUp(myList)}\n')

def listNumberDown(publicList):
    numeroMayor = 0
    # ECONTRAR EL MAYOR
    for i in range(len(publicList)):
        if publicList[i] > numeroMayor:
            numeroMayor = publicList[i]
    numeroMenor = numeroMayor
    # ENCONTRAR EL MENOR
    for i in range(len(publicList)):
        if myList[i] < numeroMenor:
            numeroMenor = publicList[i]
    return str(numeroMenor)
        
print(f'El número menor de la lista {myList} es {listNumberDown(myList)}\n')

def sumPositive(publicList):
    aux = 0
    # ENCONTRAR LA SUMA TOTAL
    for i in range(len(publicList)):
        aux += publicList[i]
    return str(aux)
    
print(f'Suma de positivos: {sumPositive(myList)}\n')

def sumNegative(publicList):
    aux = 0
    # ENCONTRAR LA RESTA TOTAL
    for i in range(len(publicList)):
        aux -= publicList[i]
    return str(aux)
print(f'Suma de negativos: {sumNegative(myList)}\n')

def mult(publicList):
    aux = 1 # EL AUXILIAR ES IGUALADO A 1 PORQUE SI SE MULTIPLICA POR 0 SIEMPRE DARA 0
    # ENCONTRAR LA MULTIPLICACION TOTAL
    for i in range(len(publicList)):
        aux *= publicList[i]
    return str(aux)

print(f'La multiplicación total es {mult(myList)}\n')

def div(publicList):
    # ENCONTRAR LA DIVISION TOTAL
    for i in range(len(publicList)):
        if i == 0:
            aux = publicList[i]
        elif i > 0:   
            aux /= publicList[i]
    return str(aux)

print(f'La división total es {div(myList)}\n')

def listDown(publicList):
    # ORDENAR LA LISTA DEL MENOR AL MAYOR
    for i in range(len(publicList)):
        for j in range(len(publicList)):
            a = j + 1
            if j == 0:
                if publicList[j] > publicList[a]:
                    publicList[j], publicList[a] = publicList[a], publicList[j]
            if a != len(publicList):
                if publicList[j] > publicList[a]:
                    publicList[j], publicList[a] = publicList[a], publicList[j]
    return str(publicList)
                    
print(f'Lista ordenada del menor al mayor: {listDown(myList)}\n')

def listUp(publicList):
    # ORDENAR LA LISTA DEL MAYOR AL MENOR
    for i in range(len(publicList)):
        for j in range(len(publicList)):
            a = j + 1
            if j == 0:
                if publicList[j] < publicList[a]:
                    publicList[j], publicList[a] = publicList[a], publicList[j]
            if a != len(publicList):
                if publicList[j] < publicList[a]:
                    publicList[j], publicList[a] = publicList[a], publicList[j]
    return str(publicList)
                
print(f'Lista ordenada del mayor al menor: {listUp(myList)}\n')

input('Presiona alguna tecla para continuar...')
