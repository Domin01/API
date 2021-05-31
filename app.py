import requests
import os

url_base='https://pro-api.coinmarketcap.com/v1'
#key=os.environ["Key"]
categorias='/cryptocurrency/listings/latest'
cabeceras= {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'f1109570-5ab5-4935-8038-0b4ef1fde30b',
}
parametros={'start':'1','limit':'20','convert':'USD'}

menu='''
1.- Elije la divisa en la que mostrar la informacion el resto del programa. 
2.- Elije un rango para mostrar el nombre de las criptomonedas entre 1 y 10.000.
3.- Dime el nombre de una criptomoneda y te muestro su información.
4.- Salir
'''

print(menu)
opcion=int(input("Elige una opcion del menu: "))
divisa="USD"

while opcion!=4:

  if opcion==1:
    print('''
    -----POR DEFECTO ES USD-----
    United States Dollar ($) USD
    Albanian Lek (L)  ALL	
    Algerian Dinar (د.ج) DZD	    
    Argentine Peso ($)	ARS	    
    Armenian Dram (֏)	AMD	    
    Australian Dollar ($)	AUD
    Azerbaijani Manat (₼)	AZN
    Bahraini Dinar (.د.ب)	BHD
    Bangladeshi Taka (৳)	BDT	   
    Belarusian Ruble (Br)	BYN	   
    Bermudan Dollar ($)	BMD	   
    Bolivian Boliviano (Bs.)	BOB	   
    Bosnia-Herzegovina Convertible Mark (KM)	BAM	   
    Brazilian Real (R$)	BRL	   
    Bulgarian Lev (лв)	BGN	   
    Cambodian Riel (៛)	KHR	   
    Canadian Dollar ($)	CAD	   
    Chilean Peso ($)	CLP	   
    Chinese Yuan (¥)	CNY	   
    Colombian Peso ($)	COP	   
    Costa Rican Colón (₡)	CRC	   
    Croatian Kuna (kn)	HRK	   
    Cuban Peso ($)	CUP	   
    Czech Koruna (Kč)	CZK	   
    Danish Krone (kr)	DKK	   
    Dominican Peso ($)	DOP	   
    Egyptian Pound (£)	EGP	   
    Euro (€)	EUR	   
    Georgian Lari (₾)	GEL	   
    Ghanaian Cedi (₵)	GHS	   
    Guatemalan Quetzal (Q)	GTQ	   
    Honduran Lempira (L)	HNL	   
    Hong Kong Dollar ($)	HKD	   
    Hungarian Forint (Ft)	HUF	   
    Icelandic Króna (kr)	ISK	   
    Indian Rupee (₹)	INR	   
    Indonesian Rupiah (Rp)	IDR	   
    Iranian Rial (﷼)	IRR	   
    Iraqi Dinar (ع.د)	IQD	   
    Israeli New Shekel (₪)	ILS	   
    Jamaican Dollar ($)	JMD	   
    Japanese Yen (¥)	JPY	   
    Jordanian Dinar (د.ا)	JOD	   
    Kazakhstani Tenge (₸)	KZT	   
    Kenyan Shilling (Sh)	KES	   
    Kuwaiti Dinar (د.ك)	KWD	   
    Kyrgystani Som (с)	KGS	   
    Lebanese Pound (ل.ل)	LBP	   
    Macedonian Denar (ден)	MKD	   
    Malaysian Ringgit (RM)	MYR	   
    Mauritian Rupee (₨)	MUR	   
    Mexican Peso ($)	MXN	   
    Moldovan Leu (L)	MDL	   
    Mongolian Tugrik (₮)	MNT	   
    Moroccan Dirham (د.م.)	MAD	   
    Myanma Kyat (Ks)	MMK	   
    Namibian Dollar ($)	NAD	   
    Nepalese Rupee (₨)	NPR	   
    New Taiwan Dollar (NT$)	TWD	   
    New Zealand Dollar ($)	NZD	   
    Nicaraguan Córdoba (C$)	NIO	   
    Nigerian Naira (₦)	NGN	   
    Norwegian Krone (kr)	NOK	   
    Omani Rial (ر.ع.)	OMR	   
    Pakistani Rupee (₨)	PKR	   
    Panamanian Balboa (B/.)	PAB	   
    Peruvian Sol (S/.)	PEN	   
    Philippine Peso (₱)	PHP	   
    Polish Złoty (zł)	PLN	   
    Pound Sterling (£)	GBP	   
    Qatari Rial (ر.ق)	QAR	   
    Romanian Leu (lei)	RON	   
    Russian Ruble (₽)	RUB	   
    Saudi Riyal (ر.س)	SAR	   
    Serbian Dinar (дин.)	RSD	   
    Singapore Dollar (S$)	SGD	   
    South African Rand (R)	ZAR	   
    South Korean Won (₩)	KRW	   
    South Sudanese Pound (£)	SSP	   
    Sovereign Bolivar (Bs.)	VES	   
    Sri Lankan Rupee (Rs)	LKR	   
    Swedish Krona ( kr)	SEK	   
    Swiss Franc (Fr)	CHF	   
    Thai Baht (฿)	THB	   
    Trinidad and Tobago Dollar ($)	TTD	   
    Tunisian Dinar (د.ت)	TND	   
    Turkish Lira (₺)	TRY	   
    Ugandan Shilling (Sh)	UGX	   
    Ukrainian Hryvnia (₴)	UAH	   
    United Arab Emirates Dirham (د.إ)	AED	   
    Uruguayan Peso ($)	UYU	   
    Uzbekistan Som (so'm)	UZS	 
    Vietnamese Dong (₫)	VND''')
    divisa=input("Dime la divisa para utilizar: ")
    parametros["convert"] = divisa
    r=requests.get(url_base+categorias,params=parametros,headers=cabeceras)
    opcion=int(input("Elige una opcion del menu: "))
  
  if opcion==2:
    parametros["limit"] = int(input("Dime el rango a utilizar: "))
    r=requests.get(url_base+categorias,params=parametros,headers=cabeceras)
    if r.status_code == 200:
      monedas = r.json()
      print("---LISTADO---")
      for a in monedas["data"]:
        print(a["name"])
    opcion=int(input("Elige una opcion del menu: "))
    
  if opcion==3:
    respuesta=(input("Dime un nombre de la lista anterior: "))
    r=requests.get(url_base+categorias,params=parametros,headers=cabeceras)
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
          print(f"---PRECIO ACTUAL {divisa} ---")
          print(int(a.get("quote").get(divisa).get("price")))
          print("---VOLUMEN 24H---")
          print(int(a.get("quote").get(divisa).get("volume_24h")))
          print("---CAPITALIZACIÓN EN EL MERCADO---")
          print(int(a.get("quote").get(divisa).get("market_cap")))
      print(menu)
      opcion=int(input("Elige una opcion del menu: "))

  if opcion==4:
    break
