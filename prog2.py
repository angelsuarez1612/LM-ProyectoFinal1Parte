import requests
import json
import os

url_base="https://exchange-rates.abstractapi.com/v1/"
key="bd37a8482ef1452bb4a63e59900b08ae"
moneda=input("Moneda a buscar: ")
cantidaddevolver=input("Introduce la cantidad de monedas total a devolver: ")
devolver="EUR"

payload={'api_key':key,"base":moneda,"target":devolver,"base_amount":cantidaddevolver}

url=url_base+"convert"
r=requests.get(url,params=payload)
if r.status_code == 200:
    datos=r.json()
    print(json.dumps(datos,indent=4,sort_keys=True))
else:
    print("Error")
    print(r.status_code)
