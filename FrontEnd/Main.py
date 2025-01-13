import flet as ft
from Login import login_page
from Registro import register_page
from Menu import menu_page
from AdicionarAcao import adicionarAcao_page

def main(page: ft.Page):
    page.title = "Carteira de Ação"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#000000"
    page.fonts = {
        "MinhaFonte": "C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Fontes/Fonte.ttf", 
        
    }
    def go_to_register(event):
        page.clean()
        page.add(register_page(go_to_login))

    def go_to_login(event):
        page.clean()
        
        page.add(login_page(go_to_register, go_to_menu))
    
    def go_to_menu(event):
        page.clean()
        page.add(menu_page(go_to_login, go_to_AdicionarAcao))

    def go_to_AdicionarAcao(event=None):
        page.clean()
        page.add(adicionarAcao_page(go_to_menu))

    go_to_AdicionarAcao()

ft.app(target=main)