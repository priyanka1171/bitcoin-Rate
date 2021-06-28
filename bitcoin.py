import requests
try:
	wa="https://api.coindesk.com/v1/bpi/currentprice.json"
	res=requests.get(wa)
	print(res)        #200 okk

	data=res.json()
	print(data)

	usd_rate=data['bpi']['USD']['rate']
	print("Usd rate : ",usd_rate)

	gbp_pri=data['bpi']['GBP']['rate']   #write a code to find the rate in GBP ans EUR
	print("GBP : ",gbp_pri)
	
	eur_pri=data['bpi']['EUR']['rate']
	print("EUR : ",eur_pri)
except Exception as e:
	print("Issue",e)