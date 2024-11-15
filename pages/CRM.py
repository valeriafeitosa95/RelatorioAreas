# Importando as bibliotecas
import streamlit as st 
import plotly_express as px
import pandas as pd

# Configuração da página
st.set_page_config(page_title='Dashboard Areas', layout= 'wide', page_icon= '🌐', initial_sidebar_state='auto')

# Título
st.header('RELATÓRIO DE CRM', divider="red")
st.write('')
st.write('')

# Carregando os dados
dfCom = pd.read_excel('db/Comercial.xlsx') 
dfDados= pd.read_excel('db/Dados.xlsx')

# Abas 1 e 2
tab1, tab2 = st.tabs(['📈 Painel','Mapa de Vendas'])
with tab1:
    st.write("")
    st.write("")
    
    # Agrupando os pedidos por pais e clientes
    totalpais= dfCom.groupby('Pais', as_index=False)['Pedidos'].count()
    totalclientes = dfCom.groupby('Clientes', as_index=False)['Pedidos'].count()

    # Métricas gerais nas colunas de 1 a 5.
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        with st.container(border=True):
            total= round(dfCom['Valor_Total'].sum(),2)
            faturamento= '{0:,}'.format(total).replace(',','.')
            st.metric(label='**Faturamento (R$)**', value=faturamento)
    with col2:
        with st.container(border=True):
            media= round(dfCom['Valor_Total'].mean())
            ticket= '{0:,}'.format(media).replace(',','.')
            st.metric(label='**Ticket Médio (R$)**', value= ticket)
    with col3:
        with st.container(border=True):
            contagem= dfCom['Pedidos'].count()
            pedidos= '{0:,}'.format(contagem).replace(',','.')
            st.metric(label='**Vendas Realizadas**', value= pedidos)
    with col4:
        with st.container(border=True):
            conta= totalpais['Pais'].count()
            paises= '{0:,}'.format(conta).replace(',','.')
            st.metric(label='**Países Atendidos**', value= paises)
    with col5:
        with st.container(border=True):
            cliente= totalclientes['Clientes'].count()
            clientes= '{0:,}'.format(cliente).replace(',','.')
            st.metric(label='**Clientes Atendidos**', value=clientes)
    st.write(' ')
    st.write(' ')
    
    # Agrupando os dados por segmento, categoria e canal de atendimento
    segmento = dfCom.groupby('Segmento', as_index=False)['Pedidos'].count()
    categoria = dfCom.groupby('Categoria', as_index=False)['Pedidos'].count()
    canalAtendimento = dfCom.groupby('Canal_Atendimento', as_index=False)['Pedidos'].count()

    # Colunas 6, 7 e 8 contendo os gráficos de rosca.
    st.write('Pedidos')
    col6, col7, col8 = st.columns(3)
    with col6:
        with st.container(border=True):
            fig = px.pie(segmento, values='Pedidos', names='Segmento', title='Por Seguimento',
                        hole=0.3, color_discrete_sequence=px.colors.sequential.RdBu)
            fig.update_layout(titlefont={'family':'Arial','size': 20, 'color': 'white'})
            fig.update_layout(legend=dict(orientation="h"))
            fig.update_traces(textfont_size=16)
            st.plotly_chart(fig, use_container_width=True)
            st.caption('Fonte: Dados fictícios')
            st.write('')
    with col7:
        with st.container(border=True):
            fig = px.pie(categoria, values='Pedidos', names='Categoria', title='Por Categoria de Produto',
                        hole=0.3, color_discrete_sequence=px.colors.sequential.RdBu)
            fig.update_layout(titlefont={'family':'Arial','size': 20, 'color': 'white'})
            fig.update_layout(legend=dict(orientation="h"))
            fig.update_traces(textfont_size=16)
            st.plotly_chart(fig, use_container_width=True)
            st.caption('Fonte: Dados fictícios')
            st.write('')
    with col8:
        with st.container(border=True):
            fig = px.pie(canalAtendimento, values='Pedidos', names='Canal_Atendimento', title='Por Canal de Atendimento',
                        hole=0.3, color_discrete_sequence=px.colors.sequential.RdBu)
            fig.update_layout(titlefont={'family':'Arial','size': 20, 'color': 'white'})
            fig.update_layout(legend=dict(orientation="h"))
            fig.update_traces(textfont_size=16)
            st.plotly_chart(fig, use_container_width=True)
            st.caption('Fonte: Dados fictícios')
            st.write('')

    # Colunas 9 e 10 contendo os gráficos de barras
    col9, col10 = st.columns(2)
    with col9:
        with st.container(border=True):
            fig = px.bar(dfDados.sort_values(by='Pedidos', ascending= True), y= 'Pais', x='Clientes',
                        title='Clientes por País',labels=True , color_discrete_sequence=px.colors.sequential.Turbo_r)
            fig.update_xaxes(title = "")
            fig.update_yaxes(title = "")
            fig.update_layout(titlefont={'family':'Arial','size': 20, 'color': 'white'})
            fig.update_layout(font={'family':'Arial','size': 16, 'color': 'white'})
            st.plotly_chart(fig, use_container_width=True)
            st.caption('Fonte: Dados fictícios')
            st.write(' ')
    with col10:
        with st.container(border=True):
            fig = px.bar(totalpais.sort_values(by='Pedidos', ascending= True), y= 'Pais', x='Pedidos',
                        title='Pedidos por País', color_discrete_sequence=px.colors.sequential.Turbo_r)
            fig.update_xaxes(title = "")
            fig.update_yaxes(title = "")
            fig.update_layout(titlefont={'family':'Arial','size': 20, 'color': 'white'})
            fig.update_layout(font={'family':'Arial','size': 16, 'color': 'white'})
            st.plotly_chart(fig, use_container_width=True)
            st.caption('Fonte: Dados fictícios')
            st.write(' ')
            
# Aba 2 contendo o mapa            
with tab2:
    fig = px.choropleth(dfDados, locations='Codigo', color='Pedidos',
                        color_continuous_scale=px.colors.sequential.Bluered, hover_name='Pais')
    fig.update_layout(margin=dict(l=30, r=30, t=30, b=30))
    st.plotly_chart(fig, use_container_width=True)
    st.caption('Fonte: Dados fictícios')
    st.write(' ')
