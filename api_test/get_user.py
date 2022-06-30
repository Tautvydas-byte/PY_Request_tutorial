import requests

resp = requests.get("https://reqres.in/api/users?page=2")

code = resp.status_code
assert  code == 200, "Code does not match"
