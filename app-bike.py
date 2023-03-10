# Ivet Ceballos Gonzalez A01066960

import streamlit as st
import pandas as pd
import numpy as np

st.title('Cicle Rides in NYC')

DATA_URL = ('citibike-tripdata.csv')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data['started_at'] = pd.to_datetime(data['started_at'])
    return data


data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")

sidebar = st.sidebar
agree = sidebar.checkbox("Show raw data")
if agree:
    st.dataframe(data)

hora_checkbox = sidebar.checkbox('Recorridos por hora')
if hora_checkbox:
    st.subheader('Numero de recorridos por hora')
    hist_values = np.histogram(
        data['started_at'].dt.hour, bins=24, range=(0, 24))[0]
    st.bar_chart(hist_values)

hora_slider = sidebar.slider('Hora', 0, 23)
filtered_data = data[data['started_at'].dt.hour == hora_slider]

st.subheader('Mapa de recorridos iniciados a las %s:00' % hora_slider)
st.map(filtered_data)
