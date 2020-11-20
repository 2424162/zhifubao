import re

path = 'resutl.html'
f = open(path,"r",encoding='utf-8')
cc = f.read()
uuid = re.findall('uuid: "(.*?)"',cc)
print(uuid[0])
