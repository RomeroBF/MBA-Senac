# RODAR NO SERVIDOR
    # uvicorn main:app --reload

#ACESSAR RESULTADO:
    # http://127.0.0.1:8000/real-to-dolar/100 → converte R$100 em dólares
    # http://127.0.0.1:8000/dolar-to-real/50 → converte US$50 em reais


from fastapi import FastAPI
import requests
app = FastAPI()

# Função auxiliar para pegar a cotação em tempo real


def get_exchange_rate():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    response = requests.get(url)
    data = response.json()
    return float(data["USDBRL"]["bid"])  # preço de compra do dólar em reais

# Rota: converter de Real para Dólar


@app.get("/real-to-dolar/{valor}")
def real_to_dolar(valor: float):
    rate = get_exchange_rate()
    return {
        "valor_em_reais": valor,
        "cotacao": rate,
        "valor_em_dolares": round(valor / rate, 2)
    }

# Rota: converter de Dólar para Real


@app.get("/dolar-to-real/{valor}")
def dolar_to_real(valor: float):
    rate = get_exchange_rate()
    return {
        "valor_em_dolares": valor,
        "cotacao": rate,
        "valor_em_reais": round(valor * rate, 2)
    }
