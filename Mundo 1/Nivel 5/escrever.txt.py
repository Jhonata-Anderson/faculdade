# Abre (ou cria) o arquivo texto.txt para escrita
with open('texto.txt', 'w') as arquivo:
    # Cria uma lista e adiciona algumas frases a ela
    texto = list();
    texto.append("HTML CSS é só o ouro");
    texto.append("Python é só o ouro também");
    texto.append("Quanto mais, melhor");
    
    # Escreve o conteúdo da lista no arquivo
    for linha in texto:
        arquivo.write(linha + '\n');

print("Arquivo 'texto.txt' criado e conteúdo escrito com sucesso.");
