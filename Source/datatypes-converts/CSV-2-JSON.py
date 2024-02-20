import pandas as pd

with open("./Dados/ipeadata[09-02-2024-07-41].csv", "r") as arquivo:
    arquivo_read = pd.read_csv(arquivo, delimiter=',')

selected_columns = arquivo_read
selected_columns.to_json("./Dados/selected.json", orient='table', indent=4, index=False)