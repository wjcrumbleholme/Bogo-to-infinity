import plotly.graph_objects as go

import flet as ft
from flet.plotly_chart import PlotlyChart


def main(page: ft.Page):

    page.title = "Bogo-to-infinity"
    page.window_height = 1024
    page.window_width = 1440


    fig = go.Figure()

    fig.add_trace(go.Box(
    x=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15,
       8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='.',
    boxpoints=False, # no data points
    marker_color='rgb(9,56,125)',
    line_color='rgb(9,56,125)'
    ))

    page.add(
        PlotlyChart(fig, expand=True)

        
        )

ft.app(target=main)