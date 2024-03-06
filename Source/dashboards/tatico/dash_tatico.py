import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


def salesPerCountry(df, country): #retorno somente duas colunas, perco informações de outras.
    salesPerCountry = df.loc[df['COUNTRY'] == country] #filtro somente o pais que eu quero
    # salesPerCountry = salesPerCountry[['CITY', 'SALES']] #seleciono somente essas colunas
    # salesPerCountry = salesPerCountry.groupby(['CITY', 'PRODUCTLINE', 'STATUS'])[['SALES', 'QUANTITYORDERED']].sum().reset_index()
    salesPerCountry = salesPerCountry.groupby(['CITY'])[['SALES']].sum().reset_index()
    # salesPerCountry = salesPerCountry.groupby('SALES')
    # salesPerCountry.sort_values(by='SALES', inplace=True)
    return salesPerCountry

df = pd.read_csv('sales_data.csv', sep=',', encoding='Windows-1252')

#-------------------Configuração da página----------------
st.set_page_config(
    page_title="DashBoard",
    page_icon="👋",
)

st.write("# Welcome to dashboard! 👋")

# st.sidebar.success("In working.")

st.markdown("""
<style>
body {
background-color: blue;
}
</style>
""", unsafe_allow_html=True
)

st.sidebar.success('select a demo')




#----------------apresentação dos dados------------------
x = st.slider('x', min_value=1, max_value=15)
st.write(x, 'squared is', x*x)
sales_country = df.groupby(['COUNTRY', 'CITY'])['SALES'].sum().reset_index()
sales_USA = salesPerCountry(df, 'USA')
sales_country.sort_values(by='SALES', inplace=True)
fig = px.sunburst(df, path=['COUNTRY', 'CITY'], values='SALES', color='COUNTRY')

fig.update_layout(
    height=1000,  # Set the desired height
    width=1400,    # Set the desired width
    font=dict(size=22),
    title=dict(
        text="Vendas por paises",  # Set the title text
        font=dict(
            family="Arial",  # Set the font family for the title (optional)
            size=18          # Set the font size for the title
        )
    )
)
st.plotly_chart(fig, use_container_width=True)