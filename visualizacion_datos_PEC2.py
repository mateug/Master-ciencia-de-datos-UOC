import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import inspect
import networkx as nx
import plotly.graph_objects as go

# Función para generar coordenadas en el disco de Poincaré con forma radial
def poincare_disk_layout(G):
    pos = {}
    levels = {}  # Nivel de cada nodo en el árbol
    root = 0
    levels[root] = 0
    
    # Asignar niveles a los nodos
    for node in nx.bfs_tree(G, root):
        parent = list(G.predecessors(node)) if G.in_degree(node) > 0 else []
        levels[node] = levels[parent[0]] + 1 if parent else 0
    
    max_level = max(levels.values())
    
    # Acortar distancias a medida que se alejan del centro (radialmente)
    for level in range(max_level + 1):
        nodes_at_level = [n for n, lvl in levels.items() if lvl == level]
        theta = np.linspace(0, 2 * np.pi, len(nodes_at_level), endpoint=False)
        r = (1 - np.exp(-level / max_level))  # Distancia decreciente con la profundidad
        for i, node in enumerate(nodes_at_level):
            x, y = r * np.cos(theta[i]), r * np.sin(theta[i])
            pos[node] = (x, y)
    
    return pos

#%%
def generate_heatmap():
    productos = ["Laptops", "Tablets", "Smartphones", "Monitores", "Teclados", "Ratones", "Impresoras", "Auriculares", "Consolas", "Cámaras"]
    data = np.random.rand(len(productos), len(productos))
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(data, annot=False, fmt=".2f", cmap="coolwarm", linewidths=0.5, xticklabels=productos, yticklabels=productos, ax=ax)
    return fig

def generate_raincloud_plot():
    regiones = ["Norte", "Sur", "Este", "Oeste", "Centro"]
    data = {
        "Región": np.random.choice(regiones, 200),
        "Altura (cm)": np.random.normal(loc=170, scale=10, size=200)
    }
    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x="Región", y="Altura (cm)", data=df, width=0.3, showcaps=False, 
                boxprops={"facecolor": "none", "edgecolor": "black"},
                whiskerprops={"color": "black"}, medianprops={"color": "red"}, ax=ax)
    sns.violinplot(x="Región", y="Altura (cm)", data=df, palette="Set2", split=True, inner=None, ax=ax)
    sns.stripplot(x="Región", y="Altura (cm)", data=df, color="black", size=3, alpha=0.5, ax=ax)
    return fig

def generate_hyperbolic_tree():
    G = nx.balanced_tree(r=2, h=4, create_using=nx.DiGraph)  # Árbol jerárquico
    pos = poincare_disk_layout(G)  # Posiciones en el disco de Poincaré
    edge_x, edge_y = [], []
    
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines'
    )
    
    node_x, node_y, node_texts = [], [], []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_texts.append(f'Miembro {node}')
    
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        marker=dict(size=10, color='blue'),
        text=node_texts,
        textposition='top center',
        hoverinfo='text'
    )
    
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=0),
                        xaxis=dict(showgrid=False, zeroline=False),
                        yaxis=dict(showgrid=False, zeroline=False)
                    ))
    return fig

def show_code(func):
    code = inspect.getsource(func)
    st.code(code, language='python')

#%% Subir a streamlit
st.title("Análisis de Datos con Visualizaciones Avanzadas")
    
st.header("Heatmap de Correlación de Ventas en Tecnología")
st.write("Este heatmap muestra la correlación entre distintos productos tecnológicos en una tienda.")
heatmap_fig = generate_heatmap()
st.pyplot(heatmap_fig)
st.write("### Código de la función `generate_heatmap`:")
show_code(generate_heatmap)

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

st.write("Recarga la página para ver nuevos valores aleatorios.")