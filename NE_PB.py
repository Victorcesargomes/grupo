import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

st.set_page_config(layout='wide')

st.title(":bar_chart:Business Intelligence")

dfpb = pd.read_csv("ne_seguranca_pb_10.csv", encoding='utf-16', sep=',', decimal=',')

c1, c2 = st.columns(2)

figpb = px.bar(dfpb, x="liquido", y='cliente', template="plotly_dark", 
color_discrete_sequence=["#0083B8"], title="Faturamento Líquido por Cliente (10/2022)",
labels={'cliente': 'Clientes','liquido':'Faturamento Líquido'})
c1.plotly_chart(figpb)

figpb1 = px.bar(dfpb, x="cliente", y='lucro', template="plotly_dark", 
color_discrete_sequence=["#0083B8"], title="Lucro por Cliente (10/2022)",
labels={'cliente': 'Clientes', 'lucro':'Lucro'}, color='folha')
c2.plotly_chart(figpb1)
c2.markdown("**O cliente Mixx Mateus Guarabira apresenta Resultado Líquido Negativo (Prejuízo).**")

st.markdown("---")

st.header("**Mapa**")
mapa = dfpb

map = px.scatter_mapbox(mapa, lat='lat', lon='long', hover_name= 'cliente',
                         color = 'bruto',
                         hover_data={'lat':False, 'long':False,'liquido':True, 'lucro':True,
                         'folha': True, 'funcionarios': True},
                         size='liquido',
                         color_continuous_scale=px.colors.cyclical.IceFire,
                         zoom=6,height=300, labels={"bruto": "Faturamento Bruto",
                         "liquido": "Faturamento Líquido", "funcionarios": "N° de Funcionários"})

map.update_layout(mapbox_style='open-street-map')
map.update_layout(height=400, margin={'r':0, 't':0, 'l':0, 'b':0})
st.plotly_chart(map)