import pandas as pd

with open('Aluno.json', 'r') as alunos:
    alunos_arquivo = pd.read_json(alunos)

alunos_arquivo.to_csv("alunos.csv", index=False)
# with open('alunos.csv', 'r') as alunosjson:
#     alunos_tojson = pd.read_csv(alunos_arquivo)
# alunos_tojson.to_json("alunos2.json")