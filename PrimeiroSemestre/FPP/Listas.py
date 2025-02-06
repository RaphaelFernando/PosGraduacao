# Listas, são dados organizados em uma sequencias, 
# sendo esses dados atribuidos  a uma unica Variavel de mesmo nome.

lista = []

lista2 = [10, 20, 30]
# cada numero dentro dessa lista são chamados de elementos,
#  e  cada elemento esta definido em uma posição.

lista3 = [3.14, 999, "Teste"]

lista2.append(99)  #append esta inserindo um novo elemento a minha lista2, atribuindo o 99 como ultimo elemento.
print(lista2)

aux = lista2.pop() # aux esta removendo o ultimo elemento da minha lista
print(aux)

print(lista2)