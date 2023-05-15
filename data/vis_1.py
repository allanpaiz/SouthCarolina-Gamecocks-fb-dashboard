import pandas as pd
import plotly.graph_objects as go
import numpy as np
import base64
from flask import jsonify
from data_main import schedule_ranking_data, load_raw_data


def create_main_scatter():
    data = load_raw_data('C:/Users/allan/OneDrive/Documents/00LIFE/Projects/GameCocks/data/raw_data.json')
    raw_df = schedule_ranking_data(data)
    df = raw_df.dropna()

    scatter_1 = go.Figure()

    # Set the axis range
    scatter_1.update_xaxes(range=[min(df['Points For']) - 50, max(df['Points For']) + 50])
    scatter_1.update_yaxes(range=[max(df['Points Against']) + 50, min(df['Points Against']) - 50])

    # Update layout and axes
    scatter_1.update_layout(
        title={
            'text': "Points For vs Points Against : 2022 Season",
            'y': 0.95, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top',
            'font': {'size': 24}
        },
        xaxis_title="Points For",
        yaxis_title="Points Against",
        xaxis=dict(title_font=dict(size=18), showgrid=True, gridwidth=1, gridcolor='rgba(255, 255, 255, 0.1)'),
        yaxis=dict(title_font=dict(size=18), showgrid=True, gridwidth=1, gridcolor='rgba(255, 255, 255, 0.1)'),
        plot_bgcolor='rgba(10, 10, 10, 1)',
        paper_bgcolor='rgba(10, 10, 10, 1)',
        font=dict(family="Arial", size=14, color="white")
    )

    # Define annotations
    annotations = [
        dict(text="Furman & JSU not shown", x=0.98, y=0.45, xref="paper", yref="paper",
            showarrow=False, font=dict(size=14, color="white"),
            bgcolor="rgba(50, 50, 50, 0.5)", bordercolor="white", borderwidth=1, opacity=0.5),
        dict(text="Poor Defense, Poor Offense", x=0.05, y=0.05, xref="paper", yref="paper",
            showarrow=False, font=dict(size=14, color="white"),
            bgcolor="rgba(240, 10, 10, 1)", bordercolor="white", borderwidth=1, opacity=1),
        dict(text="Poor Defense, Better Offense", x=0.95, y=0.05, xref="paper", yref="paper",
            showarrow=False, font=dict(size=14, color="white"),
            bgcolor="rgba(210, 100, 10, 1)", bordercolor="white", borderwidth=1, opacity=1),
        dict(text="Better Defense, Poor Offense", x=0.05, y=0.95, xref="paper", yref="paper",
            showarrow=False, font=dict(size=14, color="white"),
            bgcolor="rgba(210, 100, 10, 1)", bordercolor="white", borderwidth=1, opacity=1),
        dict(text="Better Defense, Better Offense", x=0.95, y=0.95, xref="paper", yref="paper",
            showarrow=False, font=dict(size=14, color="white"),
            bgcolor="rgba(30, 190, 50, 1)", bordercolor="white", borderwidth=1, opacity=1
        )
    ]

    # Add annotations to the layout
    scatter_1.update_layout(annotations=annotations)

    # Create a scatter plot with custom images as data points
    for index, row in df.iterrows():
        # Read image and convert to base64
        image_filename = f"C:/Users/allan/OneDrive/Documents/00LIFE/Projects/GameCocks/logos/{row['Team Name'].lower().replace(' ', '_')}_logo.png"
        encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')

        scatter_1.add_layout_image(
            dict(
                source=f"data:image/png;base64,{encoded_image}",
                x=row['Points For'],
                y=row['Points Against'],
                sizex=40,
                sizey=40,
                xanchor="center",
                yanchor="middle",
                xref="x",
                yref="y",
                sizing="contain",
                opacity=0.8,
                layer="above"
            )
        )

        # Add hover text
        scatter_1.add_trace(
            go.Scatter(
                x=[row['Points For']],
                y=[row['Points Against']],
                text=[f"{row['Team Name']}<br>Points For: {row['Points For']}<br>Points Against: {row['Points Against']}"],
                mode="text",
                hoverinfo="text",
                textposition="bottom center",
                showlegend=False,
                textfont=dict(size=1, color="black")  # Set text size to 1 to make it very small, effectively invisible
            )
        )

    # Add dashed lines for average Points per game and Points allowed per game
    scatter_1.add_shape(type='line', x0=np.mean(df['Points For']), x1=np.mean(df['Points For']),
                        y0=scatter_1.layout.yaxis.range[0], y1=scatter_1.layout.yaxis.range[1],
                        yref='y', xref='x', line=dict(color='white', dash='longdash'))
    scatter_1.add_shape(type='line', y0=np.mean(df['Points Against']), y1=np.mean(df['Points Against']),
                        x0=scatter_1.layout.xaxis.range[0], x1=scatter_1.layout.xaxis.range[1],
                        yref='y', xref='x', line=dict(color='white', dash='longdash'))
    
    return scatter_1.to_json()