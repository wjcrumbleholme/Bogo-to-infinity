import plotly.graph_objects as go

import flet as ft
from flet.plotly_chart import PlotlyChart


def main(page: ft.Page):

    page.title = "Bogo-to-infinity"
    page.window_height = 1024
    page.window_width = 1440
    page.bgcolor="#BECEDA"
    page.fonts = {
        'Boldena' : "fonts/BoldenaBold.ttf"
    }

    boxPlot = go.Figure()

    boxPlot.add_trace(go.Box(
    x=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15,
       8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='.',
    boxpoints=False, # no data points
    marker_color='rgb(9,56,125)',
    line_color='rgb(9,56,125)',
    ))

    boxPlot.update_layout(
        autosize = False,
        width=1500,
        height=600,
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0,
            pad=1
        ),
        xaxis = dict(
        tickfont = dict(size=20)),
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_color="#FFFFFF",
        plot_bgcolor='rgba(0,0,0,0)',
    )
    boxPlot.update_xaxes(
        showline = True,
        linecolor = "White",
        gridcolor = 'White',
        gridwidth = 2,
    )

    barGraph = go.Figure()

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    barGraph.add_trace(go.Bar(
        y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
        name='Primary Product',
        marker_color='indianred'
    ))    
    barGraph.update_layout(
        autosize = False,
        width=1700,
        height=1000,
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0,
            pad=1
        ),
        xaxis = dict(
        tickfont = dict(size=20)),
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_color="#FFFFFF",
        plot_bgcolor='rgba(0,0,0,0)',
        bargap = 0,
    )
    barGraph.update_xaxes(
        showline = True,
        linecolor = "White",
        visible = False,
    )
    barGraph.update_yaxes(
        showline = False,
        showgrid = False,
        showticklabels = False,
    )


    def left_column(align: ft.CrossAxisAlignment):
        return ft.Column (
            [
            ft.Container(
                content=ft.Text("Bogo to Infinity", font_family="Boldena", size="48"),
                margin=2,
                padding=2,
                alignment=ft.alignment.Alignment(-0.9,0),
                bgcolor="#89A8BD",
                width=626,
                height=83,
                border_radius=10,
            ),
            ft.Container(
                content=PlotlyChart(barGraph,expand=True),
                margin=2,
                padding=2,
                alignment=ft.alignment.center,
                bgcolor="#89A8BD",
                width=875,
                height=526,
                border_radius=10,
            ),
            ft.Container(
                content=PlotlyChart(boxPlot,expand=True),
                margin=2,
                padding=2,
                alignment=ft.alignment.center,
                bgcolor="#89A8BD",
                width=875,
                height=320,
                border_radius=10,
            ),
            ]
        )
    
    def right_column(align: ft.CrossAxisAlignment):
        return ft.Column(
            [
            ft.Container(
                content=ft.Text("Bogo to Infinity", font_family="Boldena", size="48"),
                margin=2,
                padding=2,
                alignment=ft.alignment.center,
                bgcolor="#89A8BD",
                width=500,
                height=313,
                border_radius=10,
            ),
            ft.Container(
                content=ft.Text("Bogo to Infinity", font_family="Boldena", size="48"),
                margin=2,
                padding=2,
                alignment=ft.alignment.center,
                bgcolor="#89A8BD",
                width=500,
                height=671,
                border_radius=10,
            ),
            ]
        )

    page.add(
        ft.Row(
        [
            left_column(ft.CrossAxisAlignment.START),
            right_column(ft.CrossAxisAlignment.END),
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.START,
        ),

    )

ft.app(target=main)