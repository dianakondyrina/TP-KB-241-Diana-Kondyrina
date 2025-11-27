import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

data = response.json()

allowed = ["EUR", "USD", "PLN"]
currency = input("Оберіть валюту (EUR, USD, PLN): ").upper()

while currency not in allowed:
    currency = input("Невірна валюта. Введіть EUR, USD або PLN: ").upper()

amount = float(input("Введіть суму: "))

rate = None
for elem in data:
    if elem["cc"] == currency:
        rate = elem["rate"]
        break

result = amount * rate

print(f"{amount} {currency} = {result:.2f} UAH")