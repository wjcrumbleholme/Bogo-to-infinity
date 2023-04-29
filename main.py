import flet as ft
import bogo as bo
from time import sleep
from random import shuffle
from timeit import default_timer as timer
from flet.plotly_chart import PlotlyChart

def main(page: ft.Page):
    # FORMAT: [Divider color, Container border color, Container color, Background color,  Text color, Far bar, Medium bar, Close bar, Actual bar]
    light = ["#BDCDD6","#6096B4","#93BFCF","#BDCDD6", "#2C3333", "#FF6363", "#FFAB76", "#FFFDA2", "#BAFFB4"]
    dark = ["#2C3333", "#2E4F4F", "#0E8388", "#2C3333", "#CBE4DE", "#37306B", "#66347F", "#9E4784", "#D27685"]
    colSchem = light

    windowY = page.height
    windowX = page.width
    aspectY = 1000
    aspectX = (windowX / windowY) * 1000
    textRatio = ((windowX * windowY) / (aspectX * aspectY))
    sizeMultX = windowX/aspectX
    sizeMultY = windowY/aspectY

    #width(x): height(y)
    def page_update(e):
        print("New page size:", page.width, page.height)
        windowY = page.height
        windowX = page.width
        aspectY = 1000
        aspectX = (windowX / windowY) * 1000
        print(f"New aspect: {aspectX}:{aspectY}")
        sizeMultX = windowX/aspectX 
        sizeMultY = windowY/aspectY 
        textRatio = sizeMultY
        # textRatio = ((windowX * windowY) / (aspectX * aspectY))
        genElements(sizeMultX, sizeMultY, textRatio)
        print(mainWindow)
        page.clean()
        addElementsToScreen()
        
    page.on_resize = page_update
    
    #settings for the page
    page.title = "Sorting algorithms"
    page.window_height = windowY
    page.window_width = windowX
    page.window_resizable = True
    page.fonts = {
        'Boldena' : "/fonts/BoldenaBold.ttf"
    }

    def colToggle(e):
        nonlocal colSchem, colButtonIcon, colButtonIconColor
        if colSchem[:] == light[:]:
            colSchem = dark
            colButtonIcon = ft.icons.LIGHT_MODE
            colButtonIconColor = "#FFFFFF"
        else:
            colSchem = light
            colButtonIcon = ft.icons.DARK_MODE
            colButtonIconColor = "#232528"
        page_update(e)
        
    def bogoButtonLogic(e):
        nonlocal bogoSortSelected
        if bogoSortSelected:
            pass
        else:
            bogoSortSelected = True
            page_update(e)
            startBogoLogic(2, 100)

    def stopButtonLogic(e):
        global bogoStop
        nonlocal bogoSortSelected
        bogoSortSelected = False
        bogoStop = True

        
    def bogoSortElements(sizeX, sizeY, sizeText, colSchem):
        screenElements = ft.Container(
            content=bo.sendElementsToOtherFile(sizeX, sizeY, sizeText, colSchem)
        )
        return screenElements
        

    
    bogoSortSelected = False
    rightContainerContents = ft.Text("")
    colButtonIcon = ft.icons.DARK_MODE
    colButtonIconColor = "#232528"
    def genElements(sizeX, sizeY, sizeText):
        global mainWindow, colButtonContainer, leftContainer, rightContainer, colButton, bogoButton, bogoButtonContainer, buttonDivider
        nonlocal rightContainerContents

        page.bgcolor = colSchem[3]
        mainWindow = ft.Container (
            content= ft.Text(""),
            margin=2,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=colSchem[3],
            width= sizeX * 1605,
            height= sizeY * 940,
            border_radius=10,
        )
        bogoButton = ft.IconButton(
                icon=ft.icons.SHUFFLE,
                icon_color=colSchem[4],
                selected_icon_color='#FFFFFF',
                icon_size=sizeText * 48,
                tooltip="Bogo Sort", 
                on_click=bogoButtonLogic,
            )
        stopButton = ft.IconButton(
                icon=ft.icons.CANCEL,
                icon_color='#F76C5E',
                selected_icon_color='#FFFFFF',
                icon_size=sizeText * 48,
                tooltip="Stop", 
                on_click=stopButtonLogic,
            )
        buttonDivider = ft.Container(
            margin=2,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=colSchem[0],
            width= sizeX * 63,
            height= sizeY * 5,
            border_radius=10,
        )
        colButton = ft.IconButton(
                icon=colButtonIcon,
                icon_color=colButtonIconColor,
                selected_icon_color='#FFFFFF',
                icon_size=sizeText * 48,
                tooltip="Toggle Theme", 
                on_click=colToggle,
            )
        colButtonContainer = ft.Container(
                content= colButton,
                margin=2,
                padding=2,
                alignment=ft.alignment.center,
                bgcolor=colSchem[2],
                width= sizeX * 83,
                height= sizeY * 83,
                border_radius=10,
            )
        bogoButtonContainer = ft.Container(
                content= bogoButton,
                margin=2,
                padding=2,
                alignment=ft.alignment.center,
                bgcolor=colSchem[2],
                width= sizeX * 83,
                height= sizeY * 83,
                border_radius=10,
            )
        stopButtonContainer = ft.Container(
                content= stopButton,
                margin=2,
                padding=2,
                alignment=ft.alignment.center,
                bgcolor=colSchem[2],
                width= sizeX * 83,
                height= sizeY * 83,
                border_radius=10,
            )
        leftContainer = ft.Container(
            content= ft.Column([
            
                colButtonContainer,
                stopButtonContainer,
                buttonDivider,
                bogoButtonContainer,
                
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            margin=2,
            padding=4,
            alignment=ft.alignment.top_center,
            bgcolor=colSchem[1],
            width= sizeX * 100,
            height= sizeY * 970,
            border_radius=10,
        )
        if bogoSortSelected == True:
            mainWindow.content = bogoSortElements(sizeX, sizeY, sizeText, colSchem)
            rightContainerContents = mainWindow


        rightContainer = ft.Container(
            content= ft.Column([
                rightContainerContents,
            ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
            margin=0,
            padding=0,
            alignment=ft.alignment.center,
            bgcolor=colSchem[1],
            width= sizeX * 1635,
            height= sizeY * 970,
            border_radius=10,
        )

    genElements(sizeMultX,sizeMultY, textRatio)


    def addElementsToScreen():
        page.add(
            ft.Column(
            [
                ft.Row([
                    leftContainer,
                    rightContainer,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                ),
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),

            
        )
    
    addElementsToScreen()



    #----BOGO LOGIC----#
    def startBogoLogic(startNum, endNum):
        startTime = timer()
        global bogoStop
        bogoStop = False
        for i in range(startNum, endNum):
            if bogoStop:
                bo.prevResults = ['','','','','','']
                break
            bo.makeNewList(i)
            bo.titleText.value = f"Bogo Sort - {i}"
            bo.titleText.update()
            mainLogicLoop(bo.list_shuffled, i, startTime)
            bo.updatePrevResults()
    
    def mainLogicLoop(list, currNum, startTime):
        listSorted = False
        tries = 0
        thisTime = timer()
        global bogoStop
        bogoStop = False
        while listSorted == False:
                if bogoStop:
                    break
                listSorted = True
                for i in range(0, len(list) - 1):
                    if list[i+1] < list[i]:
                        listSorted = False
                tries += 1
                shuffle(bo.list_shuffled)
                bo.triesText.value = f"Number of tries: {tries}"
                bo.triesText.update()
                measuredTime = timer()
                currTime = bo.timeDifference(measuredTime, thisTime)
                
                
                if tries % currNum == 0:
                    bo.currTimeText.value = f"Current sort time - {currTime}"
                    bo.updateBarChart(bo.list_shuffled)
                    bo.elapsedTimeText.value = bo.elapsedTime(startTime)
                    page.update()
                else:
                    pass

        bo.updateBarChart(bo.createList(1,currNum))
        page.update()
        sleep(0.5)
        page.update()
        bo.storeInfo(currNum, tries, currTime)


ft.app(target=main,port=5000)
#ft.app(target=main,port=5000,assets_dir="fonts",view=ft.WEB_BROWSER)