import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kualitas Udara", layout="wide")

st.subheader("Data Analysis from March 1, 2013 to February 28, 2017")

data = {
    'Minggu ke-': [1, 2, 3, 4, 5, 6, 7, 8],
    'PM2.5': [267.178571, 30.357143, 61.732143, 106.137500, 90.821429, 67.755952, 87.202381, 33.869048],
    'PM10': [276.369048, 40.488095, 76.017857, 121.154167, 98.779762, 83.125000, 103.577381, 44.148810]
}

data_pm25 = {
    'Stasiun': ['Aotizhongxin', 'Changping', 'Dingling', 'Dongsi', 'Guanyuan', 'Gucheng', 'Huairou', 'Nongzhuan', 'Shunyi', 'Tiantan', 'Wanliu', 'Wanshouxigong'],
    'Mean PM2.5': [80.827438, 69.773106, 64.590090, 84.414816, 81.669655, 82.454632, 67.815537, 83.372747, 77.499906, 80.636431, 82.499085, 83.396004]
}

df_pm25 = pd.DataFrame(data_pm25)

df = pd.DataFrame(data)

st.title('Air Quality Trends at Aotizhongxin in Early 2017')
st.dataframe(df)

st.line_chart(df.set_index('Minggu ke-'))

st.bar_chart(df.set_index('Minggu ke-'))

st.subheader('Descriptive Statistics:')
st.write(df.describe())

st.title('Check Your Location!')
selected_location = st.selectbox('Select a Location:', df_pm25['Stasiun'])

mean_pm25_selected_location = df_pm25[df_pm25['Stasiun'] == selected_location]['Mean PM2.5'].values[0]
st.subheader(f'Mean PM2.5 at {selected_location}: {mean_pm25_selected_location}')