import flet as ft
import bogo as bo
from time import sleep


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
        textRatio = ((windowX * windowY) / (aspectX * aspectY))
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
        
        
 
    colButtonIcon = ft.icons.DARK_MODE
    colButtonIconColor = "#232528"
    def genElements(sizeX, sizeY, sizeText):
        global mainWindow, bogoButtonContainer, leftContainer, rightContainer, colButton
        page.bgcolor = colSchem[3]
        mainWindow = ft.Container (
            content= ft.Text(""),
            margin=2,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=colSchem[2],
            width= sizeX * 1590,
            height= sizeY * 930,
            border_radius=10,
        )
        colButton = ft.IconButton(
                icon=colButtonIcon,
                icon_color=colButtonIconColor,
                selected_icon_color='#FFFFFF',
                icon_size=sizeText * 60,
                tooltip="Toggle Theme", 
                on_click=colToggle,
            )
        bogoButtonContainer = ft.Container(
                content= colButton,
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
                bogoButtonContainer,
            ],
            ),
            margin=2,
            padding=2,
            alignment=ft.alignment.top_center,
            bgcolor=colSchem[1],
            width= sizeX * 100,
            height= sizeY * 970,
            border_radius=10,
        )
        rightContainer = ft.Container(
            content= ft.Column([
                mainWindow,
            ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
            margin=2,
            padding=2,
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

ft.app(target=main,port=5000)
# ft.app(target=main,port=5000,assets_dir="fonts",view=ft.WEB_BROWSER)