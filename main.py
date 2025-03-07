import fastapi
import ejemplo_scraping

app = fastapi.FastAPI()

divisas = ejemplo_scraping.precios_divisas()

@app.get("/")
def precios():
    return divisas

@app.get("/divisas")
def divisa(simbolo: str):
    try:
        for moneda in divisas['divisas']:
            if moneda['simbolo'].lower().strip() == simbolo.lower():
                return {
                    'simbolo': moneda['simbolo'],
                    'precio': moneda['precio'],
                    'status': 200
                }
    except Exception as e:
        return {
            'Mensaje': str(e),
            'Status': 500
        }

@app.post("/conversion")
def conversion(simbolo: str, cantidad: float):
    try:
        for moneda in divisas['divisas']:
            if moneda['simbolo'].lower().strip() == simbolo.lower():
                return {
                    'simbolo': moneda['simbolo'],
                    'precio': moneda['precio'],
                    'conversion': moneda['precio'] * cantidad,
                    'status': 200
                }
    except Exception as e:
        return {
            'Mensaje': str(e),
            'Status': 500
        }
