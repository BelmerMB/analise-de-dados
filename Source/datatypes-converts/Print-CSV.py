import pandas as pd

with open("./Dados/alunos.csv", "r") as arquivo:
    arquivo_csv = arquivo.read()

print(arquivo_csv)



    # for i, linha in enumerate(arquivo_csv):
    #     if i == 0:
    #         print('Dados:' + str(linha))
    #     else:
    #         print('ID: '+ str(linha))