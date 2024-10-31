import requests

swiss_request = requests.get("https://www.homegate.ch/rent/apartment/country-switzerland/matching-list")
swiss_request.encoding = 'utf-8'
print(f"Status code of swiss: {swiss_request.status_code}")

print("Done.")