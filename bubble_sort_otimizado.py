def bubble_sort(array):
    array = array[:]
    passadas = 0
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            passadas += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return passadas, array


def bubble_sort_otimizado(array):
    array = array[:]
    passadas = 0
    n = len(array)

    while n > 1:
        pos_ultima_troca = 0

        for i in range(n - 1):
            passadas += 1
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                pos_ultima_troca = i + 1

        n = pos_ultima_troca

    return passadas, array


n = int(input("Quantos números você quer ordenar? \n>>> "))

numeros = []
for i in range(n):
    numero = int(input(f"Digite o {i+1}º número: \n>>> "))
    numeros.append(numero)

passadas_normal, ordenado_normal = bubble_sort(numeros)
passadas_otim, ordenado_otim = bubble_sort_otimizado(numeros)

print("ANTES DE ORDENAR:", numeros)
print(f"DEPOIS BUBBLE SORT NORMAL:    {ordenado_normal} | PASSADAS = {passadas_normal}")
print(f"DEPOIS BUBBLE SORT OTIMIZADO: {ordenado_otim} | PASSADAS = {passadas_otim}")
