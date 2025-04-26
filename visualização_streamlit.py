import pandas as pd
import streamlit as st
import matplotlib.pyplot as plp
path='machinery_data.csv'
df=pd.read_csv(path)
x=df['Machine_Type'].unique()
y=df.groupby('Machine_Type')['Failures'].sum()
st.dataframe(df.head()



st.title('Dashboard de Produção de Máquinas')
st.bar_chart(x,y)

