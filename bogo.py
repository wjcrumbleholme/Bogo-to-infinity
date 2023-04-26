import plotly.graph_objects as go
from timeit import default_timer as timer
import flet as ft
from flet.plotly_chart import PlotlyChart
from time import sleep
from random import shuffle


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



# global elapsedTimeText, titleText
elapsedTimeText = ft.Text("Total time - 00:00:00", font_family="Boldena")
titleText = ft.Text(f"Bogo Sort - 0", font_family = "Boldena")
triesText = ft.Text("Amount of tries - 0", font_family="Boldena")
currTimeText = ft.Text("Current sort time - 00:00:00", font_family="Boldena")
box1 = ft.Text("1", font_family="Boldena")
box2 = ft.Text("2", font_family="Boldena")
box3 = ft.Text("3", font_family="Boldena")
box4 = ft.Text("4", font_family="Boldena")
box5 = ft.Text("5", font_family="Boldena")
box6 = ft.Text("6", font_family="Boldena")
prevValuesText = ft.Text("Previous values", font_family="Boldena")
barGraphDisplay = PlotlyChart(barGraph,expand=True)

def topLeftContainer(sizeX, sizeY, sizeText, colSchem):
    titleText.size, titleText.color = sizeText * 50, colSchem[4]
    correctText = ft.Text("100% Correct", font_family= "Boldena", size= sizeText * 24, color = colSchem[8])
    closeText = ft.Text(">75% Correct", font_family= "Boldena", size= sizeText * 24, color = colSchem[7])
    mediumText = ft.Text("<75% Correct", font_family= "Boldena", size= sizeText * 24, color = colSchem[6])
    farText = ft.Text("<50% Correct", font_family= "Boldena", size= sizeText * 24, color = colSchem[5])
    titleContainer = ft.Container(
        content= titleText,
        margin=2,
        padding=2,
        alignment=ft.alignment.Alignment(-0.9,0),
        bgcolor=colSchem[2],
        width= sizeX * 500,
        height= sizeY * 83,
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
        width= sizeX * 350,
        height= sizeY * 83,
        border_radius=10,
    )


    container = ft.Row(
        [
        
        titleContainer,
        keyContainer,       
        ],
        spacing= 15
    )
    return container

def barGraphElement(sizeX, sizeY, sizeText, colSchem):
    barGraphDisplay = PlotlyChart(barGraph,expand=True)
    barGraphContainerInner = ft.Container(
            content=barGraphDisplay,
            margin=2,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=colSchem[2],
            width= sizeX * 1053,
            height= sizeY * 778,
            border_radius=10,
        )
    barGraphContainerOuter = ft.Container(
        content=barGraphContainerInner,
        margin=2,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=colSchem[1],
        width= sizeX * 1086,
        height= sizeY * 811,
        border_radius=10,
    )
    return barGraphContainerOuter

def rightTopContainer(sizeX, sizeY, sizeText, colSchem):
    elapsedTimeText.size, elapsedTimeText.color = sizeText * 28, colSchem[4]
    triesText.size, triesText.color = sizeText * 28, colSchem[4]
    currTimeText.size, currTimeText.color = sizeText * 28, colSchem[4]
    currTimeContainer = ft.Container(
        content=currTimeText,
        margin=2,
        padding=2,
        alignment=ft.alignment.Alignment(-0.9,0),
        bgcolor=colSchem[2],
        width= sizeX * 450,
        height= sizeY * 83,
        border_radius=10,
    )
    noTriesContainer = ft.Container(
        content=triesText,
        margin=2,
        padding=2,
        alignment=ft.alignment.Alignment(-0.9,0),
        bgcolor=colSchem[2],
        width= sizeX * 450,
        height= sizeY * 83,
        border_radius=10,
    )
    elapsedTimeContainer = ft.Container(
        content=elapsedTimeText,
        margin=2,
        padding=2,
        alignment=ft.alignment.Alignment(-0.9,0),
        bgcolor=colSchem[2],
        width= sizeX * 450,
        height= sizeY * 83,
        border_radius=10,
    )
    container = ft.Container(
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
            width= sizeX * 480,
            height= sizeY * 313,
            border_radius=10,
        )
    return container

