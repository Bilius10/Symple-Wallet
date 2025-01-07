import flet as ft
import requests

def main(page: ft.Page):
     # Configurar o título da página
    page.title = "Tela de Registro"
    
    # Criar os campos de entrada
    login_input = ft.TextField(label="Login", autofocus=True)
    senha_input = ft.TextField(label="Senha", password=True)
    cpf_input = ft.TextField(label="CPF", keyboard_type=ft.KeyboardType.NUMBER)

    # Função para enviar os dados para o servidor
    def on_register_click(e):
        # Captura os dados inseridos nos campos
        login = login_input.value
        senha = senha_input.value
        cpf = cpf_input.value
        
        # Criar o corpo da requisição
        data = {"Login": login, "senha": senha, "cpf": cpf}
        
        # Enviar os dados via POST para o servidor
        try:
            response = requests.post("http://localhost:8080/auth/registro", json=data)
            if response.status_code == 200:
                page.add(ft.Text("Registro bem-sucedido!"))
            else:
                page.add(ft.Text("Erro ao registrar. Tente novamente."))
        except requests.exceptions.RequestException as e:
            page.add(ft.Text(f"Erro ao enviar dados: {e}"))

    # Criar botão de registro
    register_button = ft.ElevatedButton("Registrar", on_click=on_register_click)

    # Adicionar os componentes na página
    page.add(login_input, senha_input, cpf_input, register_button)


ft.app(target=main)