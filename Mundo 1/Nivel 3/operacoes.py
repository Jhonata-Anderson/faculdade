# Realiza o cálculo da média dos alunos
def calculoDaMedia(notas):
    return sum(notas) / len(notas);

# Verifica se o aluno foi reprovado de acordo com a média
def verificarAlunoReprovado(media):
    return media < 6;

# Identifica o aluno reprovado e mostra seus dados
def mostrarAlunosReprovados(dadosAlunos, matriculasReprovadas):
    reprovados = '';
    for aluno in dadosAlunos:
        if aluno['matricula'] in matriculasReprovadas:
            reprovados = reprovados + (f'Aluno Reprovado: {aluno['nome']} - Matrícula: {aluno['matricula']} - Média Final {aluno['media']}\n');
    return reprovados;