def bottomRightContainer(sizeX, sizeY, sizeText, colSchem):
    prevValuesText.size, prevValuesText.color = sizeText * 40, colSchem[4] 
    box1.size, box1.color = sizeText * 20, colSchem[4]
    box2.size, box2.color = sizeText * 20, colSchem[4]
    box3.size, box3.color = sizeText * 20, colSchem[4]
    box4.size, box4.color = sizeText * 20, colSchem[4]
    box5.size, box5.color = sizeText * 20, colSchem[4]
    box6.size, box6.color = sizeText * 20, colSchem[4]
    prevValuesContainer = ft.Container(
    content=prevValuesText,
    margin=2,
    padding=2,
    alignment=ft.alignment.center,
    bgcolor=colSchem[2],
    width= sizeX * 350,
    height= sizeY * 100,
    border_radius=10,
    )
    dividerContainer = ft.Container(
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[0],
        width= sizeX * 415,
        height= sizeY * 5,
        border_radius=10,
    )
        
    box1Container = ft.Container(
        content=box1,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= sizeX * 210,
        height= sizeY * 110,
        border_radius=10,
    )
    box3Container = ft.Container(
        content=box3,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= sizeX * 210,
        height= sizeY * 110,
        border_radius=10,
    )
    box5Container = ft.Container(
        content=box5,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= sizeX * 210,
        height= sizeY * 110,
        border_radius=10,
    )
    box2Container = ft.Container(
        content=box2,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= sizeX * 210,
        height= sizeY * 110,
        border_radius=10,
    )
    box4Container = ft.Container(
        content=box4,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= sizeX * 210,
        height= sizeY * 110,
        border_radius=10,
    )
    box6Container = ft.Container(
        content=box6,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=colSchem[2],
        width= sizeX * 210,
        height= sizeY * 110,
        border_radius=10,
    )
    container= ft.Container(
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
            alignment=ft.MainAxisAlignment.START,
        ),
        margin=2,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=colSchem[1],
        width= sizeX * 480,
        height= sizeY * 580,
        border_radius=10,
    )
    return container
    


barColorSchem = []
#----SCREEN STRUCTURE----#
def sendElementsToOtherFile(sizeX, sizeY, sizeText, colSchem):
    global barColorSchem
    barColorSchem = colSchem 
    bogoContainer = ft.Row(
        [
            ft.Column (
            [
            #title
            topLeftContainer(sizeX, sizeY, sizeText, colSchem),
            #bar chart
            barGraphElement(sizeX, sizeY, sizeText, colSchem),
            ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Column(
            [
            rightTopContainer(sizeX, sizeY, sizeText, colSchem),
            bottomRightContainer(sizeX, sizeY, sizeText, colSchem),
            ],
            alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    return bogoContainer

def makeNewList(length):
    global list_shuffled
    list_shuffled = list(range(1, length + 1))
    shuffle(list_shuffled) 


def updatePrevResults():
    box1.value = prevResults[0]
    box2.value = prevResults[1]
    box3.value = prevResults[2]
    box4.value = prevResults[3]
    box5.value = prevResults[4]
    box6.value = prevResults[5]
    box1.update()
    box2.update()
    box3.update()
    box4.update()
    box5.update()
    box6.update()
        

prevResults = ['','','','','','']
def storeInfo (currNum, tries, currTime):
    prevResults.insert(0,f"{currNum} values took:\n{currTime}\nTries: {tries}")

def updateBarChart(list,tries):
    barGraph.update_traces(go.Bar(
        y=list,
        marker_color = barColorList(list),
    ))

def barColorList(list):
        global barColorSchem
        barColorList = []
        diff_list = []
        
        for i in range(0, len(list)):
            diff_list.append(abs(list[i] - (i+1)))
        
        for i in range(0, len(diff_list)):
            if diff_list[i] == 0:
                barColorList.append(barColorSchem[8])
            
            elif diff_list[i] < (len(diff_list) / 100) * 25:
                barColorList.append(barColorSchem[7])
            elif diff_list[i] < len(diff_list) / 2:
                barColorList.append(barColorSchem[6])
            else: 
                barColorList.append(barColorSchem[5])
        return barColorList
    
def timeDifference(time1, time2):
    total = time1 - time2
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
    return f"{hours}:{minutes}:{seconds}"

def elapsedTime(startTime):
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