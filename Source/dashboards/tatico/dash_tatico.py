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

st.markdown(
    "<h2 style='text-align: center;'>Dashboard</h2>",
    unsafe_allow_html=True)

#----------------Manipulação dos dados------------------
sales_country_total = df.groupby(['COUNTRY','YEAR_ID'])['SALES'].sum().reset_index() #agrupando os dados por pais e ano
sales_country = df.groupby(['COUNTRY','PRODUCTLINE','YEAR_ID'])['SALES'].sum().reset_index() #agrupando os dados por pais e ano
sales_USA = salesPerCountry(df, 'USA')#filtrando por pais. retorna os valores agrupados.
# sales_country.sort_values(by='SALES', inplace=True) #ordem crescente dos dados


#------------------interface-------------------------------
#Dict to use stantard ISO name for country to user scattermap
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

st.markdown(
    "<h2 style='text-align: center;'>Sales per country</h2>",
    unsafe_allow_html=True
)
st.bar_chart(sales_country_total, x='COUNTRY', y='SALES', color='COUNTRY', use_container_width=True,height=600)

st.markdown(
    "<h2 style='text-align: center;'>Sells per country</h2>",
    unsafe_allow_html=True
)

years_sales = sales_country_total['YEAR_ID'].unique()
year_sale_country = st.selectbox("Selecione o ano", options=years_sales)
country = st.selectbox("Selecione o pais", options=country_iso_mapping)
sales_country_unique = sales_country.loc[(sales_country['COUNTRY'] == country) & (sales_country['YEAR_ID'] == year_sale_country)]

if not len(sales_country_unique):
    st.markdown(
    "<h2 style='text-align: center;'>Doesnot have any data sales in this year</h2>",
    unsafe_allow_html=True
)


#-------------plota a sunburst grafic---------------------
fig = px.sunburst(sales_country_unique, path=['COUNTRY', 'PRODUCTLINE'], values="SALES", height=600)
fig.update_layout(
    font=dict(size=18),
    margin=dict(t=0, l=100, r=0, b=10))
st.plotly_chart(fig, se_container_width=True)

# st.markdown(
#     f"""
#     <style>
#         stPlotlyChart.js-plotly-plot {{
#             display: flex;
#             justify-content: center;
#         }}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )