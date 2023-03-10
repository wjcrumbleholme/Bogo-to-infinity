import plotly.graph_objects as go

import flet as ft
from flet.plotly_chart import PlotlyChart


def main(page: ft.Page):

    fig = go.Figure()

    fig = go.Figure()
    fig.add_trace(go.Box(
        y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15,
        8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
        name="All Points",
        jitter=0.3,
        pointpos=-1.8,
        boxpoints='all', # represent all points
        marker_color='rgb(7,40,89)',
        line_color='rgb(7,40,89)'
    ))

    page.add(PlotlyChart(fig, expand=True))

ft.app(target=main,view=ft.WEB_BROWSER)