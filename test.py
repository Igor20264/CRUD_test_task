import time

import requests
import json
s = requests.post("http://localhost:8000/user/add",json.dumps({"name":"3Дea5da0sd5asdeb","password":"1009"}))
id = int(s.text)
#s = requests.post("http://localhost:8000/user/checkname?username=hleb")
#s = requests.post("http://localhost:8000/user/getname?username=hleb")
#s = requests.get("http://localhost:8000/user/getall")

#s = requests.get(f"http://localhost:8000/user/{id}/get_reg_time?password=1009")
#print(s.text)
#time = int(s.text)
#s = requests.put(f"http://localhost:8000/user/{id}/reset_password?created={time}&password=Вух")
#s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660}))
book_id = 13
s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660,"comment":"3 место с права"}))
print(s.text)
s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660,"comment":"3 место с права"}))
print(s.text)
s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660,"comment":"3 место с права"}))
print(s.text)
s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660,"comment":"3 место с права"}))
print(s.text)
s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660,"comment":"3 место с права"}))
print(s.text)
s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660,"comment":"3 место с права"}))
print(s.text)
s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660,"comment":"3 место с права"}))
print(s.text)
s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660,"comment":"3 место с права"}))
print(s.text)
s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660,"comment":"3 место с права"}))
print(s.text)
s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660,"comment":"3 место с права"}))
print(s.text)
s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660,"comment":"3 место с права"}))
print(s.text)

#s = requests.delete(f"http://localhost:8000/booking/{id}/{book_id}/del?password=1009")
#print(s.text)

#s = requests.put(f"http://localhost:8000/booking/{id}/{book_id+1}/update?password=1009",json.dumps({"user_id":id,"start":0,"end":int(time.time()),"comment":"3-тичное место с права"}))
#print(s.text)

s = requests.get(f"http://localhost:8000/booking/{id}/getall")
print(s.text)

s = requests.delete(f"http://localhost:8000/user/{id}/del?password=1009")
print(s.text)

s = requests.get(f"http://localhost:8000/booking/{id}/getall")
print(s.text)