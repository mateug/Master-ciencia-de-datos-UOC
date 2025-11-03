import streamlit as st
import inspect
from functions_1 import generate_heatmap
from functions_2 import generate_nightingale_chart, generate_beeswarm_chart

def show_code(func):
    code = inspect.getsource(func)
    st.code(code, language='python')

st.title("Análisis de Datos con Visualizaciones Avanzadas")
    
st.header("Heatmap de Correlación de Ventas en Tecnología")
st.write("Este heatmap muestra la correlación entre distintos productos tecnológicos en una tienda.")
heatmap_fig = generate_heatmap()
st.pyplot(heatmap_fig)
st.write("### Código de la función `generate_heatmap`:")
show_code(generate_heatmap)

"""
st.header("Distribución de Alturas por Región")
st.write("Este raincloud plot muestra la distribución de alturas de personas dependiendo de la región donde viven.")
raincloud_fig = generate_raincloud_plot()
st.pyplot(raincloud_fig)
st.write("### Código de la función `generate_raincloud_plot`:")
show_code(generate_raincloud_plot)

st.header("Jerarquía de la Empresa (Hyperbolic Tree)")
st.write("Este gráfico muestra la jerarquía de los miembros de una empresa en forma de un árbol hiperbólico interactivo.")
hyperbolic_tree_fig = generate_hyperbolic_tree()
st.plotly_chart(hyperbolic_tree_fig)
st.write("### Código de la función `generate_hyperbolic_tree`:")
show_code(generate_hyperbolic_tree)
"""

st.header("Gráfico de Rosas de Nightingale")
st.write("Este gráfico de rosas de Nightingale muestra la distribución de ventas por categoría de producto.")
nightingale_fig = generate_nightingale_chart()
st.plotly_chart(nightingale_fig)
st.write("### Código de la función `generate_nightingale_chart`:")
show_code(generate_nightingale_chart)

st.header("Gráfico Beeswarm de Valores por Categoría")
st.write("Este gráfico beeswarm muestra la distribución de valores para diferentes categorías.")
beeswarm_fig = generate_beeswarm_chart()
st.pyplot(beeswarm_fig)
st.write("### Código de la función `generate_beeswarm_chart`:")
show_code(generate_beeswarm_chart)

st.write("Recarga la página para ver nuevos valores aleatorios.")