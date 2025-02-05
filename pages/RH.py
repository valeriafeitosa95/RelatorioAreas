# Importando as bibliotecas
import streamlit as st 
import plotly_express as px
import pandas as pd

# Configuração da página
st.set_page_config(page_title='Dashboard Areas', layout= 'wide', page_icon= '🌐', initial_sidebar_state='auto')


# Título
st.header('RELATÓRIO DE RECURSOS HUMANOS', divider="blue")
st.write('')
st.write('')

# Carregando os dados
dfRH = pd.read_excel('db/RH.xlsx')


# Métricas das colunas de 1 a 4.
col1, col2, col3, col4 = st.columns(4)
with col1:
    with st.container(border=True):
        qtdadefunc = dfRH['Ativo'].count()
        st.metric(label='**Funcionários Ativos**', value= qtdadefunc)
with col2:
    with st.container(border=True):
        desligados = dfRH['Desligado'].count()
        st.metric(label='**Funcionários Desligados**', value= desligados)
with col3:
    with st.container(border=True):
        med = round(dfRH['Salario_Mensal'].mean())
        media = '{0:,}'.format(med).replace(',','.')
        st.metric(label='**Média Salarial (R$)**', value= media)
with col4:
    with st.container(border=True):
        tempomedio = round(dfRH['Anos_na_Empresa'].mean())
        st.metric(label='**Tempo Médio na Empresa**', value= tempomedio)
st.write(' ')
st.write(' ')

# Agrupando os funcionários ativos
genero = dfRH.groupby('Genero', as_index=False)['Ativo'].count()
disponivel = dfRH.groupby('Disponivel_Hora_Extra', as_index=False)['Ativo'].count()
area = dfRH.groupby('Departamento', as_index=False)['Ativo'].count()
nivel = dfRH.groupby('Nivel_Satisfacao_Trabalho', as_index=False)['Id_Funcionario'].count()

# Colunas 5 e 6 - Gráficos de Pizza - Genero e Disponibilidade
col5, col6 = st.columns(2, gap="small")
with st.container(border=True):
    with col5:
        fig = px.pie(genero, values='Ativo', names='Genero', color_discrete_sequence=px.colors.sequential.Jet)
        fig.update_layout(title_text = 'Funcionários por Genero', title_xref='paper', title_font_color='White')
        fig.update_layout(legend=dict(orientation="h"), legend_font_size=16)
        fig.update_traces(textfont_size=16)
        st.plotly_chart(fig, use_container_width=True)
        st.caption('Fonte: Dados fictícios')
        st.write(' ')

        fig = px.pie(disponivel, values='Ativo', names='Disponivel_Hora_Extra', color_discrete_sequence=px.colors.sequential.YlGnBu_r)
        fig.update_layout(title_text = 'Disponíveis para Hora Extra', title_xref='paper', title_font_color='White')
        fig.update_layout(legend=dict(orientation="h"), legend_font_size=16)
        fig.update_traces(textfont_size=16)
        st.plotly_chart(fig, use_container_width=True)
        st.caption('Fonte: Dados fictícios')
        st.write(' ')
    with col6:
        fig = px.bar(area.sort_values(by='Ativo', ascending= True), y= 'Departamento', x='Ativo', color='Ativo')
        fig.update_layout(title_text = 'Funcionários por Departamento', title_xref='paper', title_font_color='White')
        fig.update_xaxes(title = "")
        fig.update_yaxes(title = "")
        st.plotly_chart(fig, use_container_width=True)
        st.caption('Fonte: Dados fictícios')
        st.write(' ')

        fig = px.bar(nivel.sort_values(by='Id_Funcionario', ascending= True), x='Nivel_Satisfacao_Trabalho', y='Id_Funcionario', color_discrete_sequence=px.colors.sequential.Jet)
        fig.update_layout(title_text = 'Nível de Satisfação no Trabalho', title_xref='paper', title_font_color='White')
        fig.update_xaxes(title = "")
        fig.update_yaxes(title = "")
        st.plotly_chart(fig, use_container_width=True)
        st.caption('Fonte: Dados fictícios')
        st.write(' ')


        
       