import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
path='machinery_data.csv'
df=pd.read_csv(path)

st.title('Dashboard de Produção de Máquinas')
y=df.groupby('Machine_Type')['Failures'].sum()
fig, x=plt.subplots()
x.bar(y.index,y.values)
x.set_title('Total de falhas')
st.pyplot(fig)
