import requests
import re

url ='http://ggzyjy.sc.gov.cn/jyxx/002008/002008001/20201106/fd4a373a-0482-4b27-a2d5-5834be21290d.html'
req = requests.get(url)
str1 = req.content.decode('utf-8')
pet = '<font face=".*?"><u>(.*?)&ensp;&ensp;</u></font></span>'
haha = re.findall(pet,str1)
print(haha)