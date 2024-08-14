def selectionSort(array):
    """
    Função para ordenar um array usando o algoritmo Selection Sort.
    
    :param array: Lista de números a ser ordenada.
    """
    n = len(array);
    for i in range(n):
        # Assume que o elemento atual é o menor
        min_index = i;
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j;
        # Trocar o menor elemento encontrado com o elemento na posição i
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i];

# Declaração e inicialização do array com 15 números inteiros
array_numeros = [29, 10, 14, 37, 13, 21, 25, 45, 9, 31, 22, 19, 44, 30, 27];

print("Array original:");
print(array_numeros);

# Aplicar o método selectionSort no array
selectionSort(array_numeros);

# Imprimir o array ordenado
print("\nArray ordenado:");
print(array_numeros);
