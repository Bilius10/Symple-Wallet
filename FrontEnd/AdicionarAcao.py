import flet as ft

def adicionarAcao_page(on_menu, InfoUsuario):
    
    image = "C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/FundoLoginRegistro.png"

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    value="Login", color="#ed8200", font_family="MinhaFonte", size=80
                ),

                ft.Container(height=40),

                ft.CupertinoButton(
                    content=ft.Text("Enviar", color="#ed8200", font_family="MinhaFonte", size=30), width=400, height=70, 
                ),
                
                ft.CupertinoButton(
                    content=ft.Text("Registrar", color="#ed8200", font_family="MinhaFonte", size=20), width=150, height=55, 
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=9,
        ),
        width=500,
        height=500,
        padding=20,
        border_radius=ft.border_radius.all(50),
        alignment=ft.alignment.center,
        image_src=image,
        image_fit=ft.ImageFit.COVER,  
        
    )