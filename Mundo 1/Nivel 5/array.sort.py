import random

# Criação do array com 15 números inteiros aleatórios
array_numeros = [random.randint(1, 100) for _ in range(15)];

print("Array original:");
print(array_numeros);

# Ordenação crescente
array_numeros.sort();
print("\nArray ordenado de forma crescente:");
print(array_numeros);

# Ordenação decrescente
array_numeros.sort(reverse=True);
print("\nArray ordenado de forma decrescente:");
print(array_numeros);

# Criação do array de strings
array_strings = ["nome", "dataNascimento", "cpf", "rg", "endereco", "telefone", "email", "cep", "cidade", "estado", "pais", "profissao", "estadoCivil", "nacionalidade", "dataEmissao"]

print("\nArray original de strings:")
print(array_strings)

# Ordenação crescente
array_strings.sort()
print("\nArray de strings ordenado de forma crescente:")
print(array_strings)

# Ordenação decrescente
array_strings.sort(reverse=True)
print("\nArray de strings ordenado de forma decrescente:")
print(array_strings)
