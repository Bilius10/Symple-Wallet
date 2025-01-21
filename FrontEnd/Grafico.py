import flet as ft
from Outros import ApiExternaBuscas

def grafico_page(on_menu):

    acoes_usuario = ApiExternaBuscas.acoesUsuario()

    def atualizar_graficos(e):
        acao_selecionada = dropdown.value
        if not acao_selecionada:
            return

        dados_acao = ApiExternaBuscas.InfoAcoes30diasCompleta(acao_selecionada)
        historico = dados_acao["results"][0]["historicalDataPrice"]

        # Preparando dados dos gráficos
        dados_fechamento = [
            ft.LineChartDataPoint(i + 1, data["close"]) for i, data in enumerate(historico)
        ]
        dados_volumes = [
            ft.LineChartDataPoint(i + 1, data["volume"]) for i, data in enumerate(historico)
        ]
        dados_maximos = [
            ft.LineChartDataPoint(i + 1, data["high"]) for i, data in enumerate(historico)
        ]
        dados_minimos = [
            ft.LineChartDataPoint(i + 1, data["low"]) for i, data in enumerate(historico)
        ]

        # Atualizando os gráficos
        grafico_fechamento.data_series = [
            ft.LineChartData(data_points=dados_fechamento, color=ft.Colors.BLUE, stroke_width=2)
        ]
        grafico_fechamento.min_y = min(data["close"] for data in historico)
        grafico_fechamento.max_y = max(data["close"] for data in historico)
        grafico_fechamento.x_axis_label = "Dias"
        grafico_fechamento.y_axis_label = "Preço de Fechamento"

        grafico_volume.data_series = [
            ft.LineChartData(data_points=dados_volumes, color=ft.Colors.GREEN, stroke_width=2)
        ]
        grafico_volume.min_y = 0
        grafico_volume.max_y = max(data["volume"] for data in historico)
        grafico_volume.x_axis_label = "Dias"
        grafico_volume.y_axis_label = "Volume"

        grafico_max_min.data_series = [
            ft.LineChartData(data_points=dados_maximos, color=ft.Colors.RED, stroke_width=2),
            ft.LineChartData(data_points=dados_minimos, color=ft.Colors.ORANGE, stroke_width=2)
        ]
        grafico_max_min.min_y = min(data["low"] for data in historico)
        grafico_max_min.max_y = max(data["high"] for data in historico)
        grafico_max_min.x_axis_label = "Dias"
        grafico_max_min.y_axis_label = "Preço"

        grafico_fechamento.update()
        grafico_volume.update()
        grafico_max_min.update()

    dropdown = ft.Dropdown(
        options=[ft.dropdown.Option(acao) for acao in acoes_usuario],
        width=200,
        on_change=atualizar_graficos,
        hint_text="Selecione uma ação",
    )

    grafico_fechamento = ft.LineChart(
        data_series=[], width=500, height=250, expand=True
    )
    grafico_volume = ft.LineChart(
        data_series=[], width=500, height=250, expand=True
    )
    grafico_max_min = ft.LineChart(
        data_series=[], width=500, height=250, expand=True
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.CupertinoButton(
                            content=ft.Text("Voltar", color="#ed8200", font_family="MinhaFonte", size=25),
                            on_click=on_menu,
                        ),
                        dropdown,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(),

                ft.Text("Valor - Últimos 30 dias", color="#ed8200", font_family="MinhaFonte", size=25, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                grafico_fechamento,

                ft.Text("Volume - Últimos 30 dias", color="#ed8200", font_family="MinhaFonte", size=20, weight=ft.FontWeight.BOLD),
                grafico_volume,

                ft.Text("Máximos e Mínimos - Últimos 30 dias", color="#ed8200", font_family="MinhaFonte", size=20, weight=ft.FontWeight.BOLD),
                grafico_max_min,
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        width=700,
        height=780,
        padding=20,
        border_radius=ft.border_radius.all(20),
        alignment=ft.alignment.center,
        image_src="C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/FundoLoginRegistro.png",
        image_fit=ft.ImageFit.COVER,
    )





