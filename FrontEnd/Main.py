import flet as ft


def main(page: ft.Page):
    page.title = "Carteira de Ação"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#000000"

    
    def Registrar(evento):
        page.clean()

        def EnviarRegistro():
            pass
        
        login_card = ft.Container(
        content=ft.Column(
            [
                 ft.Text(
                    "Registrar",
                    size=35,  
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),
                ft.TextField(
                    label="Nome", width=250, height=50, bgcolor="gray"
                ),  
                ft.TextField(
                    label="Senha", width=250, height=50, password=True, bgcolor="gray"
                ),
                ft.TextField(
                    label="Cpf", width=250, height=50, password=True, bgcolor="gray"
                ),
                ft.ElevatedButton(
                    "Enviar", width=200, height=45
                ),  
                  
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
        width=300,
        height=370,
        padding=20,
        border_radius=ft.border_radius.all(12),
        alignment=ft.alignment.center,
        bgcolor="#111111",

        
        )
        page.add(login_card)


    login_card = ft.Container(
        content=ft.Column(
            [
                 ft.Text(
                    "Login",
                    size=35,  
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),
                ft.TextField(
                    label="CPF", width=250, height=50, bgcolor="gray"
                ),  
                ft.TextField(
                    label="Senha", width=250, height=50, password=True, bgcolor="gray"
                ),
                ft.ElevatedButton(
                    "Enviar", width=200, height=45
                ),  
                ft.CupertinoButton(
                    "Registrar", width=150, height=55, on_click=Registrar
                ),  
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
        width=300,
        height=370,
        padding=20,
        border_radius=ft.border_radius.all(12),
        alignment=ft.alignment.center,
        bgcolor="#111111",
    )

    page.add(login_card)


ft.app(target=main)
