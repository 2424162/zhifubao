import requests
import hashlib

url = "https://apissl.ksapisrv.com/rest/n/search/new"

url2 = 'http://api3.gifshow.com/rest/n/search/new?mod=Xiaomi%28MI%20NOTE%20LTE%29&lon=103.85135&country_code=cn&kpn=KUAISHOU&oc=GENERIC&egid=DFP7A28F2E28B8445FB1CFC15CD8D6F7BE6231EE5209B81DFB9654569AB09147&hotfix_ver=&sh=1920&appver=6.9.2.11245&max_memory=128&isp=CUCC&browseType=1&kpf=ANDROID_PHONE&did=&net=WIFI&app=0&ud=1942009504&c=GENERIC&sys=ANDROID_6.0.1&sw=1080&ftt=K-T-T&language=zh-cn&iuid=&lat=30.047985&did_gt=1595038232671&ver=6.9'


salt = '382700b563f4'
str = 'app=0appver=6.9.2.11245browseType=1c=GENERICclient_key=3c2cd3f3country_code=cndid=did_gt=1595038232671egid=DFP7A28F2E28B8445FB1CFC15CD8D6F7BE6231EE5209B81DFB9654569AB09147fromPage=1ftt=K-T-Thotfix_ver=isp=CUCCiuid=keyword=六六六kpf=ANDROID_PHONEkpn=KUAISHOUkuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSsAHQGSJokveL1l172Uy_XxmAxBNAteBqMdoHXAi5O-ay88NiHqBn28aafMPspsj4F6Vho9kapL5AsV1sc4ZK56dvICXxP-Cf8yIDDq2qYPwXQk5FWlmsvngw8L1JDIJ4S7g9Qsi4i-UQpGC1NwTlX1w00vb7o-d_kE8V0oEE5IgGoGjSZwJu2akmzR9cZofGF2dGIFwXD9fQNFiPhUKRcIGGjKFdPU6SSTE_poTHulxEHRoSZkJiZF_qSRKoI0G7Sb9VLlZMIiCXvPYy0BEv89YxBN9nIpkCP28rrUy6GArqBV4qgN4BkCgFMAElanguage=zh-cnlat=30.047985lon=103.85135max_memory=128mod=Xiaomi(MI NOTE LTE)net=WIFIoc=GENERICos=androidrelatedTab=sh=1920sw=1080sys=ANDROID_6.0.1token=1801aa80f3d6418a93334401b1cb002f-1942009504ud=1942009504ver=6.9'+salt
m = hashlib.md5(str.encode())
sig = m.hexdigest()



data = {'keyword': '六六六',
'relatedTab': '',
'fromPage': '1',
'__NS_sig3': '2195612689c67adeefaa04c74d653f4cb9796ea131',
'__NStokensig': '20b0e6ca9bbf37776cbf7d84aaa4fc6f99a61628c8c0d57aea2ddb046ee69138',
'kuaishou.api_st': 'Cg9rdWFpc2hvdS5hcGkuc3QSsAHQGSJokveL1l172Uy_XxmAxBNAteBqMdoHXAi5O-ay88NiHqBn28aafMPspsj4F6Vho9kapL5AsV1sc4ZK56dvICXxP-Cf8yIDDq2qYPwXQk5FWlmsvngw8L1JDIJ4S7g9Qsi4i-UQpGC1NwTlX1w00vb7o-d_kE8V0oEE5IgGoGjSZwJu2akmzR9cZofGF2dGIFwXD9fQNFiPhUKRcIGGjKFdPU6SSTE_poTHulxEHRoSZkJiZF_qSRKoI0G7Sb9VLlZMIiCXvPYy0BEv89YxBN9nIpkCP28rrUy6GArqBV4qgN4BkCgFMAE',
'token': '1801aa80f3d6418a93334401b1cb002f-1942009504',
'client_key': '3c2cd3f3',
'os': 'android',
'sig': sig,
}
result = requests.post(url = url2,data=data)
print(result.url)
print(result.headers)
print(result.text)
