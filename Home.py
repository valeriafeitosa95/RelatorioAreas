import streamlit as st 
import plotly_express as px
import pandas as pd
import base64

# configuração da página
st.set_page_config(page_title='Dashboard Areas', layout= 'wide', page_icon= '🌐', initial_sidebar_state='auto')


# Boas vindas - gif
st.subheader('Olá, seja bem-vindo(a)',divider='grey')
file_ = open("img/gif.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown( f'<img src="data:image/gif;base64,{data_url}" alt="gif">', unsafe_allow_html=True)
st.write('')
st.write('')
st.write('')
st.write('_____________:blue[Navegue pelas páginas para acessar os dados por área de negócio]_____________')

