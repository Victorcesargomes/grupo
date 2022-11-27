import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

st.set_page_config(layout='wide')

image = Image.open('pontually-removebg.png')
st.image(image, width=600)
st.markdown("---")

st.title(":bar_chart:Business Intelligence")

dados = pd.read_csv("ne_seguranca_10.csv", encoding='latin-1', sep=';', decimal=',')

c1, c2 = st.columns(2)

for tem in ["plotly_dark"]:
    fig = px.bar(dados, x='Liquido', y='Cliente',
    labels={"Liquido": "Faturamento Líquido", "Cliente":"Clientes", "Bruto":"Faturamento Bruto"}
    , title="Faturamento por Cliente (10/2022)", template=tem, color_discrete_sequence=["#0083B8"])
    
    c1.plotly_chart(fig)
    c1.markdown("**A Empresa Pandenor apresenta a melhor Receita Líquida. O EDF. Maria da Penha, por sua vez, configura a menor Receita Líquida entre os clientes.**")

for t in ["plotly_dark"]:
    fig1 = px.bar(dados, x='Lucro', y='Cliente', color='Folha', title="Lucro por Cliente (10/2022)",
    labels={"Cliente":"Clientes"}, template=t, color_discrete_sequence=["#0083B8"])
    c2.plotly_chart(fig1)
    c2.markdown("**O cliente Instituto de Vida Consagrada apresentou o melhor Retorno Líquido (Lucro de R$ 29.000,99)**")

st.markdown("---")
c3, c4 = st.columns(2)

for template in ['plotly_dark']:
    fig2 = px.bar(dados,y='Folha', x='Cliente', color='Funcionarios', template=template, 
    title="Folha por Cliente (10/2022)", labels={"Cliente": "Clientes"}, color_discrete_sequence=["#0083B8"])
    c3.plotly_chart(fig2)
    c3.markdown("**A empresas TEMAPE configura como um dos clientes com  maior Despesa com Folha. Além disso, a empresa possui 13 funcionários ativos.**")
    

for temas in ["plotly_dark"]:
    fig3 = px.scatter(dados, x='Folha', y='Lucro', color='Liquido',trendline="ols",
     title="Lucro vs Receita Líquida (10/2022)",
     template=temas,color_discrete_sequence=["#0083B8"])
    
    c4.plotly_chart(fig3)
    c4.markdown("**O gráfico a cima demonstra uma relação positiva entre a Folha e o Lucro, isto é, mesmo com uma Despesa com Folha significativa; o que vai impactar o lucro é o tamaho da Receita. No caso da NE Segurança Matriz, a qualidade da Receita está fortemente ligada ao seu aspecto quantitativo.**")
    #fig3 = px.scatter(dados,x="Cliente", y="Folha", color='Funcionarios',template=template)
    #c4.plotly_chart(fig3)

st.markdown("---")

## Mapa
st.header("**Mapa**")
mapa = dados

map = px.scatter_mapbox(mapa, lat='Lat', lon='Long', hover_name= 'Cliente',
                         color = 'Bruto',
                         hover_data={'Lat':False, 'Long':False,'Liquido':True, 'Lucro':True,
                         'Folha': True, 'Funcionarios': True},
                         size='Liquido',
                         color_continuous_scale=px.colors.cyclical.IceFire,
                         zoom=6,height=300, labels={"Bruto": "Faturamento Bruto",
                         "Liquido": "Faturamento Líquido", "Funcionarios": "N° de Funcionários"})

map.update_layout(mapbox_style='open-street-map')
map.update_layout(height=400, margin={'r':0, 't':0, 'l':0, 'b':0})
st.plotly_chart(map)