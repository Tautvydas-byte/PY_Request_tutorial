import requests

payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

resp = requests.post("https://reqres.in/api/register", data=payload)
print(resp)
print(resp.json()["token"])
