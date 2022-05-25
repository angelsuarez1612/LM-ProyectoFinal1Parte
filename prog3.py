import requests
import json
import os

url_base="https://exchange-rates.abstractapi.com/v1/"
key=os.environ["api_key"]
moneda1=input("Moneda a buscar: ")
moneda2=input("Moneda a devolver: ")
fecha=input("Introduce la fecha en la que buscar: (FORMATO YYY-MM-DD) ")

payload={'api_key':key,"base":moneda1,"target":moneda2,"date":fecha}

url=url_base+"historical"
r=requests.get(url,params=payload)
if r.status_code == 200:
    datos=r.json()
    print(json.dumps(datos,indent=4,sort_keys=True))
else:
    print("Error")
    print(r.status_code)
