import flet as ft
import requests
import time
from Outros.ApiExternaBuscas import nomeAcoes, infoAcoes, CadastrarAcaoNaCarteira
from Outros.session import session

def adicionarAcao_page(on_menu):

    estado_positivo = True

    def InformaçãoAçao(evento):
        response = infoAcoes(codigo_value.value)
        inserir = response.json()
        
        nome_acao = str(inserir['results'][0].get('longName', 'Null'))

        minimo = inserir['results'][0].get('regularMarketDayLow', 0)
        minima_acao = str(minimo if minimo != 0 else inserir['results'][0].get('regularMarketPrice', 0))

        maxima =  inserir['results'][0].get('regularMarketDayHigh', 0)
        maxima_acao = str(maxima if maxima != 0 else inserir['results'][0].get('regularMarketPrice', 0))
        
        volume_acao = str(inserir['results'][0].get('regularMarketVolume', '0'))
        logo_url = str(inserir['results'][0].get('logourl', ''))

        Nome_acao.value = nome_acao
        Codigo_acao.value = "Codigo \n" + codigo_value.value
        Maxima_acao.value = "Maxima \nR$:" + maxima_acao
        Minima_acao.value = "Minima \nR$:" + minima_acao
        Volume_acao.value = "Volume \n" + volume_acao
        Logo_acao.src = logo_url

        
        container_2.controls = [Nome_acao, Codigo_acao, Maxima_acao, Minima_acao, Volume_acao, Logo_acao]
        container_2.update()

    def CadastrarAcaoNaCarteira(Evento):
        nonlocal estado_positivo
        
        try:
           
            parametros = {
                "codigo": codigo_value.value,
                "Nome": Nome_acao.value,
                "Valor": valor_value.value if estado_positivo == True else float(valor_value.value) * -1,
                "quantidade": Quantidade_value.value  if estado_positivo == True else float(Quantidade_value.value) * -1,
                "idUsuario": session.user_data.get('idLogin')
            }
            
            response = CadastrarAcaoNaCarteira(parametros)

            if(response.status_code == 200):
                mensagem_api.value = "Ação adicionada"
                mensagem_api.color = "green"
            else:
                mensagem_api.value = "Erro ao adicionar"
                mensagem_api.color = "red"

        except requests.exceptions.RequestException as e:
            mensagem_api.value = str(e)
            mensagem_api.color = "red"

        mensagem_api.update()
        time.sleep(1)

        mensagem_api.value = ""
        mensagem_api.update()

    def mudarSinal(evento):
        nonlocal estado_positivo  
        if estado_positivo:
            sinal.content = ft.Text("-", color="#FF0000", font_family="MinhaFonte", size=20)
        else:
            sinal.content = ft.Text("+", color="#008000", font_family="MinhaFonte", size=20)
        estado_positivo = not estado_positivo  
        sinal.update()

    image = "C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/FundoLoginRegistro.png"

    #Container 1
    lista_acoes = nomeAcoes()
    codigo_value = ft.Dropdown(label="Ações", hint_content="Escolha sua ação", options= [ft.dropdown.Option(acao) for acao in lista_acoes], autofocus=True, prefix=image, border_color="#f7931a", label_style=ft.TextStyle(color="#000000"), width=400, height=50)

    nome_value = ft.TextField(label="Nome açao", width=400, height=50, label_style= ft.TextStyle(color="#000000"), prefix=image, border_color="#f7931a")

    valor_value = ft.TextField(label="Valor Unitario", width=343, height=50, label_style= ft.TextStyle(color="#000000"), prefix=image, border_color="#f7931a")

    sinal = ft.ElevatedButton(content=ft.Text("+", color="#008000", font_family="MinhaFonte", size=20),width=50, height=50, bgcolor="#ffcb8c", on_click=mudarSinal)

    Quantidade_value = ft.TextField(label="Quantidade", width=400, height=50, label_style= ft.TextStyle(color="#000000"), prefix=image, border_color="#f7931a")

    mensagem_api = ft.Text("", color="white", font_family="MinhaFonte")
    
    #Container 2
    Nome_acao = ft.Text("Nome da ação", font_family="MinhaFonte", color="#ed8200", size=30)
    Codigo_acao = ft.Text("Codigo \n Nome ", font_family="MinhaFonte", color="#ed8200", size=25)
    Maxima_acao = ft.Text("Maxima \n R$:0.00", font_family="MinhaFonte", color="#ed8200", size=25)
    Minima_acao = ft.Text("Minima \n R$:0.00", font_family="MinhaFonte", color="#ed8200", size=25)
    Volume_acao = ft.Text("Volume \n 0", font_family="MinhaFonte", color="#ed8200", size=25)
    Logo_acao = ft.Image(
        src="C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/DefaultLogoValor.png",
        width=150,
        height=150,
        fit=ft.ImageFit.CONTAIN,
    )

    container_2 = ft.Container(
        content=ft.Column(
            [
                Nome_acao,

                ft.Container(height=40),
                Logo_acao,
                ft.Container(height=40),

                ft.Row(
                    [
                        Codigo_acao,
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
                            on_click=on_menu 
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
    )

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
                    
                    ft.Row(
                        controls=[
                            valor_value,
                            sinal
                        ],  alignment=ft.MainAxisAlignment.CENTER
                    ),

                    Quantidade_value,
                    mensagem_api,

                    ft.Row(
                        [
                            ft.CupertinoButton(
                                content=ft.Text("Adicionar", color="#ed8200", font_family="MinhaFonte", size=25),
                                on_click=CadastrarAcaoNaCarteira
                            ),
                            ft.CupertinoButton(
                                content=ft.Text("Informação Ação", color="#ed8200", font_family="MinhaFonte", size=25),
                                on_click=InformaçãoAçao
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8,
            ),
            width=500,
            height=600,
            padding=20,
            border_radius=ft.border_radius.all(50),
            alignment=ft.alignment.center,
            image_src=image,
            image_fit=ft.ImageFit.COVER,
        ),

        container_2
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    spacing=20,
)


