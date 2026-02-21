# Bubble Sort Normal vs Bubble Sort Otimizado (com contagem de passadas)

Este projeto em **Python** compara duas versões do algoritmo **Bubble Sort**:

- **Bubble Sort normal** (tradicional)
- **Bubble Sort otimizado** (melhoria que reduz comparações desnecessárias)

Além de ordenar, o programa também conta quantas **passadas** (comparações) cada versão fez.

🎥 Vídeo onde eu explico também:  
https://youtu.be/ym0mGl_z1DI

---

## 🔗 Outro repositório (Bubble Sort normal + vídeo)

Se você quiser ver a versão **normal** separada, com explicação em vídeo, está aqui:  
- Repositório: https://github.com/ChaMagalhaes/Bubble_sort  
- Vídeo: https://youtu.be/Z1LhmKNDWiQ

---

## ✅ O que o programa faz?

1. Pergunta quantos números você quer ordenar.
2. Lê os números digitados no terminal.
3. Executa:
   - Bubble Sort normal
   - Bubble Sort otimizado
4. Mostra:
   - Lista antes de ordenar
   - Lista ordenada por cada método
   - Quantidade de **passadas** (comparações) em cada um

---

## 🧠 O que são “passadas” aqui?

No seu código, `passadas` é incrementado a cada comparação entre dois elementos (ex.: `if array[i] > array[i+1]`).

Ou seja:
- **mais passadas = mais trabalho**
- **menos passadas = mais eficiente** (especialmente em listas quase ordenadas)

---

## 📌 Bubble Sort normal (tradicional)

### Como funciona
Ele percorre a lista várias vezes comparando elementos vizinhos e trocando quando necessário.  
Mesmo que a lista já esteja quase ordenada, ele continua fazendo muitas comparações.

### Características
- Faz sempre os mesmos loops (tende a trabalhar “a mais”).
- Complexidade típica: **O(n²)**

---

## 🚀 Bubble Sort otimizado (melhoria)

### Qual é a melhoria?
Ele **descobre até onde precisa comparar** com base na última troca feita.

- Se em uma passada a última troca aconteceu em certa posição,
  **depois disso já está tudo certo** (essa parte final já está ordenada).
- Então ele diminui o tamanho do trecho que ainda precisa ser analisado (`n = pos_ultima_troca`).

### Por que isso é melhor?
Em listas:
- **já ordenadas**
- **quase ordenadas**
- **com poucos elementos fora do lugar**

…essa versão pode reduzir MUITO a quantidade de comparações em alguns casos :D.

---

## 🧾 Código do projeto

```python
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
