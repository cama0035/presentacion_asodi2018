import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='HEMODIÁLISIS CRÓNICA EN CHILE')
st.header('HEMODIÁLISIS CRÓNICA EN CHILE')
st.subheader('P.M.P. SEGUN AÑO')


### --- LOAD DATAFRAME
excel_file = 'Consolidado2.xlsx'
sheet_name = 'Consolidado2'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:I',
                   header=0)


# --- STREAMLIT SELECTION
anos = df['ANOS'].unique().tolist()

anos_selection = st.slider('ANOS:',
                        min_value= min(anos),
                        max_value= max(anos),
                        value=(min(anos),max(anos)))


# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['ANOS'].between(*anos_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')


# --- GROUP DATAFRAME AFTER SELECTION
df_mask = df[mask]
df_mask = df_mask.reset_index()


# --- PLOT BAR CHART
bar_chart = px.bar(df_mask,
                   x='ANOS',
                   y='PACIENTES',
                   text='PACIENTES',
                   color_discrete_sequence =['#F63366']*len(df),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)


# --- DISPLAY IMAGE & DATAFRAME
col1, col2 = st.columns(2)
image = Image.open('images/1.jpg')
col1.image(image,
        caption='Designed by cmunoz / DataHounder',
        use_column_width=True)
col2.dataframe(df[mask])


# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['ANOS'].between(*anos_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')


# --- PLOT LINE CHART
line_chart = px.line(df_mask,
                   x='ANOS',
                   y=['HOSPITALES2', 'CENTROS2', 'CASAS2'],
                   color_discrete_sequence =['#F63366', '#2e29cc', '#20a825']*len(df_mask),
                   template= 'plotly_white')
st.plotly_chart(line_chart)


image = Image.open('images/2.jpg')
st.image(image,
        caption='Designed by cmunoz / DataHounder',
        use_column_width=True)
