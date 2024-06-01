# Conteúdo Inicial
set_inicial = {11, 12, 13, 14};
print(set_inicial);

# Adicionar o elemento com add
set_inicial.add(15);
print(set_inicial);

# Atualizando os elementos com update
set_inicial.update({1, 2, 3, 4, 5});
print(set_inicial);

# Removendo o elemento com discard
set_inicial.discard(13);
print(set_inicial);

# Criando um novo set
novo_set = {20, 21, 23, 1, 2};
print(novo_set);

# Juntando os sets
set_inicial.update(novo_set);
print(set_inicial);

# interseção dos sets
print(set_inicial & novo_set);

# diferença entre os sets
print(set_inicial - novo_set);
