import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.graph_objects as go

def generate_nightingale_chart():
    meses = ['Enero 2025', 'Febrero 2025', 'Marzo 2025', 'Abril 2025', 'Mayo 2025', 'Junio 2025']
    canales = ['SEO', 'SEM', 'Email', 'Social Media', 'Afiliados']
    
    data = np.random.randint(20, 150, size=(len(meses), len(canales)))
    df = pd.DataFrame(data, index=meses, columns=canales)
    
    fig = go.Figure()
    for canal in df.columns:
        fig.add_trace(go.Barpolar(
            r=df[canal],
            theta=df.index,
            name=canal,
            hovertemplate=(
                "<b>Mes</b>: %{theta}<br>" +
                "<b>Canal</b>: %{fullData.name}<br>" +
                "<b>Inversión</b>: %{r:,.0f}€" +
                "<extra></extra>"
            )
        ))

    fig.update_layout(
        template='plotly_dark',
        title='Inversión de Marketing Digital por Canal y Mes',
        showlegend=True,
        legend_title_text='Canales de Marketing',
        polar=dict(
            radialaxis=dict(
                showticklabels=True, 
                ticks='outside',
                title='Inversión Total (M€)',
                tickangle=45,
            ),
            angularaxis=dict(
                showticklabels=True, 
                ticks='outside',
                direction='clockwise'
            ),
        )
    )
    
    return fig

def generate_beeswarm_chart():
    
    np.random.seed(42)
    
    n_puntos_por_region = 200
    regiones = ['EEUU-Este', 'Europa-Oeste', 'Asia-Pacífico', 'Latinoamérica']
    datos_lista = []
    perfiles = {
        'EEUU-Este':     {'media': 80, 'std': 20},
        'Europa-Oeste':  {'media': 110, 'std': 30},
        'Asia-Pacífico': {'media': 180, 'std': 40},
        'Latinoamérica': {'media': 150, 'std': 55}
    }
    
    for region in regiones:
        tiempos = np.random.normal(
            loc=perfiles[region]['media'],
            scale=perfiles[region]['std'],
            size=n_puntos_por_region
        )
        
        tiempos = np.maximum(tiempos, 15)
        for t in tiempos:
            datos_lista.append({'Región': region, 'Tiempo de Respuesta (ms)': t})
            
    df = pd.DataFrame(datos_lista)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.swarmplot(
        x='Región', 
        y='Tiempo de Respuesta (ms)', 
        data=df, 
        ax=ax,
        palette='viridis',
        alpha=0.7,
        s=4 
    )
    
    ax.set_title('Distribución de Tiempos de Respuesta por Región del Servidor', fontsize=16, pad=20)
    ax.set_xlabel('Región del Servidor', fontsize=12)
    ax.set_ylabel('Tiempo de Respuesta (ms)', fontsize=12)
    ax.yaxis.grid(True, linestyle='--', alpha=0.5)
    sns.despine(trim=True)
    
    return fig