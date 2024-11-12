# Conteúdo inicial
meu_dicionario = {
    1: {'linguagem': 'Python'},
    2: {'linguagem': 'Java'},
    3: {'linguagem': 'PHP'}
};

# tipo de dados com type
print(type(meu_dicionario));

# Mostrar o elemento da chave com get
print(meu_dicionario.get(1).get('linguagem'))

# criando outro dicionario com o método dict
dicionario_frutas = dict()

# Inserindo os elementos no novo dicionário
dicionario_frutas[1] = {'nome': 'limão', 'tipo': 'ácida'}
dicionario_frutas[2] = {'nome': 'laranja', 'tipo': 'ácida'}
dicionario_frutas[3] = {'nome': 'manga', 'tipo': 'semiácida'}
dicionario_frutas[4] = {'nome': 'maça', 'tipo': 'semiácida'}
dicionario_frutas[5] = {'nome': 'banana', 'tipo': 'doce'}
dicionario_frutas[6] = {'nome': 'mamão', 'tipo': 'doce'}

# Mostrar o nome e tipo da chave 1
print(dicionario_frutas[1]['nome'], dicionario_frutas[1]['tipo']);

# Mostrar o nome e tipo da chave 2
print(dicionario_frutas[2]['nome'], dicionario_frutas[2]['tipo']);

# Utilizando o laço for para exibir todos os elementos do dicionario
for chave, valor in dicionario_frutas.items():
    print(chave, valor['nome'], valor['tipo']);
