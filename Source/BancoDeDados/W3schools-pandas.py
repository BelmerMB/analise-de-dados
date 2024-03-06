import pandas as pd

arq = pd.read_csv('Source/BancoDeDados/data.csv', sep=',')

# a = [2, 3 ,5]
# myvar = pd.Series(a, index= ["x", "y", "z"])
# print(myvar[1])
# print('-----')
# print(myvar)
# print('-----')
# print(myvar['z'])
# print('-----')
# print('-----')

# a = {1: 420,"day": 3 , "some":5}
# myvar = pd.Series(a)
# print(myvar)
# print('-----')
# print(myvar[1])
# print('-----')
# print(myvar['some'])

# myvar = pd.Series(a, index= [1, 'some'])
# print()
# print()
# print(myvar)


var = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "cal": [420, 380, 390],
}
# #2 dimensional data structure
# #read_csv transform csv to a data frame
# myvar = pd.DataFrame(var)
# print()
# print()
# print(myvar)

# #locate a row (linha)

# print(myvar.loc[[2, 1]])

# myvar = pd.DataFrame(var, index = ['day1', ' day2', 'day3'])
# print(myvar)
# print(pd.options.display.max_rows) # I can change

#---------------- json read ------------
#json objects have the same format as python dictionaries
# df = pd.read_json("Source/BancoDeDados/data.json") # o caminho é relativo ao caminho de onde vc esta executando o programa!!
# # print(df.to_string())
# print(df.tail) #rturn the header and last n rows
# print(df.info())

# print(arq)

#Retirando valores NULL/NaN (garbage) do arquivo
#---------------------------------------------

#remove a colunas que contém todos qualquer valor faltante (para retirar linhas axis=0)
#arq.dropna(axis=1, how='all', inplace=True) #muda direto no arquivo (inplace)

# print("\n\n--------------\n\n")
# print(arq)
# #removendo linhas que contém qualquer NaN
# arck = arq.dropna(how='any')
# print("\n\n--------------\n\n")
# print(arck)


# print("\n\n--------------\n\n")
# print("\n\n--------------\n\n")
# arq['Calories'].fillna('robson', inplace=True) #substitui qualquer NaN por 666
# print(arq)

# x = arq['Calories'].mean()
# arq['Calories'].fillna(x, inplace=True)
# print(arq)


# #TRANSFORMANDO DATAS E RETIRANDO DADOS INUTEIS OU MODIFICANDO ELES
# arq['Date'] = pd.to_datetime(arq['Date'], format='mixed', errors='coerce')
# arq.dropna(inplace=True)
# # arq.dropna(subset=['Calories'], inplace=True)
# for x in arq.index:
#     if arq.loc[x, "Duration"] > 120:
#         arq.drop(x, inplace=True) 
#         #arq.loc[x, "Duration"] = 60 #modifico o valor incoerente para algum valor conhecido.
# arq.drop_duplicates(inplace=True)
# print(arq)

arquivo = pd.read_csv('./Dados/data.csv', sep=',')
# print(arquivo.duplicated())
if arquivo.duplicated().all():
    print('duplicado')

# print(arquivo[arquivo.duplicated()])
arquivo.drop_duplicates(inplace=True)
# print("apos limpeza", arquivo[arquivo.duplicated()])
arquivo.dropna(inplace=True)
# print(arquivo.duplicated)
# print("Filtrados \n\n------------------\n\n\t")
for x in arquivo.index:
  if arquivo.loc[x, 'Duration'] > 90:
    arquivo.drop(x, inplace=True)

# print(arquivo)
# arquivo.to_csv('./Dados/data-limpo.csv', sep=',', index=False)
print(arquivo.corr())
import matplotlib.pyplot as plt

arquivo.plot(x='Duration', y='Calories', kind='scatter')
plt.show()

x = '  hello  '
print(x)
print(x)
x.strip()
