import flet as ft
import pandas as pd
from Outros.ApiExternaBuscas import nomeAcoes


def adicionarAcao_page(on_menu):
    
    image = "C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/FundoLoginRegistro.png"

    #Container 1
    lista_acoes = nomeAcoes()
    codigo_value = ft.Dropdown(label="Ações", hint_content="Escolha sua ação", options= [ft.dropdown.Option(acao) for acao in lista_acoes], autofocus=True, prefix=image, border_color="#f7931a", label_style=ft.TextStyle(color="#000000"), width=400, height=50)

    nome_value = ft.TextField(label="Nome açao", width=400, height=50, label_style= ft.TextStyle(color="#000000"), prefix=image, border_color="#f7931a")

    valor_value = ft.TextField(label="Valor Unitario", width=400, height=50, label_style= ft.TextStyle(color="#000000"), prefix=image, border_color="#f7931a")

    Quantidade_value = ft.TextField(label="Quantidade", width=400, height=50, label_style= ft.TextStyle(color="#000000"), prefix=image, border_color="#f7931a")
    
    #Container 2
    Nome_acao = ft.Text("Nome \n Nome ", font_family="MinhaFonte", color="#ed8200", size=25)
    Maxima_acao = ft.Text("Maxima \n R$:0.00", font_family="MinhaFonte", color="#ed8200", size=25)
    Minima_acao = ft.Text("Minima \n R$:0.00", font_family="MinhaFonte", color="#ed8200", size=25)
    Volume_acao = ft.Text("Volume \n 0", font_family="MinhaFonte", color="#ed8200", size=25)
    Logo_acao = ft.Image(
        src="C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/DefaultLogoValor.png",
        width=150,
        height=150,
        fit=ft.ImageFit.CONTAIN,
    )

    def voltar(evento):
        on_menu(evento)

    return ft.Row(
    [
        # Primeiro quadrado
        ft.Container(
            content=ft.Column(
                [
                    ft.Image(
                        src="C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/MenuLogo.png",
                        width=250,
                        height=250,
                        fit=ft.ImageFit.CONTAIN,
                    ),

                    codigo_value,
                    nome_value,
                    valor_value,
                    Quantidade_value,

                    ft.Row(
                        [
                            ft.CupertinoButton(
                                content=ft.Text("Adicionar", color="#ed8200", font_family="MinhaFonte", size=25),
                            ),
                            ft.CupertinoButton(
                                content=ft.Text("Informação Ação", color="#ed8200", font_family="MinhaFonte", size=25),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            width=500,
            height=600,
            padding=20,
            border_radius=ft.border_radius.all(50),
            alignment=ft.alignment.center,
            image_src=image,
            image_fit=ft.ImageFit.COVER,
        ),

        # Segundo quadrado
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Informações da Ação", size=30, font_family="MinhaFonte", color="#ed8200"
                    ),

                    ft.Container(height=40),
                    Logo_acao,
                    ft.Container(height=40),

                    ft.Row(
                        [
                            Nome_acao,
                            Maxima_acao
                        ],
                        alignment=ft.MainAxisAlignment.CENTER, spacing=30
                    ),

                    ft.Row(
                        [
                            Volume_acao,
                            Minima_acao
                        ],
                        alignment=ft.MainAxisAlignment.CENTER, spacing=30
                    ),

                    ft.CupertinoButton(
                                content=ft.Text("Voltar", color="#ed8200", font_family="MinhaFonte", size=25),
                                on_click=voltar
                    ),
                    

                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            width=500,
            height=600,
            padding=20,
            border_radius=ft.border_radius.all(50),
            alignment=ft.alignment.center,
            image_src=image,
            image_fit=ft.ImageFit.COVER,
        ),
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    spacing=20,
)


