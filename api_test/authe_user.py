import requests

res=requests.get("https://the-internet.herokuapp.com/basic_auth",auth=('username','pass'))
res1=requests.get("https://the-internet.herokuapp.com/basic_auth",auth=('admin','admin'))
print(res.status_code)
print(res1.status_code)

#http://the-internet.herokuapp.com/
#https://requests.readthedocs.io/en/latest/user/authentication/#oauth-1-authentication