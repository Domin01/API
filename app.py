import requests
import os

url_base='https://pro-api.coinmarketcap.com/v1'
key=os.environ["Key"]

parametros={'start':'1','limit':'20','convert':'USD'}
cabeceras= {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': key,
}

menu='''
1.- Elije el rango de la lista de divisas a mostrar entre 1 y 5000. 
2.- Elije un rango de la lista de criptomonedas a mostrar entre 1 y 10.000.
3.- Dime el nombre de una criptomoneda y te muestro su información.
4.- Salir
'''


print(menu)
opcion=int(input("Elige una opcion del menu: "))

while opcion!=4:

  if opcion==1:
    parametros={'start':'1','limit':'20'}
    url='/fiat/map'
    parametros["limit"] = int(input("Dime el rango a utilizar: "))
    r=requests.get(url_base+url,params=parametros,headers=cabeceras)
    monedas= r.json()
    for a in monedas["data"]:
        print(a["name"],a["sign"],a["symbol"])
    divisa=input("Dime la divisa para utilizar: ")
    parametros["convert"] = divisa
    print(menu)
    opcion=int(input("Elige una opcion del menu: "))
  
  if opcion==2:
    parametros["limit"] = int(input("Dime el rango a utilizar: "))
    url='/cryptocurrency/listings/latest'
    r=requests.get(url_base+url,params=parametros,headers=cabeceras)
    if r.status_code == 200:
      monedas = r.json()
      print("---LISTADO---")
      for a in monedas["data"]:
        print(a["name"])
    print(menu)
    opcion=int(input("Elige una opcion del menu: "))
    
  if opcion==3:
    url='/cryptocurrency/listings/latest'
    respuesta=(input("Dime un nombre de la lista anterior: "))
    r=requests.get(url_base+url,params=parametros,headers=cabeceras)
    if r.status_code == 200:
      monedas = r.json()
      for a in monedas["data"]:
        if a["name"] == respuesta:
          print("---NOMBRE---")
          print(a["name"])
          print("---SIMBOLO---")
          print(a["symbol"])
          print("---FECHA AÑADIDA---")
          print(a["date_added"])
          print(f"---PRECIO ACTUAL",parametros["convert"],"---")
          print(int(a.get("quote").get(parametros["convert"]).get("price")))
          print("---VOLUMEN 24H---")
          print(int(a.get("quote").get(parametros["convert"]).get("volume_24h")))
          print("---CAPITALIZACIÓN EN EL MERCADO---")
          print(int(a.get("quote").get(parametros["convert"]).get("market_cap")))
      print(menu)
      opcion=int(input("Elige una opcion del menu: "))

  if opcion==4:
    break