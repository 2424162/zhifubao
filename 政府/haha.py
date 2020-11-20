import requests
import urllib
url = "https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID=96636213&t=1604902267937&starttime=2020%2F11%2F9%2014%3A02%3A46&ktimes=181&rn=3065235275.26461396&hlv=1&jqnonce=2fdc6cfd-3eb5-4b44-bbc7-8b51b6bfd521&jqsign=3geb7bge%2C2dc4%2C5c55%2Cccb6%2C9c40c7cge430&jpm=17"
proxy = '113.194.28.190:9999'

proxies = {'http': '1.196.177.160:9999',
	    }


headers = {'Host': 'www.wjx.cn',
'Connection': 'keep-alive',
'Content-Length': '534',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': '*/*',
'Origin': 'https://www.wjx.cn',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://www.wjx.cn/jq/96636213.aspx',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': '.ASPXANONYMOUS=eCrfyO_s1gEkAAAANTc0ZTExYjItY2U1Ni00NDc1LWFhZGMtMzU2ZjU4NDExZGE0lQykDs3jFZZsEDFjvMgjaDMLxKw1; UM_distinctid=175ab998e5f4c-0e99029e2865f4-230346d-1fa400-175ab998e60f9; actidev_96636213=1; jpckey=%E5%AD%A6%E5%8E%86; acw_tc=76b20f6316049179663204489e7344878f5ef8e874c00bc888be08b88f4526; acw_sc__v2=5fa91ace285f3de55b55902cc1514eb21e8450bd; CNZZDATA4478442=cnzz_eid%3D768684781-1604898516-%26ntime%3D1604914716; LastActivityJoin=96636213,107722548049; join_96636213=1; jac96636213=60629012; SERVERID=2a2dcf6de1f5b497e80dc0f7231b4801|1604918093|1604917966; ssxmod_itna=YqAxuiiQDtE6dGHf747qDK4Y5KzTi7oO7OWx0H4i=rDSxGKidDqxBWmQ24FnD9Ga7FDBKW4Np7uNaq2A+hPWdFo1pxWqKjoRoDHxY=DUO7ieoD4RKGwD0eG+DD4DWDmm7DnxAQDj=5GWDmbCDWPDYxDr26KDRxi7DD5QGx07DQHCY4KwSrozKG74oe5D9OoDs6RE7e5mAf3Kx+R8DlK6DCKsSPy1W4Gd/iiFeerNqibFoieikD2iriWxFYedZ70PkG23dTeraWQB7DDWoGr4aCz44D==; ssxmod_itna2=YqAxuiiQDtE6dGHf747qDK4Y5KzTi7oO7ODn9gi40=Dl6704jb2Di=uoQqdUD6CO9X=SzrCYx1FDU7APwDEZkinsgAFuD0eu0QwpXGzc1qARf6D87KkcHvxZ4iAPsHy8U1dNqtXUXIM59CS=46+=ZtboZ74tpzLLntfL31jRA/8jP7fLsGmDHG3ADsrEsmMpetpx/e3YMWcofbwExf+3oT0PrbfR6QDLx+cp5K8Dg7SKN=GBxIfP/KiT5+f8bw8f4MeH8Wdh+i=fkTb89/EiTE9kaceR6GpSvvgKrKGUDoYvhHwi8SxYyYiMhsx2oKBdYqY9ohHb5c0QwohyqoAh+oBdjgFC2oiOwn8KFeYuLYqDzKAbAo+6fmWjYMqzarILjKiW3/OPCghBivOeqUiTErqUDd4gOUBaAjKXAxqOqtgAyYChAK3kFxLKhSKTEedcPmdYb8rmrsZrIHnkb4zCYm=joPhPzlYyY5ncLsRo9cmvE3dLfC2wbbQP3hhST6rdxCvWmK8m2YzXbjKydi2hIbRro3LLxR2jIlQd8nh8Cda/AwEdyGoIzHsEWoBeD7jhrHm3FZGxmcI6G2f8oeAwiCN48hsLerGnezwnjDFiw=GhtoEpLwIv9=ml8jGeSD8ey1r06HwUqKsnkCGK4Gq1mDzb0Spccyhjsqtxrdmw=74jXvSMravqe04DDLxD+hx4D===; ssxmod_ktimd=121',



}
data = {
'submitdata':'1%241%7D2%241%7D3%242%7D4%243%7D5%242%7D6%243%7D7%241%7D8%24-3%7D9%24-3%7D10%24-3%7D11%24-3%7D12%24-3%7D13%24-3%7D14%24-3%2C-3%2C-3%2C-3%7D15%24-3%2C-3%2C-3%7D16%24-3%2C-3%2C-3%2C-3%7D17%24-3%2C-3%2C-3%2C-3%7D18%24-3%2C-3%2C-3%7D19%24-3%2C-3%2C-3%7D20%24-3%2C-3%2C-3%7D21%24-3%2C-3%2C-3%7D22%24-3%2C-3%2C-3%2C-3%7D23%24-3%7D24%24-3%7D25%24-3%7D26%24-3%7D27%24-3%7D28%24-3%7D29%24-3%7D30%24-3%7D31%24-3%7D32%24(%E8%B7%B3%E8%BF%87)%7D33%24(%E8%B7%B3%E8%BF%87)%5E(%E8%B7%B3%E8%BF%87)%5E(%E8%B7%B3%E8%BF%87)%7D34%24-3%2C-3%2C-3v'
}
req = requests.post(url=url,headers = headers,data=data,proxies=proxies)
print(req.content)