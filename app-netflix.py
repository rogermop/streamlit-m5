# Ivet Ceballos Gonzalez A01066960

import streamlit as st
import pandas as pd

st.title('Netflix app')

DATA_URL = ('movies.csv')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    return data


def filtrar_titulo(titulo):
    filtered_data = data[data['name'].str.upper().str.contains(titulo)]
    return filtered_data


def filtrar_director(director):
    filtered_data = data[data['director'] == director]
    return filtered_data


data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")

sidebar = st.sidebar
agree = sidebar.checkbox("Mostrar todas las peliculas")
if agree:
    st.dataframe(data)

titulo_peli = sidebar.text_input('Titulo de la pelicula :')
buscar = st.sidebar.button('Buscar peliculas')

if (buscar):
    filterbyname = filtrar_titulo(titulo_peli.upper())
    count_row = filterbyname.shape[0]
    st.write(f"Total peliculas mostradas : {count_row}")
    st.write(filterbyname)

director_peli = sidebar.selectbox(
    'Seleccionar Director', data['director'].unique())
directorBtn = sidebar.button('Filtrar director')

if (directorBtn):
    filterbydirector = filtrar_director(director_peli)
    count_row = filterbydirector.shape[0]
    st.write(f"Total peliculas : {count_row}")
    st.write(filterbydirector)
