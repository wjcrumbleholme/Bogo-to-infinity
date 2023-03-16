import plotly.graph_objects as go
from timeit import default_timer as timer
import flet as ft
from flet.plotly_chart import PlotlyChart
from time import sleep
from random import shuffle
import os



#----COLORS----#
# FORMAT: [Divider color, Container border color, Container color, Background color,  Text color, Far bar, Medium bar, Close bar, Actual bar]
light = ["#BDCDD6","#6096B4","#93BFCF","#BDCDD6", "#2C3333", "#FF6363", "#FFAB76", "#FFFDA2", "#BAFFB4"]
dark = ["#2C3333", "#2E4F4F", "#0E8388", "#2C3333", "#CBE4DE", "#37306B", "#66347F", "#9E4784", "#D27685"]
colSchem = light

windowY = 954
windowX = 1672
aspectY = 900
aspectX = 1600
textRatio = ((windowX * windowY) / (aspectX * aspectY))


#settings for the     title = "Bogo-to-infinity"
window_height = windowY
window_width = windowX
window_resizable = True
window_maximized = True
window_full_screen = True
bgcolor=colSchem[3]
fonts = {
    'Boldena' : "/fonts/BoldenaBold.ttf"
}

#----DARK MODE AND THEMES----#    

def toggleDarkMode(e):
    darkButton.on_click = toggleLightMode
    darkButton.icon = ft.icons.LIGHT_MODE
    darkButton.icon_color = "#FFFFFF"
    darkButton.tooltip = "Toggle Light Mode"
    
    colSchem = dark
    updateColors()
    
def toggleLightMode(e):
    darkButton.on_click = toggleDarkMode
    darkButton.icon=ft.icons.DARK_MODE
    darkButton.icon_color="#232528"
    darkButton.tooltip = "Toggle Dark Mode"

    colSchem = light
    updateColors()

def closeApp(e):
    os._exit(1)

#This is utterly stupid and dumb
def updateColors():
    bgcolor = colSchem[3]
    titleContainer.bgcolor = colSchem[2]
    barGraphContainerOuter.bgcolor = colSchem[1]
    barGraphContainerInner.bgcolor = colSchem[2]
    currTimeContainer.bgcolor = colSchem[2]
    noTriesContainer.bgcolor = colSchem[2]
    elapsedTimeContainer.bgcolor = colSchem[2]
    rightTopContainer.bgcolor = colSchem[1]
    prevValuesContainer.bgcolor = colSchem[2]
    dividerContainer.bgcolor = colSchem[0]
    box1Container.bgcolor = colSchem[2]
    box3Container.bgcolor = colSchem[2]
    box5Container.bgcolor = colSchem[2]
    box2Container.bgcolor = colSchem[2]
    box4Container.bgcolor = colSchem[2]
    box6Container.bgcolor = colSchem[2]
    bottomRightContainer.bgcolor = colSchem[1]
    titleText.color = colSchem[4]
    elapsedTimeText.color = colSchem[4]
    triesText.color = colSchem[4]
    currTimeText.color = colSchem[4]
    prevValuesText.color = colSchem[4]
    box1.color = colSchem[4]
    box2.color = colSchem[4]
    box3.color = colSchem[4]
    box4.color = colSchem[4]
    box5.color = colSchem[4]
    box6.color = colSchem[4]
    darkButtonContainer.bgcolor = colSchem[2]
    exitButtonContainer.bgcolor = colSchem[2]
    keyContainer.bgcolor = colSchem[2]
    correctText.color = colSchem[8]
    closeText.color = colSchem[7]
    mediumText.color = colSchem[6]
    farText.color = colSchem[5]


#----BAR CHART----#

barGraph = go.Figure()

