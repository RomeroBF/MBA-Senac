

import pandas as pd #Criar dataframe
import numpy as np
import matplotlib.pyplot as plt # Criar gráficos
import seaborn as sns
import streamlit as st

path='machinery_data.csv'
df=pd.read_csv(path)

st.title('Dashboard de Produção de Máquinas')


