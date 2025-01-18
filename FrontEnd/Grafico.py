import flet as ft
from Outros.session import session

def grafico_page(on_menu):
    
    image = "C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/FundoLoginRegistro.png"

    return ft.Container(
        ft.CupertinoButton(
                            content=ft.Text("Voltar", color="#ed8200", font_family="MinhaFonte", size=25),
                            on_click=on_menu 
        ),
        width=500,
        height=600,
        padding=20,
        border_radius=ft.border_radius.all(50),
        alignment=ft.alignment.center,
        image_src=image,
        image_fit=ft.ImageFit.COVER,
    )