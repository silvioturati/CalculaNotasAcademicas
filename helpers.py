from dados import alunos

def media_notas(notas):
    """
    Função para calcular a média das notas
    :param notas:[lista de notas de cada tipo de teste]
    :return: media das notas
    """
    soma = sum(notas)
    media_nota = float(soma / len(notas))
    return media_nota

def media_ponderada(aluno):
    """
    Função para calcular a média ponderada do aluno com base nos pesos informados
    :param aluno: {dicionario de alunos}
    :return: media ponderada
    """
    media_trabalhos = media_notas(aluno['trabalhos'])
    media_provas = media_notas(aluno['provas'])
    media_laboratorio = media_notas(aluno['laboratorio'])
    nota_final = (0.25 * media_trabalhos) + (0.55 * media_provas) + (0.20 * media_laboratorio)
    return nota_final

def atribuir_nota(nota_final):
    """
    Função para classificar a nota com base na media final do aluno
    :param nota_final:
    :return: nota
    """
    if nota_final >= 90:
        return "A"
    elif nota_final >= 80:
        return "B"
    elif nota_final >= 70:
        return "C"
    elif nota_final >= 60:
        return "D"
    else:
        return "F"

def media_classe():
    """
    Função para calcular a média da classe de alunos
    :return: media_classe
    """
    media_alunos = []
    for aluno, detalhes in alunos.items():
        media_aluno = media_ponderada(alunos[aluno])
        media_alunos.append(media_aluno)
    return media_notas(media_alunos)