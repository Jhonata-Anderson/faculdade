# Conteúdo inicial
informacaoPessoal = {
    1: {'nome' : 'Maria', 'idade' : 26, 'nacionalidade' : 'brasileira'}
}
informacaoPessoal.update({
    2: {'nome' : 'Jhonata', 'idade' : 19, 'nacionalidade' : 'brasileiro'}
});
print(informacaoPessoal);

# Criando uma copia com copy
copiaInformacaoPessoal = informacaoPessoal.copy();

# Removendo elemento com pop
copiaInformacaoPessoal.pop(2);
print(copiaInformacaoPessoal);

# Utilizando o popitem para mostrar o último elemento removido
print(informacaoPessoal.popitem());

# Removendo todos os elementos dos dicionarios
informacaoPessoal.clear();
copiaInformacaoPessoal.clear();

# Usando o método fromKeys para definir um novo dicionário
novoDicionario = dict.fromkeys([1, 2, 3], 0);
print(novoDicionario.items());
print(novoDicionario.keys());
print(novoDicionario.values());
