import requests

url = 'https://ep.vpn.cn/Util/sendCode.html'

pic_url = "https://ep.vpn.cn/Util/verify.html"

url2 = 'https://ep.vpn.cn/Customer/reg/id/1.html'
headers = {

'Host': 'ep.vpn.cn',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'no-cors',
'Sec-Fetch-Dest': 'image',
'Referer': 'https://ep.vpn.cn/Customer/reg/id/1.html',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'PHPSESSID=2fdesph40me817robhvf38lqa1',
}
data = {
'code':'',
    'username':'17721836656',
    'type':'1'

}

data2 = {

    'form_token':'',
    'username':'17652141929',
    'capcha':'namn',
    'code':'9199',
    'password':'',
    'agreement':'on'
}
result = requests.post(url=url2,headers = headers,data = data2)
haha = result.json()
print(haha)