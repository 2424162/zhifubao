import requests

url  = 'http://pic.netbian.com/downpic.php?id=23424&classid=60'
res = requests.get(url=url)
print(res.content)
f = open('蜘蛛侠.jpg','wb')
f.write(res.content)