import requests

url = 'https://app.kwaixiaodian.com/rest/app/grocery/product/self/midPage/list'
headers = {'Host': 'app.kwaixiaodian.com',
'Connection': 'keep-alive',
'Content-Length': '200',
'Accept': 'application/json',
'Origin': 'https://app.kwaixiaodian.com',
'Trace-Id': '1.66858969827253.607211286017.1604480694893.4',
'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; vivo X20A Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Kwai/6.9.2.11245 AliBaichuan(2014_0_23537706@baichuan_h5_0.1.1/6.9.2.11245) AllowKsCallApp',
'Content-Type': 'application/json;charset=UTF-8',
'Referer': 'https://app.kwaixiaodian.com/merchant/shop/list?id=715427034&webviewClose=false&biz=merchant&carrierType=3&from=profile&hyId=kwaishop',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie': 'mod=vivo%28vivo+X20A%29; lon=114.568329; country_code=CN; kpn=KUAISHOU; oc=GENERIC; egid=DFPED4FE0E1AEE83B87D6673972539527109872E36460819A468FBA650512E90; hotfix_ver=; sh=1600; max_memory=128; isp=CMCC; browseType=1; kpf=ANDROID_PHONE; net=WIFI; app=0; ud=0; c=GENERIC; sw=900; ftt=; language=zh-cn; iuid=; lat=25.997958; did_gt=1599889958395; ver=6.9; sys=ANDROID_5.1.1; appver=6.9.2.11245; did=ANDROID_4c1d96d144ad9668; token=; client_key=3c2cd3f3; kuaishou.api_st=; kuaishou.h5_st=; sid=4e1a9b21-904c-420c-954f-cb8861e7c4ba; mod=vivo%28vivo+X20A%29; lon=114.568329; country_code=CN; kpn=KUAISHOU; oc=GENERIC; egid=DFPED4FE0E1AEE83B87D6673972539527109872E36460819A468FBA650512E90; hotfix_ver=; sh=1600; max_memory=128; isp=CMCC; browseType=1; kpf=ANDROID_PHONE; net=WIFI; app=0; ud=0; c=GENERIC; sw=900; ftt=; language=zh-cn; iuid=; lat=25.997958; did_gt=1599889958392; ver=6.9; sys=ANDROID_5.1.1; appver=6.9.2.11245; did=ANDROID_4c1d96d144ad9668; token=; client_key=3c2cd3f3; kuaishou.api_st=; kuaishou.h5_st=; sid=4e1a9b21-904c-420c-954f-cb8861e7c4ba',
'X-Requested-With': 'com.smile.gifmaker'}
data = {"listProductParam":{"id":"495681329",
                            "webviewClose":"false",
                            "biz":"merchant",
                            "carrierType":"3",
                            "from":"profile","hyId":"kwaishop","visitorId":"0",
                            "clientVersion":"6.9.2.11245","clientId":2,"page":1}}

req  = requests.post(url=url,json=data,headers=headers)
print(req.content)