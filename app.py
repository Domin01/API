import requests
import os

url_base='https://pro-api.coinmarketcap.com/v1'
key=os.environ["Key"]

categorias='/cryptocurrency/listings/latest'

cabeceras= {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': key,
}



parametros={
  'start':'1',
  'limit':'20',
  'convert':'USD'
}

r=requests.get(url_base+categorias,params=parametros,headers=cabeceras)
if r.status_code == 200:
    doc = r.text
    
print(doc)
        



#Debes entregar al menos tres programas python que realicen peticiones a la API (o APIs) 
# que vayas a utilizar en la práctica