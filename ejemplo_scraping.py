import requests
from bs4 import BeautifulSoup

URL = "https://www.bcv.org.ve/"


def precios_divisas():
    response = requests.get(URL, verify=False)

    resultado = {
        'divisas': [
            
        ],
        'status': 200
    }
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            divs = soup.find_all('div', class_="row recuadrotsmc")
            
            for i in divs:
                sopa = BeautifulSoup(str(i), 'html.parser')
                
                simbolo = sopa.find('span').text
                
                precio = sopa.find('div', class_="col-sm-6 col-xs-6 centrado").text
                resultado['divisas'].append({
                    'simbolo': simbolo,
                    'precio': float(precio.strip().replace(",","."))
                })
    except Exception as e:
        resultado = {
            'Mensaje': str(e),
            'Status': 500
        }

    return resultado