import requests

parameter={"page":2}
resp = requests.get("https://reqres.in/api/users",params=parameter)
print(resp.url)

code = resp.status_code
# assert code == 200, "Code does not match"
json_response = resp.json()
print(json_response["total"])
assert json_response["total"] == 12, "total do not match"
print(json_response["total_pages"])
assert json_response["total_pages"] == 2, "total pages count is not matching"

print(json_response["data"][0]["email"])
assert (json_response["data"][0]["email"]).endswith("reqres.in"), "email format is not matching the correct"

print(json_response["data"][2]["last_name"])
assert (json_response["data"][2]["last_name"]) != None, "Last name is None"

print(json_response["support"]["url"])
# assert (json_response["data"][0]["first_name"]).endswith("gmail.com"),"email format is not matching the correct"
# print(resp.text)
# print(resp.content)
# print(resp.json())
# print(type(resp.headers))
# print(resp.headers)
# print(resp.cookies)
# print(resp.encoding)
# print(resp.url)
