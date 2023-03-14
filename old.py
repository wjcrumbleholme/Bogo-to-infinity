import plotly.graph_objects as go
from timeit import default_timer as timer
import flet as ft
from flet.plotly_chart import PlotlyChart
from time import sleep
from random import shuffle


def main(page: ft.Page):

    #settings for the page
    page.title = "Bogo-to-infinity"
    page.window_height = 1024
    page.window_width = 1440
    page.window_resizable = True
    page.bgcolor="#BECEDA"
    page.fonts = {
        'Boldena' : "fonts/BoldenaBold.ttf"
    }

    #all text fields in the page that are changed
    page.titleText = ft.Text(f"Bogo to Infinity - 0", font_family="Boldena", size="48")
    page.elapsedTimeText = ft.Text("Total time - 00:00:00", font_family="Boldena", size="32")
    page.triesText = ft.Text("Amount of tries - 0", font_family="Boldena", size="32")
    page.currTimeText = ft.Text("Current sort time - 00:00:00", font_family="Boldena", size="32")
    page.box1 = ft.Text("1", font_family="Boldena", size="24")
    page.box2 = ft.Text("2", font_family="Boldena", size="24")
    page.box3 = ft.Text("3", font_family="Boldena", size="24")
    page.box4 = ft.Text("4", font_family="Boldena", size="24")
    page.box5 = ft.Text("5", font_family="Boldena", size="24")
    page.box6 = ft.Text("6", font_family="Boldena", size="24")

    #create bar chart
    barGraph = go.Figure()
    
    barGraph.add_trace(go.Bar(
        y=[1,2,3],
        name='Primary Product',
        marker_color='indianred',
    ))   
    #bar chart settings
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

    #used for updating the bar chart
    page.barGraphDisplay = PlotlyChart(barGraph,expand=True)

    #left side
    def left_column(align: ft.CrossAxisAlignment):
        return ft.Column (
            [
            #title
            ft.Container(
                content=page.titleText,
                margin=2,
                padding=2,
                alignment=ft.alignment.Alignment(-0.9,0),
                bgcolor="#89A8BD",
                width=400,
                height=83,
                border_radius=10,
            ),
            #bar chart
            ft.Container(
                content = 
                    ft.Container(
                    content=page.barGraphDisplay,
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
            ]
        )
    
    #right side
    def right_column(align: ft.CrossAxisAlignment):
        return ft.Column(
            [
            ft.Container(
                content=
                ft.Column (
                    [
                    #current time box
                    ft.Container(
                        content=page.currTimeText,
                        margin=2,
                        padding=2,
                        alignment=ft.alignment.Alignment(-0.9,0),
                        bgcolor="#426276",
                        width=450,
                        height=83,
                        border_radius=10,
                    ),
                    #no of tries box
                    ft.Container(
                        content=page.triesText,
                        margin=2,
                        padding=2,
                        alignment=ft.alignment.Alignment(-0.9,0),
                        bgcolor="#426276",
                        width=450,
                        height=83,
                        border_radius=10,
                    ),
                    #elapsed time box
                    ft.Container(
                        content=page.elapsedTimeText,
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
                        #prev values box
                        ft.Container(
                        content=ft.Text("Previous values", font_family="Boldena", size="60"),
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
                        #divider
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
                        #left column of prev values
                        ft.Column(
                                [
                                    #box1
                                    ft.Container(
                                        content=page.box1,
                                        margin=2,
                                        padding=2,
                                        alignment=ft.alignment.center,
                                        bgcolor="#426276",
                                        width=220,
                                        height=150,
                                        border_radius=10,
                                        ),
                                    #box3
                                    ft.Container(
                                        content=page.box3,
                                        margin=2,
                                        padding=2,
                                        alignment=ft.alignment.center,
                                        bgcolor="#426276",
                                        width=220,
                                        height=150,
                                        border_radius=10,
                                        ),
                                    #box5
                                    ft.Container(
                                        content=page.box5,
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
                        #right column of prev values
                        ft.Column(
                                [
                                    #box2
                                    ft.Container(
                                        content=page.box2,
                                        margin=2,
                                        padding=2,
                                        alignment=ft.alignment.center,
                                        bgcolor="#426276",
                                        width=220,
                                        height=150,
                                        border_radius=10,
                                        ),
                                    #box4
                                    ft.Container(
                                        content=page.box4,
                                        margin=2,
                                        padding=2,
                                        alignment=ft.alignment.center,
                                        bgcolor="#426276",
                                        width=220,
                                        height=150,
                                        border_radius=10,
                                        ),
                                    #box6
                                    ft.Container(
                                        content=page.box6,
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

    #finds how close the shuffled list is to the sorted list (if 0 was returned the list would be sorted and any other number is how close the list is to be sorted)
    def wholeAlikeness(list4):
        total_alikeness = 0
        for i in range(0, len(list4)):
            total_alikeness += abs(list_shuffled[i] - (i+1))
            total_alikeness += 1
            return total_alikeness
        
    #takes in a length and makes a new list from 1 - length
    def makeNewList(length):
        global list_shuffled
        list_shuffled = list(range(1, length + 1))
        shuffle(list_shuffled)  

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
        
            
    #updates the bar graph and colours it
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

    #Responsible for making incrementing the number of values in the list, checking wether the list is sorted and updating the prev values and title text
    for i in range(2, 100):
        makeNewList(i)
        updateTitleText(i)
        sortChecker(list_shuffled, i)
        updatePrevResults()
    
ft.app(target=main)
# ft.app(target=main,port=8550,view=ft.WEB_BROWSER)


    