import flet as ft

def carregamento_page(on_AdicionarAcao, on_carteira):
    
    return ft.Container(
        content=ft.Column(
            [
                ft.Column(
                    [ft.ProgressRing()],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER, scale=4
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=9,
        ),
        width=500,
        height=700,
        padding=20,
        border_radius=ft.border_radius.all(50),
        alignment=ft.alignment.center,
        image_src="C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/TelaLogin.png",
        image_fit=ft.ImageFit.COVER,  
        
    )