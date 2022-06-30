import requests

resp = requests.get("https://reqres.in/api/users?page=2")

code = resp.status_code
assert code == 200, "Code does not match"

# print(resp.text)
# print(resp.content)
# print(resp.json())
# print(type(resp.headers))
# print(resp.headers)
# print(resp.cookies)
# print(resp.encoding)
# print(resp.url)