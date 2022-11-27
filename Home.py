import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio



st.set_page_config(page_title="Dashboards Grupo NE Segurança", 
layout='wide', page_icon=":bar_chart")

image = Image.open('pontually-removebg.png')
st.image(image, width=600)
st.markdown("---")



st.title("*Quem Somos*")
st.markdown('**Somos uma Empresa Contábil atuando no mercado desde 2008, ajudando centenas de empreendedores a gerir seus negócios. Contamos com profissionais altamente qualificados, especialistas em suas áreas de atuação e comprometidos com o nosso propósito de contribuir para a solidez das empresas em seus respectivos mercados.**')
st.markdown("---")

st.title("*Objetivo do App*")
st.markdown('**Analisar os dados financeiros da empresa tendo como principais variáveis os aspectos da Receita Líquida (Receita Bruta - Impostos e Deduções) e o resultado líquido da Despesa com Folha (Folha de Pagamentos - Descontos e Deduções). Nesse sentido, portanto, o presente App tem como objetivo analisar o impacto da Folha com Pessoal sobre a Receita Corrente Líquida - evidenciando as características quantitavivas e qualitativas das variáveis analisadas.**')
