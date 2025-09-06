# main.py
from fastapi import FastAPI
import requests

app = FastAPI(title="API de Conversão USD-BRL")

# ------------------------------
# Função auxiliar para pegar a cotação em tempo real
# ------------------------------
def get_exchange_rate():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    response = requests.get(url)
    data = response.json()
    return float(data["USDBRL"]["bid"])  # preço de compra do dólar em reais

# ------------------------------
# Rota raiz / para teste
# ------------------------------
@app.get("/")
def root():
    return {"message": "API de Conversão USD-BRL está funcionando!"}

# ------------------------------
# Evitar 404 do favicon.ico
# ------------------------------
@app.get("/favicon.ico")
def favicon():
    return {}

# ------------------------------
# Rota: converter de Real para Dólar
# ------------------------------
@app.get("/real-to-dolar/{valor}")
def real_to_dolar(valor: float):
    rate = get_exchange_rate()
    return {
        "valor_em_reais": valor,
        "cotacao": rate,
        "valor_em_dolares": round(valor / rate, 2)
    }

# ------------------------------
# Rota: converter de Dólar para Real
# ------------------------------
@app.get("/dolar-to-real/{valor}")
def dolar_to_real(valor: float):
    rate = get_exchange_rate()
    return {
        "valor_em_dolares": valor,
        "cotacao": rate,
        "valor_em_reais": round(valor * rate, 2)
    }

# ------------------------------
# Rodar no Colab ou local
# ------------------------------
if __name__ == "__main__":
    import uvicorn
    import nest_asyncio
    from pyngrok import ngrok

    # Necessário para rodar Uvicorn no Colab/loop assíncrono
    nest_asyncio.apply()

    # Expor porta pública se necessário (ngrok)
    public_url = ngrok.connect(8000)
    print("API pública via ngrok:", public_url)

    # Rodar FastAPI
    uvicorn.run(app, host="0.0.0.0", port=8000)
