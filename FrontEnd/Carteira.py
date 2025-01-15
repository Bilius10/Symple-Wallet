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
            return "C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/Diamente.png"
        
    return ft.Container(
        content=ft.Column(
            [   
                ft.Text(
                    f"{session.user_data.get('login')+" Wallet"}",
                    size=30, font_family="MinhaFonte"
                ),

                ft.Image(
                    src=imagemDoNivel(),  
                    width=300,  
                    height=300,  
                    fit=ft.ImageFit.CONTAIN,  
                ),

                ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Codigo")),
                            ft.DataColumn(ft.Text("Nome")),
                            ft.DataColumn(ft.Text("Quantidade"), numeric=True),
                            ft.DataColumn(ft.Text("Valor Total"), numeric=True)
                        ],
                        rows=[
                            ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(acao["codigo"])),
                                ft.DataCell(ft.Text(acao["nome"])),
                                ft.DataCell(ft.Text(f"R$ {acao['quantidade']}")),
                                ft.DataCell(ft.Text(str(acao["quantidade"]*acao['valor'])))
                            ]
                        ) for acao in data["InfoAcoes"]
                    ]
                ),
            
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