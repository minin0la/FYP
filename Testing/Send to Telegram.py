import requests

content = {"value1":"Ok it is working"}
requests.post("https://maker.ifttt.com/trigger/FridgeBud_Item/with/key/d9O5pfQ2QslLb8AHONzshC", json=content)