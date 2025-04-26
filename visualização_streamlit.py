import pandas as pd
import streamlit as st
import matplotlib.pyplot as plp
path='machinery_data.csv'
df=pd.read_csv(path)

st.title('Dashboard de Produção de Máquinas')
y=df.groupby('Machine_Type')['Failures'].sum()
fig, x=plt.subplots()
x.bar(y['Machine_Type'],y['Failures'])
st.pyplot(fig)
