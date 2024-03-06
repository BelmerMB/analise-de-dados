import streamlit as st
import pandas as pd
import numpy as np


def confi_menu():
    st.title("peida")
    st.header('test')


# df = pd.DataFrame(
#     np.random.rand(10,3), 
#     columns=['Preço', 'Taxa de ocupação', 'Taxa de Inadimplência'])

df_one = pd.read_csv('data.csv')
df_one.dropna(inplace=True)
#basica
# st.table(df_one)
#exibição mais completa
# st.write(df_one)
#st.dataframe(df_one)
#grafico de linha
# st.pydeck_chart(df_one)
st.line_chart(df_one)
# st.sidebar.progress(0)
confi_menu()
