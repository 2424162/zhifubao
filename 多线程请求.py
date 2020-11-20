import requests
import threading
import time
num=0
url = ''
th_list = []
def haha():
    print("ha");

def post_url():
    global num

    data = {
        "userName": "wxid_h2n5ygoxw8pn12",
         "password": "eeeerr790",
         "data62": "62706c6973743030d4010203040506090a582476657273696f6e58246f626a65637473592461726368697665725424746f7012000186a0a2070855246e756c6c5f102037383566636331313032633432316335636633383730336439386333353433325f100f4e534b657965644172636869766572d10b0c54726f6f74800108111a232d32373a406375787d0000000000000101000000000000000d0000000000000000000000000000007f",
         "proxyIp": "",
         "proxyUserName": "",
         "proxyPassword": "",
    }
    url = 'http://193.112.183.247/api/Login/Data62Login'
    result = requests.post(url=url,json=data)
    print(result)
    num=num+1
    if num==60:
        time3 =time.time()
        print(time3-time1)
for i in range(60):
    th = threading.Thread(target=post_url)
    th_list.append(th)
time1 = time.time()
for th in th_list:
    th.start()
time2 = time.time()
print(time2-time1)
