import pandas as pd
import streamlit as st
path='machinery_data.csv'
df=pd.read_csv(path)

st.title('Dashboard de Produção de Máquinas')


