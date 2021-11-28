import requests

# Llamar la api y devolver las toda la información de regiones,countrys,languages etc. en formato json función no recibe parametros
def obtener_regiones():
    url = "https://restcountries.com/v2/all"
    response = requests.request("GET", url)
    return response.json()


