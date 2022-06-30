import requests

req=requests.get("https://httpbin.org/delay/3",timeout=5)
# req=requests.get("https://httpbin.org/delay/5",timeout=3)

print(req.status_code)
