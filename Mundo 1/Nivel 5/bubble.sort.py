def bubbleSort(array):
    """
    Função para ordenar um array usando o algoritmo Bubble Sort.
    
    :param array: Lista de números a ser ordenada.
    """
    n = len(array);
    for i in range(n):
        # O último i elementos estão na posição correta
        for j in range(0, n - i - 1):
            # Comparar o elemento atual com o próximo
            if array[j] > array[j + 1]:
                # Trocar os elementos se estiverem na ordem errada
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;

# Declaração de um array de números com 15 posições
array_numeros = [34, 7, 23, 32, 5, 62, 45, 29, 8, 91, 4, 78, 11, 19, 3];

# Aplicar o método bubbleSort no array
bubbleSort(array_numeros);

# Imprimir o array ordenado
print("Array ordenado:");
print(array_numeros);
