import flet as ft
import requests

def login_page(on_register):

    cpf_value = ft.TextField(label="CPF", width=250, height=50, bgcolor="gray")
    senha_value = ft.TextField(label="Senha", width=250, height=50, bgcolor="gray")

    mensagem_api = ft.Text("", color="white")

    def fazerLogin(evento):
        
        data = {
            "cpf": cpf_value.value,
            "senha": senha_value.value
        }

        try:
            response = requests.post("http://localhost:8080/auth/login",json=data)
            
            if response.status_code == 200 or response.status_code == 201:
                mensagem_api.value = "Seja Bem vindo! "+response.json().get('login') 
                mensagem_api.color = "green"
            else:
                
                mensagem_api.value = response.json().get("message", "Erro desconhecido.")
                mensagem_api.color = "red"

        except requests.exceptions.RequestException as e:
            mensagem_api.value = f"Erro ao enviar dados: {e}"
            mensagem_api.color = "red"

        mensagem_api.update()

        senha_value.value = ""
        cpf_value.value = ""

        senha_value.update()
        cpf_value.update()


    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Login",
                    size=35,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),
                
                cpf_value,

                senha_value,

                ft.ElevatedButton(
                    "Enviar", width=200, height=45, on_click=fazerLogin
                ),
                mensagem_api,
                ft.CupertinoButton(
                    "Registrar", width=150, height=55, on_click=on_register
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
