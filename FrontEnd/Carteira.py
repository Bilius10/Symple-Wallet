import flet as ft
import pandas as pd
import requests
import time
from Outros.ApiExternaBuscas import nomeAcoes, infoAcoes
from Outros.session import session


def carteira_page(on_menu):
    
    headers = {"Authorization": "Bearer "+session.user_data.get('token')}
    response = requests.get("http://localhost:8080/acao/infoAcao/"+str(session.user_data.get('idLogin')), headers=headers)
    data = response.json()

    def imagemDoNivel():
        
        if(response.json().get('somaValor') is None):
            return "C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/Pedra.png"
         
        if(response.json().get('somaValor') <= 1000):
            return "C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/Pedra.png"
        elif(response.json().get('somaValor') <= 5000):
            return "C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/Carvao.png"
        elif(response.json().get('somaValor') <= 10000):
            return "C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/ouro.png"
        elif(response.json().get('somaValor') <= 50000):
            return "C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/Ruby.png"
        else:
            return "C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/Diamante.png"
    

    columns=[ft.DataColumn(ft.Text("Codigo")),
             ft.DataColumn(ft.Text("Nome")),
             ft.DataColumn(ft.Text("Quantidade"), numeric=True),
             ft.DataColumn(ft.Text("Valor Total"), numeric=True)]
    
    rows=[ft.DataRow(
                     cells=[
                            ft.DataCell(ft.Text(acao["codigo"])),
                            ft.DataCell(ft.Text(acao["nome"])),
                            ft.DataCell(ft.Text(f"R$ {acao['quantidade']}")),
                            ft.DataCell(ft.Text(str(acao["quantidade"]*acao['valor'])))
                           ]
                    ) for acao in data["InfoAcoes"]
        ]
    
    data_table = ft.DataTable(columns=columns,rows=rows,border=ft.border.all(1),)


    return ft.Container(
        content=ft.Column(
            [   
                ft.Text(
                    f"{session.user_data.get('login')+" Wallet"}",
                    size=30, font_family="MinhaFonte", color="#ed8200"
                ),

                ft.Image(
                    src=imagemDoNivel(),  
                    width=200,  
                    height=200,  
                    fit=ft.ImageFit.CONTAIN,  
                ),

                ft.Column([data_table], scroll=ft.ScrollMode.ALWAYS, height=150),

                ft.Row(
                        [
                            ft.Text(
                                f"{f"Quantidade \n{data['somaQuantidade']}"}",
                                size=30, font_family="MinhaFonte", color="#ed8200"
                            ),
                            ft.Text(
                                f"{f"Valor Total \nR$: {data['somaValor']}"}",
                                size=30, font_family="MinhaFonte", color="#ed8200"
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER, spacing=70,
                    ),

                ft.Row(
                        [
                            ft.Text(
                                f"{f"Melhor Ação \nMGLU3"}",
                                size=30, font_family="MinhaFonte", color="#ed8200"
                            ),
                            ft.Text(
                                f"{f"Pior Ação \nPETR4"}",
                                size=30, font_family="MinhaFonte", color="#ed8200"
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER, spacing=70,
                    )
            
            ],
            alignment=ft.MainAxisAlignment.START, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,  
        ),
        width=500,
        height=700,
        padding=20,
        border_radius=ft.border_radius.all(50),
        alignment=ft.alignment.center,
        image_src="C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/FundoLoginRegistro.png",
    )