import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
path='machinery_data.csv'
df=pd.read_csv(path)

st.title('Dashboard de Produção de Máquinas')
y=df.groupby('Machine_Type')['Failures'].sum()
fig, ax=plt.subplots()
ax.bar(y['Machine_Type'],y['Failures'])
st.pyplot(fig)
