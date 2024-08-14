# Abre o arquivo e lê o conteúdo
arquivo = open('loremipsum.txt', 'r')
conteudo = arquivo.read()

# Imprime todo o conteúdo do arquivo
print("Conteúdo do arquivo:")
print(conteudo)

# Imprime apenas a primeira linha do arquivo
arquivo.seek(0)  # Volta ao início do arquivo
primeira_linha = arquivo.readline().strip()
print("\nPrimeira linha do arquivo:")
print(primeira_linha)

# Imprime apenas os 3 primeiros caracteres do arquivo
arquivo.seek(0)  # Volta ao início do arquivo
primeiros_caracteres = conteudo[:3]
print("\nOs 3 primeiros caracteres do arquivo:")
print(primeiros_caracteres)

# Fecha o arquivo
arquivo.close()

# Utiliza a instrução `with` para abrir e ler o arquivo
with open('loremipsum.txt', 'r') as arquivo:
    conteudo_with = arquivo.read()

# Imprime o conteúdo lido usando `with`
print("\nConteúdo do arquivo lido com 'with':")
print(conteudo_with)
