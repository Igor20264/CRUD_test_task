import requests
import json
s = requests.post("http://localhost:8000/user/add",json.dumps({"name":"Jleb","password":"109"}))
id = int(s.text)
#s = requests.post("http://localhost:8000/user/checkname?username=hleb")
#s = requests.post("http://localhost:8000/user/getname?username=hleb")
#s = requests.get("http://localhost:8000/user/getall")
s = requests.delete(f"http://localhost:8000/user/{id}/{109}/del")
print(s.text)