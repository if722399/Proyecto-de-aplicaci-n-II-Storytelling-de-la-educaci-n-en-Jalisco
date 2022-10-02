import main as mn
import matplotlib.pyplot as plt
# import functions as fn
import seaborn as sns
import plotly.express as px
import unidecode
import pandas as pd
import streamlit as st



# Leyendo mapas
def map_viz(col):
    
    jalisco = mn.jalisco
    data = mn.data.copy()
    # Limpiando los mapas de Jalisco
    jalisco['NOMBRE'] = jalisco['NOMBRE'].apply(lambda x: unidecode.unidecode(x))

    # Reemplazando algunos caracteres del mapa de Jalisco
    ugly_dict = {'BOLAÃ\x83Â\x83Ã\x82Â\x83Ã\x83Â\x82Ã\x82Â\x91OS': 'BOLANOS',
            'CAÃ\x83Â\x83Ã\x82Â\x83Ã\x83Â\x82Ã\x82Â\x91ADAS DE OBREGON': 'CANADAS DE OBREGON',
            'SAN MARTIN DE BOLAÃ\x83Â\x83Ã\x82Â\x83Ã\x83Â\x82Ã\x82Â\x91OS': 'SAN MARTIN DE BOLANOS',
            'TLAJOMULCO DE ZUÃ\x83Â\x83Ã\x82Â\x83Ã\x83Â\x82Ã\x82Â\x91IGA': 'TLAJOMULCO DE ZUNIGA'}

    data['MUNICIPIO'].replace(ugly_dict, inplace=True)

    mean = data.groupby('MUNICIPIO').mean()[col]

    jalisco_merged = pd.merge(jalisco,mean, left_on='NOMBRE', right_index=True)

    # Colormap
    cmap='Oranges'
    fig, ax = plt.subplots(figsize = (10,10))
    ax.axis('off')

    vmin, vmax = data[col].min(),data[col].max()
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin,vmax=vmax))
    sm._A = []
    cbar = fig.colorbar(sm)

    jalisco_merged.plot(col,cmap,ax=ax);


import plotly.graph_objects as go
from plotly.subplots import make_subplots


def dax_viz(v1,v2,title):
        # Create figure with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])


        # Add traces
        fig.add_trace(
        go.Scatter(x=mn.df[title], y=mn.df[v1], name=str(v1)),
        secondary_y=False,
        )

        fig.add_trace(
        go.Scatter(x=mn.df[title], y=mn.df[v2], name=str(v2)),
        secondary_y=True,
        )

        # Add figure title
        fig.update_layout(
        title_text=f"Contrasting variable by {title}]",
        autosize=False,
        width=950,
        height=700
        )

        # Set x-axis title
        fig.update_xaxes(title_text="Municipios")

        # Set y-axes titles
        fig.update_yaxes(title_text=f"<b>{v1}</b> ", secondary_y=False)
        fig.update_yaxes(title_text=f"<b>{v2}</b>", secondary_y=True)

        return fig

