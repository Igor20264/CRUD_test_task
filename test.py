import time
import random
import requests
import json
import threading

import unittest


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        self.name = str(random.randint(1,1000))
        self.password = str(random.randint(1000000,999999999))
        self.data = 0

    def tearDown(self) -> None:
        pass

    def testA(self):
        s = requests.post("http://localhost:8000/user/add",json.dumps({"name":self.name,"password":self.password}))
        self.data = id = s.json()["user_id"]
        assert type(id) == int
    
    def testB(self):
        s = requests.post(f"http://localhost:8000/user/checkname?username={str(random.randint(1,1000))}")
        self.id = s.json()
        assert type(self.id)== bool

    def testC(self):
        s = requests.post(f"http://localhost:8000/user/getid?username={self.name}")
        id = s.json()
        print(id,type(id))
        assert type(id)
    
    def testD(self):
        s = requests.get("http://localhost:8000/user/getall")
        id = s.json()
        assert type(id) == list

    def testE(self):
        s = requests.get(f"http://localhost:8000/user/{self.data}/get_reg_time?password={self.password}")
        id = s.json()
        print(id)
        assert type(id)

    def testE(self):
        s = requests.put(f"http://localhost:8000/user/{id}/reset_password?created={time}&password={self.password}")
        id = s.json()
        print(id)
        assert type(id)

    
    



#s = requests.post("http://localhost:8000/user/add",json.dumps({"name":str(random.randint(1,1000)),"password":"1009"}))
#id = s.json()
#print(id,type(id))
#s = requests.post("http://localhost:8000/user/checkname?username=hleb")
#s = requests.post("http://localhost:8000/user/getname?username=hleb")
#s = requests.get("http://localhost:8000/user/getall")
#print(s.text)
#s = requests.get(f"http://localhost:8000/user/{id}/get_reg_time?password=1009")
#print(s.text)
#time = int(s.text)
#s = requests.put(f"http://localhost:8000/user/{id}/reset_password?created={time}&password=Вух")
#s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660}))
#book_id = 13
#s = requests.post(f"http://localhost:8000/booking/add",json.dumps({"user_id":id,"start":int(time.time()),"end":int(time.time())+3660,"comment":"3 место с права"}))
#print(s.text)

#s = requests.delete(f"http://localhost:8000/booking/{id}/{book_id}/del?password=1009")
#print(s.text)

#s = requests.put(f"http://localhost:8000/booking/{id}/{book_id+1}/update?password=1009",json.dumps({"user_id":id,"start":0,"end":int(time.time()),"comment":"3-тичное место с права"}))
#print(s.text)
'''
s = requests.get(f"http://localhost:8000/booking/{id}/getall")
print(s.text)

s = requests.delete(f"http://localhost:8000/user/{id}/del?password=1009")
print(s.text)

s = requests.get(f"http://localhost:8000/booking/{id}/getall")
print(s.text)'''

if __name__ == "__main__":
    unittest.main() # run all tests