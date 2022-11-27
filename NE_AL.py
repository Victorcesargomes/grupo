import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

st.set_page_config(layout='wide')

st.title(":bar_chart:Business Intelligence")

df = pd.read_csv("ne_seguranca_al.csv", encoding='utf-16', sep=',', decimal=',')

c1, c2 = st.columns(2)

figal = px.bar(df, x='Líquido', y='Cliente', template="plotly_dark", 
color_discrete_sequence=["#0083B8"], title="Faturamento Líquido por Cliente (10/2022)",
labels={'Cliente': 'Clientes','Líquido':'Faturamento Líquido'})
c1.plotly_chart(figal)



figal1 = px.bar(df, x='Cliente', y='Lucro', color_discrete_sequence=["#0083B8"],
title="Lucro por CLiente (10/2022)", labels={'Cliente':'Clientes'}, color='Folha', template='plotly_dark')

c2.plotly_chart(figal1)
c2.markdown("**De acordo com o gráfico, o cliente SPE Maceió Ambiental apresentou o maior Resultado Líquido (Lucro) em relação aos demais clientes. No entanto, o cliente possui o maior quantitativo em termos de Folha com Pessoal. O Atacadão Praia, por sua vez, apresentou um prejuízo e ocupa a 2° colocação em termos de gasto com Folha.**")

st.markdown("---")

st.header("**Mapa**")
mapa = df

map = px.scatter_mapbox(mapa, lat='Lat', lon='Long', hover_name= 'Cliente',
                         color = 'Bruto',
                         hover_data={'Lat':False, 'Long':False,'Líquido':True, 'Lucro':True,
                         'Folha': True, 'Funcionarios': True},
                         size='Líquido',
                         color_continuous_scale=px.colors.cyclical.IceFire,
                         zoom=9,height=300, labels={"Bruto": "Faturamento Bruto",
                         "Líquido": "Faturamento Líquido", "Funcionarios": "N° de Funcionários"})

map.update_layout(mapbox_style='open-street-map')
map.update_layout(height=400, margin={'r':0, 't':0, 'l':0, 'b':0})
st.plotly_chart(map)