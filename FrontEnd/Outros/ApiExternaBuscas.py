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

def infoAcoes(nomeAcao):

    try:

        response = requests.get("http://localhost:8080/external/API/"+nomeAcao)

        if(response.status_code == 200):
            return response
        else:
            return {
                    "results": [
                        {
                            "longName": "null",
                            "regularMarketDayHigh": 0.0,
                            "regularMarketDayLow": 0.0,
                            "logourl": "null",
                            "regularMarketVolume": 0
                        }
                    ]
                    }
        
    except requests.exceptions.RetryError as e:
        return str(e)
    