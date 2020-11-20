import requests
import urllib3
import urllib


url = "https://v.kuaishou.com/8Uz5Ay"
url2 = "https://www.ontarioimmigration.gov.on.ca/register_enu/dynamicform/register/launch/JOID"
#re = requests.request(method='get' ,url=url,headers = headers,allow_redirects=True)
http = urllib3.PoolManager()
r = http.request("GET",url2,redirect=False)
print(r.status)
print(r.headers['Location'])


