import requests
import json

url = "https://www.behance.net/ekaterinatkach"
response = requests.get(url)
print(response)
