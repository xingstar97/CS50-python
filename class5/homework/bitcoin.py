import sys
import requests
import json

if len(sys.argv)!=2:
    sys.exit("MIssing command line arguments")

try:
    number = float(sys.argv[1])
except ValueError:
    sys.exit("Wrong input")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
    price = response["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    exit("Request error!")
#see explanation for request exception:
#https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module

print(f"${number*price:,.4f}")