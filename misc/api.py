import requests
import json

URL="https://randomuser.me/api/"

res=requests.get(URL)
# print(res.status_code)

# loading into dictionary
data=json.loads(res.text)
name = data["results"][0]["name"]["first"]