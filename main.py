import plotly.graph_objects as go
from timeit import default_timer as timer
import flet as ft
from flet.plotly_chart import PlotlyChart
from time import sleep
from random import shuffle


windowY = 720
windowX = 1280
aspectY = 900
aspectX = 1600
textRatio = ((windowX * windowY) / (aspectX * aspectY))

def main(page: ft.Page):
    page.light = ["#162127","#426276","#89A8BD","#BECEDA", "#2A2D34"]
    page.dark = ["#2A2D34", "#4A5F82", "#405763", "#2A2D34", "#FFFFFF"]
    page.colSchem = page.light

    #settings for the page
    page.title = "Bogo-to-infinity"
    page.window_height = windowY
    page.window_width = windowX
    page.window_resizable = True
    page.bgcolor=page.colSchem[3]
    page.fonts = {
        'Boldena' : "/fonts/BoldenaBold.ttf"
    }

    #----DARK MODE AND THEMES----#    

    def toggleDarkMode(e):
        page.darkButton.on_click = toggleLightMode
        page.darkButton.icon = ft.icons.LIGHT_MODE
        page.darkButton.icon_color = "#FFFFFF"
        page.darkButton.tooltip = "Toggle Light Mode"
        
        page.colSchem = page.dark
        
        updateColors()
        
    def toggleLightMode(e):
        page.darkButton.on_click = toggleDarkMode
        page.darkButton.icon=ft.icons.DARK_MODE
        page.darkButton.icon_color="#232528"
        page.darkButton.tooltip = "Toggle Dark Mode"

        page.colSchem = page.light
        updateColors()

    #This is utterly stupid and dumb
    def updateColors():
        page.bgcolor = page.colSchem[3]
        page.titleContainer.bgcolor = page.colSchem[2]
        page.barGraphContainerOuter.bgcolor = page.colSchem[1]
        page.barGraphContainerInner.bgcolor = page.colSchem[2]
        page.currTimeContainer.bgcolor = page.colSchem[2]
        page.noTriesContainer.bgcolor = page.colSchem[2]
        page.elapsedTimeContainer.bgcolor = page.colSchem[2]
        page.rightTopContainer.bgcolor = page.colSchem[1]
        page.prevValuesContainer.bgcolor = page.colSchem[2]
        page.dividerContainer.bgcolor = page.colSchem[0]
        page.box1Container.bgcolor = page.colSchem[2]
        page.box3Container.bgcolor = page.colSchem[2]
        page.box5Container.bgcolor = page.colSchem[2]
        page.box2Container.bgcolor = page.colSchem[2]
        page.box4Container.bgcolor = page.colSchem[2]
        page.box6Container.bgcolor = page.colSchem[2]
        page.bottomRightContainer.bgcolor = page.colSchem[1]
        page.titleText.color = page.colSchem[4]
        page.elapsedTimeText.color = page.colSchem[4]
        page.triesText.color = page.colSchem[4]
        page.currTimeText.color = page.colSchem[4]
        page.prevValuesText.color = page.colSchem[4]
        page.box1.color = page.colSchem[4]
        page.box2.color = page.colSchem[4]
        page.box3.color = page.colSchem[4]
        page.box4.color = page.colSchem[4]
        page.box5.color = page.colSchem[4]
        page.box6.color = page.colSchem[4]
        page.update()

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

    page.barGraphDisplay = PlotlyChart(barGraph,expand=True)
    page.titleText = ft.Text(f"Bogo to Infinity - 0", font_family = "Boldena", size= textRatio * 60, color= page.colSchem[4])
    page.elapsedTimeText = ft.Text("Total time - 00:00:00", font_family="Boldena", size= textRatio * 32, color= page.colSchem[4])
    page.triesText = ft.Text("Amount of tries - 0", font_family="Boldena", size= textRatio * 32, color= page.colSchem[4])
    page.currTimeText = ft.Text("Current sort time - 00:00:00", font_family="Boldena", size= textRatio * 32, color= page.colSchem[4])
    page.prevValuesText = ft.Text("Previous values", font_family="Boldena", size= textRatio * 60, color= page.colSchem[4])
    page.box1 = ft.Text("1", font_family="Boldena", size= textRatio * 32, color= page.colSchem[4])
    page.box2 = ft.Text("2", font_family="Boldena", size= textRatio * 32, color= page.colSchem[4])
    page.box3 = ft.Text("3", font_family="Boldena", size= textRatio * 32, color= page.colSchem[4])
    page.box4 = ft.Text("4", font_family="Boldena", size= textRatio * 32, color= page.colSchem[4])
    page.box5 = ft.Text("5", font_family="Boldena", size= textRatio * 32, color= page.colSchem[4])
    page.box6 = ft.Text("6", font_family="Boldena", size= textRatio * 32, color= page.colSchem[4])
    page.darkButton = ft.IconButton(
            icon=ft.icons.DARK_MODE,
            icon_color="#232528",
            selected_icon_color='#FFFFFF',
            icon_size=textRatio * 60,
            tooltip="Toggle Dark Mode",
            on_click=toggleDarkMode,
        )
    page.titleContainer = ft.Container(
            content=
            ft.Row([
                page.titleText,
                page.darkButton,
            ],
            spacing = 15,
            ),
            margin=2,
            padding=2,
            alignment=ft.alignment.Alignment(-0.9,0),
            bgcolor=page.colSchem[2],
            width= windowX/aspectX * 500,
            height= windowY/aspectY * 83,
            border_radius=10,
        )
    page.barGraphContainerInner = ft.Container(
            content=page.barGraphDisplay,
            margin=2,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=page.colSchem[2],
            width= windowX/aspectX * 1103,
            height= windowY/aspectY * 841,
            border_radius=10,
        )
    page.barGraphContainerOuter = ft.Container(
            content =  page.barGraphContainerInner,
            margin=2,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=page.colSchem[1],
            width= windowX/aspectX * 1136,
            height= windowY/aspectY * 891,
            border_radius=10,
        )
    page.currTimeContainer = ft.Container(
            content=page.currTimeText,
            margin=2,
            padding=2,
            alignment=ft.alignment.Alignment(-0.9,0),
            bgcolor=page.colSchem[2],
            width= windowX/aspectX * 594,
            height= windowY/aspectY * 83,
            border_radius=10,
        )
    page.noTriesContainer = ft.Container(
            content=page.triesText,
            margin=2,
            padding=2,
            alignment=ft.alignment.Alignment(-0.9,0),
            bgcolor=page.colSchem[2],
            width= windowX/aspectX * 594,
            height= windowY/aspectY * 83,
            border_radius=10,
        )
    page.elapsedTimeContainer = ft.Container(
            content=page.elapsedTimeText,
            margin=2,
            padding=2,
            alignment=ft.alignment.Alignment(-0.9,0),
            bgcolor=page.colSchem[2],
            width= windowX/aspectX * 594,
            height= windowY/aspectY * 83,
            border_radius=10,
        )
    page.rightTopContainer = ft.Container(
            content=
            ft.Column (
                [
                #current time box
                page.currTimeContainer,
                #no of tries box
                page.noTriesContainer,
                #elapsed time box
                page.elapsedTimeContainer,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            margin=2,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=page.colSchem[1],
            width= windowX/aspectX * 660,
            height= windowY/aspectY * 313,
            border_radius=10,
        )
    page.prevValuesContainer = ft.Container(
        content=page.prevValuesText,
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor=page.colSchem[2],
        width= windowX/aspectX * 450,
        height= windowY/aspectY * 100,
        border_radius=10,
        )
    page.dividerContainer = ft.Container(
            margin=2,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=page.colSchem[0],
            width= windowX/aspectX * 595,
            height= windowY/aspectY * 5,
            border_radius=10,
        )
    page.box1Container = ft.Container(
            content=page.box1,
            margin=2,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=page.colSchem[2],
            width= windowX/aspectX * 290,
            height= windowY/aspectY * 150,
            border_radius=10,
        )
    page.box3Container = ft.Container(
            content=page.box3,
            margin=2,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=page.colSchem[2],
            width= windowX/aspectX * 290,
            height= windowY/aspectY * 150,
            border_radius=10,
        )
    page.box5Container = ft.Container(
            content=page.box5,
            margin=2,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=page.colSchem[2],
            width= windowX/aspectX * 290,
            height= windowY/aspectY * 150,
            border_radius=10,
        )
    page.box2Container = ft.Container(
            content=page.box2,
            margin=2,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=page.colSchem[2],
            width= windowX/aspectX * 290,
            height= windowY/aspectY * 150,
            border_radius=10,
        )
    page.box4Container = ft.Container(
            content=page.box4,
            margin=2,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=page.colSchem[2],
            width= windowX/aspectX * 290,
            height= windowY/aspectY * 150,
            border_radius=10,
        )
    page.box6Container = ft.Container(
            content=page.box6,
            margin=2,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=page.colSchem[2],
            width= windowX/aspectX * 290,
            height= windowY/aspectY * 150,
            border_radius=10,
        )
    page.bottomRightContainer = ft.Container(
            content=
            ft.Column(
                [
                ft.Row(
                    [
                    #prev values box
                    page.prevValuesContainer,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                    #divider
                    page.dividerContainer,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.Column(
                            [
                            page.box1Container,
                            page.box3Container,
                            page.box5Container,
                            ]
                        ),
                        ft.Column(
                            [
                            page.box2Container,
                            page.box4Container,
                            page.box6Container,
                            ]
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ],
                alignment=ft.CrossAxisAlignment.CENTER,
            ),
            margin=2,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=page.colSchem[1],
            width= windowX/aspectX * 660,
            height= windowY/aspectY * 661,
            border_radius=10,
        )

    #----SCREEN STRUCTURE----#

    #left side
    def left_column(align: ft.CrossAxisAlignment):
        return ft.Column (
            [
            #title
            page.titleContainer,
            #bar chart
            page.barGraphContainerOuter,
            ]
        )
    
    #right side
    def right_column(align: ft.CrossAxisAlignment):
        return ft.Column(
            [
            page.rightTopContainer,
            page.bottomRightContainer,
            ],
        )
        
    #add all elements to the screen
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
    page.update()

    #---TIMING LOGIC---#

    startTime = timer()
    #calculates the total time
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
        page.elapsedTimeText.value = f"Total time - {hours}:{minutes}:{seconds}"
        page.elapsedTimeText.update()

    #calculates the time difference between 2 values
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
        
    #----SORT AND COLOR BARS LOGIC----#

    #checks if the list is sorted and if it is not, shuffles it again. 
    #also handles updating all of the display elements except prev values
    def sortChecker(list1, currNum):
        listSorted = False
        tries = 0
        thisTime = timer()
        while listSorted == False:
            listSorted = True
            for i in range(0, len(list1) - 1):
                if list1[i+1] < list1[i]:
                    listSorted = False
            tries += 1
            shuffle(list_shuffled)
            updateNoTries(tries)
            measuredTime = timer()
            currTime = timeDifference(measuredTime, thisTime)

            #runs every 10 tries to speed the program up from updating the display elements to quickly    
            if tries % 10 == 0:
                page.currTimeText.value = f"Current sort time - {currTime}"
                page.currTimeText.update()
                updateBarChart(list_shuffled,tries)
                page.barGraphDisplay.update()
                elapsedTime()
            else:
                pass
        storeInfo(currNum, tries, currTime)

    
    #find the difference between sorted and unsorted list
    #compare each value in the compared list with the number it is meant to be
    #if the compared number is zero, the number is in the right place and is coloured green
    #if compared number is within 25% range of the actual value it is coloured yellow
    #if compared number is within half the range of the actual value it is coloured orange
    #else number is coloured red
    def barColorList(list1):
        barColorList = []
        diff_list = []
        
        for i in range(0, len(list1)):
            diff_list.append(abs(list1[i] - (i+1)))
        
        for i in range(0, len(diff_list)):
            if diff_list[i] == 0:
                barColorList.append("#C5D86D")
            
            elif diff_list[i] < (len(diff_list) / 100) * 25:
                barColorList.append("#FADF7F")
            elif diff_list[i] < len(diff_list) / 2:
                barColorList.append("#FCAA67")
            else: 
                barColorList.append("#CC444B")
        return barColorList
        
    #----UPDATING ELEMENTS ON DISPLAY LOGIC----#   
        
    #updates the bar graph and colors it
    def updateBarChart(list2,tries):
        barGraph.update_traces(go.Bar(
            y=list2,
            marker_color = barColorList(list2),
        ))

    #updates the no of tries element
    def updateNoTries(tries):
        page.triesText.value = f"Number of tries: {tries}"
        page.triesText.update()

    #updates the title with the current number of values in the list it is sorting
    def updateTitleText(num):
        page.titleText.value = f"Bogo Sort - {num}"
        page.titleText.update()
    
    #after a successful sort, it is stored in a list with the number of values in the list, the list sort time and the number of tries
    prevResults = ['','','','','','']
    def storeInfo (currNum, tries, currTime):
        prevResults.insert(0,f"{currNum} values took:\n{currTime}\nTries: {tries}")

    #updates all the previous values boxes with the prev results stored in prevResults
    def updatePrevResults():
        page.box1.value = prevResults[0]
        page.box2.value = prevResults[1]
        page.box3.value = prevResults[2]
        page.box4.value = prevResults[3]
        page.box5.value = prevResults[4]
        page.box6.value = prevResults[5]
        page.update()

    #----INITIALIZATION AND MAIN LOOP LOGIC----#
    
    #takes in a length and makes a new list from 1 - length
    def makeNewList(length):
        global list_shuffled
        list_shuffled = list(range(1, length + 1))
        shuffle(list_shuffled)  

    #Responsible for making incrementing the number of values in the list, checking wether the list is sorted and updating the prev values and title text
    for i in range(2, 100):
        makeNewList(i)
        updateTitleText(i)
        sortChecker(list_shuffled, i)
        updatePrevResults()
    
ft.app(target=main, assets_dir="fonts")
#ft.app(target=main,port=8550,view=ft.WEB_BROWSER,assets_dir="fonts")


    