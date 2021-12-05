from numpy.lib.function_base import rot90
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style('darkgrid')

st.title("Bienvenido al visualizador")
st.markdown("## Casos positivos Covid por Region y Comuna.")
df = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto65/PositividadPorComuna.csv")

col1,col2=st.columns(2)

with col1:
    region = st.radio("Seleccione Region: ", df.Region.unique())
    st.markdown("Su seleccion es: "+region)
with col2:
    comuna = st.selectbox ("Seleccione comuna: ", df.Comuna.unique())
    st.write('La comuna seleccionada es: '+''+comuna)

super_filtro = df[(df.Region==region)&(df.Comuna==comuna)]
st.dataframe(super_filtro)
fig,ax= plt.subplots()
to_plot=(super_filtro.iloc[:,5:-1])
ax.plot(to_plot.T)

ax.set_title(region)
ax.set_ylabel("Casos")
ax.set_xlabel("Fechas")

ejeX=np.arange(0,super_filtro.shape[1]-1,2)
plt.xticks(ejeX,rotation=90)


st.pyplot(fig)