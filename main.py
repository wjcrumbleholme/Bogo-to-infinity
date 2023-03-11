import plotly.graph_objects as go
from timeit import default_timer as timer
import flet as ft
from flet.plotly_chart import PlotlyChart
from time import sleep
from random import shuffle

titleText = ft.Text(f"Bogo to Infinity - 0", font_family="Boldena", size="48")
elapsedTimeText = ft.Text("Total time - 00:00:00", font_family="Boldena", size="32")
triesText = ft.Text("Amount of tries - 0", font_family="Boldena", size="32")

def main(page: ft.Page):

    page.title = "Bogo-to-infinity"
    page.window_height = 1024
    page.window_width = 1440
    page.window_resizable = False
    page.bgcolor="#BECEDA"
    page.fonts = {
        'Boldena' : "fonts/BoldenaBold.ttf"
    }

    currentNum = 0

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
    
    barGraph.add_trace(go.Bar(
        y=[1,2,3],
        name='Primary Product',
        marker_color='indianred',
    ))   
    barGraph.update_layout(
        autosize = False,
        width=1500,
        height=900,
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
                content=titleText,
                margin=2,
                padding=2,
                alignment=ft.alignment.Alignment(-0.9,0),
                bgcolor="#89A8BD",
                width=626,
                height=83,
                border_radius=10,
            ),
            ft.Container(
                content = 
                    ft.Container(
                    content=PlotlyChart(barGraph,expand=True),
                    margin=2,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor="#89A8BD",
                    width=850,
                    height=501,
                    border_radius=10,
                ),
                margin=2,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor="#426276",
                width=875,
                height=526,
                border_radius=10,
            ),
            ft.Container(
                content =
                ft.Container(
                    content=PlotlyChart(boxPlot,expand=True),
                    margin=2,
                    padding=5,
                    alignment=ft.alignment.center,
                    bgcolor="#89A8BD",
                    width=850,
                    height=295,
                    border_radius=10,
                ),
                margin=2,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor="#426276",
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
                content=
                ft.Column (
                    [
                    ft.Container(
                        content=ft.Text("Current sort time - 00:00:00", font_family="Boldena", size="32"),
                        margin=2,
                        padding=2,
                        alignment=ft.alignment.Alignment(-0.9,0),
                        bgcolor="#426276",
                        width=450,
                        height=83,
                        border_radius=10,
                    ),
                    ft.Container(
                        content=triesText,
                        margin=2,
                        padding=2,
                        alignment=ft.alignment.Alignment(-0.9,0),
                        bgcolor="#426276",
                        width=450,
                        height=83,
                        border_radius=10,
                    ),
                    ft.Container(
                        content=elapsedTimeText,
                        margin=2,
                        padding=2,
                        alignment=ft.alignment.Alignment(-0.9,0),
                        bgcolor="#426276",
                        width=450,
                        height=83,
                        border_radius=10,
                    ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                margin=2,
                padding=2,
                alignment=ft.alignment.center,
                bgcolor="#89A8BD",
                width=500,
                height=313,
                border_radius=10,
            ),
            ft.Container(
                content=
                ft.Column(
                    [
                    ft.Row(
                        [
                        ft.Container(
                        content=ft.Text("Previous times", font_family="Boldena", size="64"),
                        margin=2,
                        padding=2,
                        alignment=ft.alignment.center,
                        bgcolor="#426276",
                        width=450,
                        height=100,
                        border_radius=10,
                        ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                        ft.Container(
                            margin=2,
                            padding=2,
                            alignment=ft.alignment.center,
                            bgcolor="#162127",
                            width=450,
                            height=5,
                            border_radius=10,
                        ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                        ft.Column(
                                [
                                    ft.Container(
                                        content=ft.Text("1", font_family="Boldena", size="32"),
                                        margin=2,
                                        padding=2,
                                        alignment=ft.alignment.center,
                                        bgcolor="#426276",
                                        width=220,
                                        height=150,
                                        border_radius=10,
                                        ),
                                    ft.Container(
                                        content=ft.Text("2", font_family="Boldena", size="32"),
                                        margin=2,
                                        padding=2,
                                        alignment=ft.alignment.center,
                                        bgcolor="#426276",
                                        width=220,
                                        height=150,
                                        border_radius=10,
                                        ),
                                    ft.Container(
                                        content=ft.Text("3", font_family="Boldena", size="32"),
                                        margin=2,
                                        padding=2,
                                        alignment=ft.alignment.center,
                                        bgcolor="#426276",
                                        width=220,
                                        height=150,
                                        border_radius=10,
                                        ),
                                ]
                            ),
                        ft.Column(
                                [
                                    ft.Container(
                                        content=ft.Text("4", font_family="Boldena", size="32"),
                                        margin=2,
                                        padding=2,
                                        alignment=ft.alignment.center,
                                        bgcolor="#426276",
                                        width=220,
                                        height=150,
                                        border_radius=10,
                                        ),
                                    ft.Container(
                                        content=ft.Text("5", font_family="Boldena", size="32"),
                                        margin=2,
                                        padding=2,
                                        alignment=ft.alignment.center,
                                        bgcolor="#426276",
                                        width=220,
                                        height=150,
                                        border_radius=10,
                                        ),
                                    ft.Container(
                                        content=ft.Text("6", font_family="Boldena", size="32"),
                                        margin=2,
                                        padding=2,
                                        alignment=ft.alignment.center,
                                        bgcolor="#426276",
                                        width=220,
                                        height=150,
                                        border_radius=10,
                                        ),
                                ],
                                
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                    ], 
                    alignment=ft.CrossAxisAlignment.CENTER,
                ),
                margin=2,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor="#89A8BD",
                width=500,
                height=630,
                border_radius=10,
            ),
            ],
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

    startTime = timer()
    def elapsedTime():
        endTime= timer()
        total = endTime - startTime
        seconds = total % 60
        minutes = total // 60
        hours = total // 3600
        if seconds < 10:
            seconds = f"0{int(seconds)}"
        else:
            seconds= int(seconds)
        if minutes < 10:
            minutes = f"0{int(minutes)}"
        else:
            minutes = int(minutes)
        if hours < 10:
            hours = f"0{int(hours)}"
        else:
            hours = int(hours)
        elapsedTimeText.value = f"Total time - {hours}:{minutes}:{seconds}"
        page.update()

    def makeNewList(length):
        global list_shuffled
        list_shuffled = list(range(1, length + 1))
        shuffle(list_shuffled)  

    def sortChecker(list1):
        listSorted = False
        tries = 0
        while listSorted == False:
            listSorted = True
            for i in range(0, len(list1) - 1):
                if list1[i+1] < list1[i]:
                    listSorted = False
                    tries += 1
            updateBarChart(list_shuffled)
            shuffle(list_shuffled)
            elapsedTime()
            updateNoTries(tries)

    
    def updateBarChart(list2):
        barGraph.update_traces(go.Bar(
            y=list2,
            name='Primary Product',
            marker_color='indianred',
        ))   
        page.update()

    def updateNoTries(tries):
        triesText.value = f"Number of tries: {tries}"
        page.update()

    
    makeNewList(10)
    sortChecker(list_shuffled)



ft.app(target=main)


    