import requests


https://47.113.123.126/wechat?method=addOrderRed&atId=2&num=1&remarks=xiaolaji&pid=2&day=2&payPassword=6677889900

url = "https://47.113.123.126/project"
headers ={'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Content-Length': '17',
'Content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
'Cookie': 'JSESSIONID=FA645EE13C98F0E30C8DFEC3C34032FA',
'Host': '47.113.123.126',
'Origin': 'https://47.113.123.126',
'Referer': 'https://47.113.123.126/project',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
data = {
'method': 'addOrderRed',
'atId': '2',
'num': '1',
'remarks': 'xiaolaji',
'pid': '2',
'day': '2',
'payPassword': '6677889900'
}

result = requests.post(url=url,headers=headers,data=data,verify = False)
print(result.text)