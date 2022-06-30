import requests

payload = {
	"name": "Mukesh",
	"job": "automation"
}

resp = requests.post("https://reqres.in/api/users", data=payload)
print(resp)
print(resp.json())
assert resp.json()["job"] == "automation"
