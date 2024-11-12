# Leitura do arquivo e separação das palavras
lista_palavras = []
with open('texto.txt', 'r') as arquivo:
    for linha in arquivo:
        palavras = linha.split()
        lista_palavras.extend(palavras)

# Ordenação usando o método nativo sort()
lista_palavras.sort()

# Criação do novo arquivo com as palavras ordenadas
with open('texto_ordenado.txt', 'w') as arquivo_ordenado:
    for palavra in lista_palavras:
        arquivo_ordenado.write(palavra + '\n')

print("Arquivo 'texto_ordenado.txt' criado com as palavras ordenadas.")
