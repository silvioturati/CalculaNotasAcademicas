"""
Calculadora para notas academicas.

Sumpário da idéia:
A pontuação final é uma média das notas dos trabalhos, provas e laboratório seguindo os pesos abaixo:
25% para a média dos trabalhos
55% para a média das provas
20% para a média do laboratório

A nota segue a seguinte classificação:
90 = A
80 = B
70 = C
60 = D
abaixo = F

No final apresentar a média da classe
"""

from helpers import media_ponderada, atribuir_nota, media_classe, alunos

if __name__ == '__main__':
    for aluno, detalhes in alunos.items():
        media_total_aluno = round(media_ponderada(alunos[aluno]), 1)
        print(f"A média das notas do {alunos[aluno]['nome'].title()} é {media_total_aluno}")
        print(f"A nota final do aluno {alunos[aluno]['nome'].title()} é {atribuir_nota(media_total_aluno)}")
        print("------------------------")

    print(f"\nA média da classe foi {round(media_classe(), 1)} ou nota {atribuir_nota(media_classe())}")