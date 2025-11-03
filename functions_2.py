import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.graph_objects as go

def generate_nightingale_chart():
    categorias = ['Electrónica', 'Ropa', 'Hogar', 'Juguetes', 'Deportes', 'Libros']
    ventas = np.random.randint(50, 200, size=len(categorias))
    
    fig = go.Figure()
    
    fig.add_trace(go.Barpolar(
        r=ventas,
        theta=[i * (360 / len(categorias)) for i in range(len(categorias))],
        width=[(360 / len(categorias)) * 0.8] * len(categorias),
        marker_color=ventas,
        marker_colorscale='Viridis',
        opacity=0.8
    ))
    
    fig.update_layout(
        title='Gráfico de Rosas de Nightingale - Ventas por Categoría',
        polar=dict(
            radialaxis=dict(showticklabels=True, ticks=''),
            angularaxis=dict(showticklabels=True, ticks='')
        ),
        showlegend=False
    )
    
    return fig

def generate_beeswarm_chart():
    # Generar datos de ejemplo
    np.random.seed(42)
    categorias = ['A', 'B', 'C', 'D']
    data = {
        'Categoría': np.random.choice(categorias, 300),
        'Valor': np.random.randn(300) + np.random.choice([0, 1, 2, 3], 300)
    }
    df = pd.DataFrame(data)

    # Crear el gráfico beeswarm
    plt.figure(figsize=(10, 6))
    sns.swarmplot(x='Categoría', y='Valor', data=df, palette='Set2')
    plt.title('Gráfico Beeswarm de Valores por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Valor')

    return plt.gcf()