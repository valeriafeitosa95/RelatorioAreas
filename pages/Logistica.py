
# Importando as bibliotecas
import streamlit as st 
import plotly_express as px
import pandas as pd

# Configuração da página
st.set_page_config(page_title='Dashboard Areas', layout= 'wide', page_icon= '🌐', initial_sidebar_state='auto')

# Título
st.header('RELATÓRIO DE LOGÍSTICA', divider="violet")
st.write('')
st.write('')

# Carregando os dados
dfLog = pd.read_excel('db/Logistica.xlsx') 

# Filtrando
norte = dfLog.query('Região == "Norte"')
nordeste = dfLog.query('Região == "Nordeste"')
sul = dfLog.query('Região == "Sul"')
sudeste = dfLog.query('Região == "Sudeste"')
centro = dfLog.query('Região == "Centro-Oeste"')

# Filtro na barra lateral
st.sidebar.subheader('**Filtro**')
lista_regioes = st.sidebar.selectbox('', options=['Todas as regiões','Norte','Nordeste','Centro-Oeste','Sul','Sudeste'])
if lista_regioes == 'Todas as regiões':
    filtro = dfLog
elif lista_regioes == 'Norte':
    filtro = norte
elif lista_regioes == 'Nordeste':
    filtro = nordeste
elif lista_regioes == 'Centro-Oeste':
    filtro = centro
elif lista_regioes == 'Sul':
    filtro = sul
else:
    filtro = sudeste

# Métricas gerais nas colunas 1, 2 e 3.
col1, col2, col3 = st.columns(3)
with col1:
    with st.container(border=True):
        pedidos = filtro['Pedidos'].count()
        pedido = '{0:,}'.format(pedidos).replace(',','.')
        st.metric(label='**Total de Pedidos**', value= pedido)
with col2:
    with st.container(border=True):
        tempomedio = round(filtro['Tempo_Entrega'].mean())
        st.metric(label='**Tempo Médio de Entrega (dias)**', value= tempomedio)
with col3:
    with st.container(border=True):
        custofrete = round(filtro['Custo_Frete'].mean())
        st.metric(label='**Custo Médio por Frete (R$)**', value= custofrete)
st.write(' ')
st.write(' ')

# Refinando o filtro por status e equipe
status = filtro.groupby('Status_Entrega', as_index=False)['Pedidos'].count()
equipe = filtro.groupby('Equipe_Entrega', as_index=False)['Pedidos'].count()

# Colunas 4 e 5 contendo os gráficos de rosca e barra
col4, col5 = st.columns(2)
with col4:
    with st.container(border=True):
        fig = px.pie(status, values='Pedidos', names='Status_Entrega', color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_layout(title_text ='Entregas por Status', title_xref='paper', title_font_color='White')
        fig.update_layout(legend=dict(orientation="h"))
        fig.update_traces(textfont_size=16)
        st.plotly_chart(fig, use_container_width=True)
        st.caption('Fonte: Dados fictícios')
        st.write(' ')
with col5:
    with st.container(border=True):
        fig = px.bar(equipe.sort_values(by='Pedidos', ascending= True), y= 'Equipe_Entrega', x='Pedidos', color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_layout(title_text ='Entregas por Equipe', title_xref='paper', title_font_color='White')
        fig.update_layout(font={'family':'Arial','size': 14, 'color': 'white'})
        fig.update_xaxes(title = "")
        fig.update_yaxes(title = "")
        st.plotly_chart(fig, use_container_width=True)
        st.caption('Fonte: Dados fictícios')
        st.write(' ')
       
# Filtrando os pedidos por região
regiao = filtro.groupby('Região', as_index=False)['Pedidos'].count()
cidade = filtro.groupby('Cidade', as_index=False)['Pedidos'].count()


# Colunas 6 e 7 contendo os gráficos de barra e treemap
col6, col7 = st.columns(2)
with col6:
    with st.container(border=True):
        fig = px.bar(regiao.sort_values(by='Pedidos', ascending= False), x='Região', y='Pedidos', color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_layout(title_text ='Entregas por Região', title_xref='paper', title_font_color='White')
        fig.update_layout(font={'family':'Arial','size': 14, 'color': 'white'})
        fig.update_xaxes(title = "")
        fig.update_yaxes(title = "")
        st.plotly_chart(fig, use_container_width=True)
        st.caption('Fonte: Dados fictícios')
        st.write(' ')
with col7:
    with st.container(border=True):
       fig = px.treemap(cidade, path=['Cidade'], values='Pedidos', color_discrete_sequence=px.colors.sequential.Agsunset)
       fig.update_layout(autosize=False)
       fig.update_layout(title_text ='Entregas por Cidade', title_xref='paper', title_font_color='White')
       st.plotly_chart(fig, use_container_width=True)
       st.caption('Fonte: Dados fictícios')
       st.write(' ')
       