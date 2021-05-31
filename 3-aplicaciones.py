import json

with open('monedas.json') as file:
    monedas = json.load(file)

nombre=[]

for a in monedas.get("data"):
    print(a.get("name"))
    print(int(a.get("quote").get("USD").get("price")))
    break
