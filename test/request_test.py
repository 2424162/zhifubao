import requests
import re
import urllib3
path = "C:\\Users\\二筒\\Desktop\\"


sh_url = '这是一只聪明的猫猫 https://v.kuaishou.com/899TWH 复制此消息，打开【快手】直接观看！'
pat = " https:\/\/v.kuaishou.com\/(.*?) "
res = re.findall(pat,sh_url)
url  = "https://v.kuaishou.com/"+res[0]
http = urllib3.PoolManager()
r = http.request("GET", url, redirect=False)

str = r.headers["Location"]
print(str)
print(r.read())
pat1 = '&userId=(.*?)&'
pat2 = 'hareObjectId=(.*?)&'

exp_pat = "&et=(.*?)&"
exp = re.findall(exp_pat, str)
exp_tag = exp[0].replace('%2F', '/')
print(exp_tag)


web_userid = re.findall(pat1,str)
workpage_id = re.findall(pat2,str)
print(web_userid[0])
print(workpage_id[0])
