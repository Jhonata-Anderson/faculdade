from operacoes import calculoDaMedia, verificarAlunoReprovado, mostrarAlunosReprovados;

# Dados dos alunos e notas de cada bimestre
dadosAlunos = [
    {"nome": "Maria", "matricula": 26, "notas": [8, 7, 5, 9]},
    {"nome": "Ana", "matricula": 101, "notas": [9, 9, 8, 9]},
    {"nome": "João", "matricula": 13, "notas": [6, 5, 5, 5]},
    {"nome": "Ágatha", "matricula": 37, "notas": [8, 6, 7.5, 9]},
    {"nome": "Joaquim", "matricula": 72, "notas": [6, 5.5, 5, 7]},
    {"nome": "Félix", "matricula": 5, "notas": [10, 8, 8, 8]}
]

# Calcular a média de cada aluno
for aluno in dadosAlunos:
    aluno['media'] = calculoDaMedia(aluno['notas']);

# Verificar se um aluno foi reprovado e identificar quem foi reprovado
alunosReprovados = []
for aluno in dadosAlunos:
    if verificarAlunoReprovado(aluno['media']):
        alunosReprovados.append(aluno['matricula']);

# Imprimir os dados dos alunos reprovados
print(mostrarAlunosReprovados(dadosAlunos, alunosReprovados));
