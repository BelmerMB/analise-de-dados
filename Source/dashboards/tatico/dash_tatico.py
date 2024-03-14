import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import time


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
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "#test"
    }
)

st.write("# Tatic dashboard! 👋")
# col1, col2 = st.columns(2)
# with col1:
#     st.header("Column 1")
#     st.write("Some data")
#     st.image("https://static.streamlit.io/examples/cat.jpg", width=128)

# with col2:
#     st.header("Column 2")
#     st.write("Some more data")
# with st.chat_message("user"):
#     st.write("Hello 👋")
#     st.chat_input("Say something")
#     st.write('resposta')
# # st.toast('Mr Stay-Puft')
# with st.container():
#     st.write("This is inside a container")
# st.sidebar.success('select a demo')
# st.sidebar.success("In working.")
# # Just add it after st.sidebar:
# a = st.sidebar.radio('Choose:',[1,2])
# #progresso da barra
# bar = st.progress(50)
# time.sleep(3)
# bar.progress(100)
# x = st.slider('x', min_value=1, max_value=15)
# st.write(x, 'squared is', x*x)

st.markdown(
    f"""
    <style>
        .stPlotlyChart {{
            display: flex;
            justify-content: center;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

#----------------Manipulação dos dados------------------
sales_country_total = df.groupby(['COUNTRY','YEAR_ID'])['SALES'].sum().reset_index() #agrupando os dados por pais e ano
sales_country = df.groupby(['COUNTRY','PRODUCTLINE'])['SALES'].sum().reset_index() #agrupando os dados por pais e ano
sales_USA = salesPerCountry(df, 'USA')#filtrando por pais. retorna os valores agrupados.
# sales_country.sort_values(by='SALES', inplace=True) #ordem crescente dos dados

country_iso_mapping = {
    'USA': 'USA',
    'France': 'FRA',
    'Norway': 'NOR',
    'Australia': 'AUS',
    'Finland': 'FIN',
    'Austria': 'AUT',
    'UK': 'GBR',
    'Spain': 'ESP',
    'Sweden': 'SWE',
    'Singapore': 'SGP',
    'Canada': 'CAN',
    'Japan': 'JPN',
    'Italy': 'ITA',
    'Denmark': 'DNK',
    'Belgium': 'BEL',
    'Philippines': 'PHL',
    'Germany': 'DEU',
    'Switzerland': 'CHE',
    'Ireland': 'IRL'
}

# st.markdown("## ")
st.markdown(
    "<h2 style='text-align: center;'>Sales per country</h2>",
    unsafe_allow_html=True
)
st.bar_chart(sales_country_total, x='COUNTRY', y='SALES', color='COUNTRY', use_container_width=True,height=600)

# st.scatter_chart(sales_country, x='COUNTRY', y='SALES', color='PRODUCTLINE')
# Create a scatter_geo plot using ISO codes
fig = px.sunburst(sales_country, path=['COUNTRY', 'PRODUCTLINE'], values="SALES", height=800)

fig.update_layout(
    font=dict(size=18),
    title_text='Vendas anual mundial',
    margin=dict(t=50, l=50, r=50, b=50))


st.markdown(
    f"""
    <style>
        .stPlotlyChart {{
            display: flex;
            justify-content: center;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.plotly_chart(fig, se_container_width=True)