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
)

st.write("# Welcome to dashboard! 👋")
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Some data")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=128)

with col2:
    st.header("Column 2")
    st.write("Some more data")

st.markdown("""
<style>
body
{
    background-color: blue;
}
</style>
""", unsafe_allow_html=True
)

st.sidebar.success('select a demo')
st.sidebar.success("In working.")
# Just add it after st.sidebar:
a = st.sidebar.radio('Choose:',[1,2])

with st.chat_message("user"):
    st.write("Hello 👋")
    st.chat_input("Say something")
    st.write('resposta')
# st.toast('Mr Stay-Puft')

bar = st.progress(50)
time.sleep(3)
bar.progress(100)
with st.container():
    st.write("This is inside a container")


# st.button('Aperte aqui!', type='primary')
# if st.button('say heelo'):
#     st.write('putz')
# else:
#     st.write('saiu')




#----------------apresentação dos dados------------------
x = st.slider('x', min_value=1, max_value=15)
st.write(x, 'squared is', x*x)
sales_country = df.groupby(['COUNTRY', 'YEAR_ID'])['SALES'].sum().reset_index()
sales_USA = salesPerCountry(df, 'USA')
sales_country.sort_values(by='YEAR_ID', inplace=True)

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

# Create a scatter_geo plot using ISO codes
fig = px.choropleth(sales_country, 
                     locations=sales_country['COUNTRY'].map(country_iso_mapping),  # Map country names to ISO codes
                    #  size='SALES',
                    color_continuous_scale=px.colors.sequential.Plasma,
                     color='COUNTRY',
                     projection='natural earth',
                     animation_frame="YEAR_ID",
                     title='Scatter Geo Plot with Custom Country Names'
                    )

fig.update_layout(
    font=dict(size=22),
    title_text='Vendas anual mundial')

st.plotly_chart(fig, se_container_width=True)






# fig = px.scatter_geo(sales_country, locations="COUNTRY", color="SALES",
#                      hover_name="COUNTRY", projection="natural earth")
# fig.show()
# fig = px.sunburst(df, path=['COUNTRY', 'CITY'], values='SALES', color='COUNTRY')

# st.plotly_chart(fig, use_container_width=True)