import requests
import matplotlib.pyplot as plt
import pandas as pd
def nomeAcoes():
    
    try:
        
        response = requests.get("http://localhost:8080/external/API/nomes")
        
        if(response.status_code == 200):
            
            data = response.json()
        
            return data.get("stocks", [])
        else:
            return []

    except requests.exceptions.RequestException as e:
        return {"Erro": "Nenhuma ação encontrada", "Detalhes": str(e)}  

