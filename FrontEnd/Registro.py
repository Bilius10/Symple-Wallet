import flet as ft
import requests

def register_page(on_back):
    
    nome_value = ft.TextField(label="Nome", width=250, height=50, bgcolor="gray")
    senha_value = ft.TextField(label="Senha", width=250, height=50, password=True, bgcolor="gray")
    cpf_value = ft.TextField(label="CPF", width=250, height=50, bgcolor="gray")
    
    
    mensagem_api = ft.Text("", color="white")

    def fazerRegistro(evento):
        
        data = {
            "login": nome_value.value,
            "senha": senha_value.value,
            "cpf": cpf_value.value
        }

        try:
            response = requests.post("http://localhost:8080/auth/registro", json=data)
            if response.status_code == 200 or response.status_code == 201:
                mensagem_api.value = "Registro bem-sucedido!"
                mensagem_api.color = "green"
            else:
                
                mensagem_api.value = response.json().get("message", "Erro desconhecido.")
                mensagem_api.color = "red"
        except requests.exceptions.RequestException as e:
            mensagem_api.value = f"Erro ao enviar dados: {e}"
            mensagem_api.color = "red"

       
        mensagem_api.update()

        nome_value.value = ""
        senha_value.value = ""
        cpf_value.value = ""

        nome_value.update()
        senha_value.update()
        cpf_value.update()
    
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Registrar",
                    size=35,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),
                nome_value,
                senha_value,
                cpf_value,
                ft.ElevatedButton(
                    "Enviar", width=200, height=45, on_click=fazerRegistro
                ),
                mensagem_api,  
                ft.CupertinoButton(
                    "Voltar", width=150, height=55, on_click=on_back
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
        width=300,
        height=450,
        padding=20,
        border_radius=ft.border_radius.all(12),
        alignment=ft.alignment.center,
        bgcolor="#111111",
    )
