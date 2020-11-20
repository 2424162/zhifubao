import requests
import hashlib

url = "https://apissl.ksapisrv.com/rest/n/search/new"

url2 = 'https://apissl.ksapisrv.com/rest/n/search/new?mod=samsung%28SM-N960F%29&lon=111.569385&country_code=CN&kpn=KUAISHOU&oc=GENERIC&egid=DFPB79348F6815E472D4636BD3B0C7C87D59E73A3936957B10D6D353A75EDE44&hotfix_ver=&sh=1600&appver=6.9.2.11245&max_memory=128&isp=CMCC&browseType=1&kpf=ANDROID_PHONE&did=ANDROID_dcdd918e3fa28010&net=WIFI&app=0&ud=1942009504&c=GENERIC&sys=ANDROID_5.1.1&sw=900&ftt=&language=zh-cn&iuid=&lat=32.999172&did_gt=1587967311124&ver=6.9'
salt = '382700b563f4'
str = 'app=0appver=6.9.2.11245browseType=1c=GENERICclient_key=3c2cd3f3country_code=CNdid=ANDROID_dcdd918e3fa28010did_gt=1587967311124egid=DFPB79348F6815E472D4636BD3B0C7C87D59E73A3936957B10D6D353A75EDE44fromPage=1ftt=hotfix_ver=isp=CMCCiuid=keyword=hahahakpf=ANDROID_PHONEkpn=KUAISHOUkuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSsAEaOo83D4pnaDKp62DuAlFBH_nuSQJbo8xzPsPeHLclukT6dMc7W6dnO9X06jAG2VX4BUzgQinI7ymrer3iMqz0Wkb8a9BUN3XRJSveGT4W6uggoTCLnZXHm-h5id0gFNWp5aZ5qLduxVW5FDWaufDVGnLsDUHkBkUCyB9Br9Kp-sraF5zrXEkGZEg--Qo5UPXH6n_GlaAJe4nryb8cJuHDSmnqUZfCusLWYKNxRtfUxBoSZkJiZF_qSRKoI0G7Sb9VLlZMIiB3AQfCPQ435Osl2Dy22qQKkfiu4c6nsiPLGJTbr-DahCgFMAElanguage=zh-cnlat=32.999172lon=111.569385max_memory=128mod=samsung(SM-N960F)net=WIFIoc=GENERICos=androidrelatedTab=sh=1600sw=900sys=ANDROID_5.1.1token=dbab2874c8884c75a852cb496ede6d2a-1942009504ud=1942009504ver=6.9'+salt
m = hashlib.md5(str.encode())
sig = m.hexdigest()
data = {'keyword': 'hahaha',
'relatedTab': '',
'fromPage': '1',
'__NS_sig3': '2195620579c67e5c17f4866a1504d440dd468de54a',
'__NStokensig': '64bf67e6e2d8fe93a91e91e4c9dc575034f69fc636ed31ebaaefbfceafffd90b',
'kuaishou.api_st': 'Cg9rdWFpc2hvdS5hcGkuc3QSsAEaOo83D4pnaDKp62DuAlFBH_nuSQJbo8xzPsPeHLclukT6dMc7W6dnO9X06jAG2VX4BUzgQinI7ymrer3iMqz0Wkb8a9BUN3XRJSveGT4W6uggoTCLnZXHm-h5id0gFNWp5aZ5qLduxVW5FDWaufDVGnLsDUHkBkUCyB9Br9Kp-sraF5zrXEkGZEg--Qo5UPXH6n_GlaAJe4nryb8cJuHDSmnqUZfCusLWYKNxRtfUxBoSZkJiZF_qSRKoI0G7Sb9VLlZMIiB3AQfCPQ435Osl2Dy22qQKkfiu4c6nsiPLGJTbr-DahCgFMAE',
'token': 'dbab2874c8884c75a852cb496ede6d2a-1942009504',
'client_key': '3c2cd3f3',
'os': 'android',
'sig': sig,
}

result = requests.post(url = url2,data=data)
print(result.url)
print(result.headers)
print(result.text)
