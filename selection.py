import flet as ft

def main(page: ft.Page):
    page.windowY = 954
    page.windowX = 1672
    page.aspectY = 900
    page.aspectX = 1600
    page.textRatio = ((page.windowX * page.windowY) / (page.aspectX * page.aspectY))

    #settings for the page
    page.title = "Sorting algorithms"
    page.window_height = page.windowY
    page.window_width = page.windowX
    page.window_resizable = True
    page.window_maximized = True
    page.window_full_screen = True
    page.fonts = {
        'Boldena' : "/fonts/BoldenaBold.ttf"
    }

    def bogoStart(e):
        pass

    page.mainWindow = ft.Container (
        content= ft.Text(""),
        margin=2,
        padding=2,
        alignment=ft.alignment.center,
        bgcolor="blue",
        width= page.windowX/page.aspectX * 1500,
        height= page.windowY/page.aspectY * 1000,
        border_radius=10,
    )
    page.bogoButton = ft.IconButton(
            icon=ft.icons.ABC,
            icon_color="red",
            selected_icon_color='#FFFFFF',
            icon_size=page.textRatio * 40,
            tooltip="Exit",
            on_click=bogoStart,
        )
    page.bogoButtonContainer = ft.Container(
            content= page.bogoButton,
            margin=2,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor="blue",
            width= page.windowX/page.aspectX * 83,
            height= page.windowY/page.aspectY * 83,
            border_radius=10,
        )
    
    def rightColumn(align: ft.CrossAxisAlignment):
        return ft.Column (
            [
                page.mainWindow,
            ],
        )
    

    def leftColumn(align: ft.CrossAxisAlignment):
        return ft.Column(
            [
                page.bogoButtonContainer,
            ],   
        )

    page.add(
        ft.Row(
        [
            leftColumn(ft.CrossAxisAlignment.START),
            rightColumn(ft.CrossAxisAlignment.END),

        ],
        alignment=ft.MainAxisAlignment.END,
        )
        
    )
    

ft.app(target=main,port=5001,)