import requests
import json
s = requests.post("http://localhost:8000/user/add",json.dumps({"name":"3Дea5d5eb","password":"1009"}))
id = int(s.text)
#s = requests.post("http://localhost:8000/user/checkname?username=hleb")
#s = requests.post("http://localhost:8000/user/getname?username=hleb")
#s = requests.get("http://localhost:8000/user/getall")
#s = requests.delete(f"http://localhost:8000/user/{19}/del?password=109")
print(id)
s = requests.get(f"http://localhost:8000/user/{id}/get_reg_time?password=1009")
print(s.text)
time = int(s.text)
s = requests.put(f"http://localhost:8000/user/{id}/reset_password?created={time}&password=Вух")

print(s.text)