barGraph.add_trace(go.Bar(
    y=[1,2,3],
    name='Primary Product',
    marker_color='indianred',
))   
#bar chart settings
barGraph.update_layout(
    autosize = True,
    # width= aspectX * 100,
    # height= aspectY * 100,
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

#----ALL ELEMENTS ON THE SCREEN---#

barGraphDisplay = PlotlyChart(barGraph,expand=True)
titleText = ft.Text(f"Bogo Sort - 0", font_family = "Boldena", size= textRatio * 50, color= colSchem[4])
elapsedTimeText = ft.Text("Total time - 00:00:00", font_family="Boldena", size= textRatio * 32, color= colSchem[4])
triesText = ft.Text("Amount of tries - 0", font_family="Boldena", size= textRatio * 32, color= colSchem[4])
currTimeText = ft.Text("Current sort time - 00:00:00", font_family="Boldena", size= textRatio * 32, color= colSchem[4])
prevValuesText = ft.Text("Previous values", font_family="Boldena", size= textRatio * 50, color= colSchem[4])
box1 = ft.Text("1", font_family="Boldena", size= textRatio * 32, color= colSchem[4])
box2 = ft.Text("2", font_family="Boldena", size= textRatio * 32, color= colSchem[4])
box3 = ft.Text("3", font_family="Boldena", size= textRatio * 32, color= colSchem[4])
box4 = ft.Text("4", font_family="Boldena", size= textRatio * 32, color= colSchem[4])
box5 = ft.Text("5", font_family="Boldena", size= textRatio * 32, color= colSchem[4])
box6 = ft.Text("6", font_family="Boldena", size= textRatio * 32, color= colSchem[4])
correctText = ft.Text("100% Correct", font_family= "Boldena", size= textRatio * 24, color = colSchem[8])
closeText = ft.Text(">75% Correct", font_family= "Boldena", size= textRatio * 24, color = colSchem[7])
mediumText = ft.Text("<75% Correct", font_family= "Boldena", size= textRatio * 24, color = colSchem[6])
farText = ft.Text("<50% Correct", font_family= "Boldena", size= textRatio * 24, color = colSchem[5])
darkButton = ft.IconButton(
        icon=ft.icons.DARK_MODE,
        icon_color="#232528",
        selected_icon_color='#FFFFFF',
        icon_size=textRatio * 40,
        tooltip="Toggle Dark Mode",
        on_click=toggleDarkMode,
    )
exitButton = ft.IconButton(
        icon=ft.icons.EXIT_TO_APP,
        icon_color="red",
        selected_icon_color='#FFFFFF',
        icon_size=textRatio * 40,
        tooltip="Exit",
        on_click=closeApp,
    )
darkButtonContainer = ft.Container(
        content= darkButton,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= windowX/aspectX * 83,
        height= windowY/aspectY * 83,
        border_radius=10,
    )
exitButtonContainer = ft.Container(
        content= exitButton,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= windowX/aspectX * 83,
        height= windowY/aspectY * 83,
        border_radius=10,
    )
keyContainer = ft.Container(
        content= 
        ft.Row([
            ft.Column([
                correctText,
                mediumText,
            ],
            spacing = 1,
            alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Column([
                closeText,
                farText,
            ],
            spacing = 1,
            alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= windowX/aspectX * 350,
        height= windowY/aspectY * 83,
        border_radius=10,
    )
titleContainer = ft.Container(
        content= titleText,
        margin=2,
        padding=2,
        alignment=ft.alignment.Alignment(-0.9,0),
        bgcolor=colSchem[2],
        width= windowX/aspectX * 500,
        height= windowY/aspectY * 83,
        border_radius=10,
    )
topLeftContainer = ft.Row(
    [
    
    titleContainer,
    keyContainer,
    darkButtonContainer,
    exitButtonContainer,
    
    ],
    spacing= 15
)
barGraphContainerInner = ft.Container(
        content=barGraphDisplay,
        margin=2,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= windowX/aspectX * 1103,
        height= windowY/aspectY * 841,
        border_radius=10,
    )
barGraphContainerOuter = ft.Container(
        content =  barGraphContainerInner,
        margin=2,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=colSchem[1],
        width= windowX/aspectX * 1136,
        height= windowY/aspectY * 891,
        border_radius=10,
    )
currTimeContainer = ft.Container(
        content=currTimeText,
        margin=2,
        padding=2,
        alignment=ft.alignment.Alignment(-0.9,0),
        bgcolor=colSchem[2],
        width= windowX/aspectX * 594,
        height= windowY/aspectY * 83,
        border_radius=10,
    )
noTriesContainer = ft.Container(
        content=triesText,
        margin=2,
        padding=2,
        alignment=ft.alignment.Alignment(-0.9,0),
        bgcolor=colSchem[2],
        width= windowX/aspectX * 594,
        height= windowY/aspectY * 83,
        border_radius=10,
    )
elapsedTimeContainer = ft.Container(
        content=elapsedTimeText,
        margin=2,
        padding=2,
        alignment=ft.alignment.Alignment(-0.9,0),
        bgcolor=colSchem[2],
        width= windowX/aspectX * 594,
        height= windowY/aspectY * 83,
        border_radius=10,
    )
rightTopContainer = ft.Container(
        content=
        ft.Column (
            [
            #current time box
            currTimeContainer,
            #no of tries box
            noTriesContainer,
            #elapsed time box
            elapsedTimeContainer,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[1],
        width= windowX/aspectX * 660,
        height= windowY/aspectY * 313,
        border_radius=10,
    )
prevValuesContainer = ft.Container(
    content=prevValuesText,
    margin=2,
    padding=2,
    alignment=ft.alignment.center,
    bgcolor=colSchem[2],
    width= windowX/aspectX * 450,
    height= windowY/aspectY * 100,
    border_radius=10,
    )
dividerContainer = ft.Container(
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[0],
        width= windowX/aspectX * 595,
        height= windowY/aspectY * 5,
        border_radius=10,
    )
box1Container = ft.Container(
        content=box1,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= windowX/aspectX * 300,
        height= windowY/aspectY * 150,
        border_radius=10,
    )
box3Container = ft.Container(
        content=box3,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= windowX/aspectX * 300,
        height= windowY/aspectY * 150,
        border_radius=10,
    )
box5Container = ft.Container(
        content=box5,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= windowX/aspectX * 300,
        height= windowY/aspectY * 150,
        border_radius=10,
    )
box2Container = ft.Container(
        content=box2,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= windowX/aspectX * 300,
        height= windowY/aspectY * 150,
        border_radius=10,
    )
box4Container = ft.Container(
        content=box4,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= windowX/aspectX * 300,
        height= windowY/aspectY * 150,
        border_radius=10,
    )
box6Container = ft.Container(
        content=box6,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= windowX/aspectX * 300,
        height= windowY/aspectY * 150,
        border_radius=10,
    )
bottomRightContainer = ft.Container(
        content=
        ft.Column(
            [
            ft.Row(
                [
                #prev values box
                prevValuesContainer,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                #divider
                dividerContainer,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.Column(
                        [
                        box1Container,
                        box3Container,
                        box5Container,
                        ]
                    ),
                    ft.Column(
                        [
                        box2Container,
                        box4Container,
                        box6Container,
                        ]
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        margin=2,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=colSchem[1],
        width= windowX/aspectX * 660,
        height= windowY/aspectY * 661,
        border_radius=10,
    )

#----SCREEN STRUCTURE----#
bogoContainer = ft.Row(
    [
        ft.Column (
        [
        #title
        topLeftContainer,
        #bar chart
        barGraphContainerOuter,
        ],
        ),
        ft.Column(
        [
        rightTopContainer,
        bottomRightContainer,
        ],
        )
    ]
)

#left side
def left_column(align: ft.CrossAxisAlignment):
    return ft.Column (
        [
        #title
        topLeftContainer,
        #bar chart
        barGraphContainerOuter,
        ]
    )

#right side
def right_column(align: ft.CrossAxisAlignment):
    return ft.Column(
        [
        rightTopContainer,
        bottomRightContainer,
        ],
    )
    
#add all elements to the screen

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
    return f"Total time - {hours}:{minutes}:{seconds}"