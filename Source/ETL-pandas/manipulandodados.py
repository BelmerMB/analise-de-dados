import pandas as pd 
import matplotlib.pyplot as plt

mt = plt

with open("../../Dados/ipeadata[09-02-2024-07-41].csv", "r") as alunos:
    aln = pd.read_csv(alunos, sep=',')

db = pd.DataFrame(aln)
plt.xlabel(db['Data'])
plt.ylabel(db['Balanço'])
plt.plot(db)