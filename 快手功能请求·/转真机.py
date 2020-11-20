import requests
import hashlib

url = "https://apissl.ksapisrv.com/rest/n/search/new"

url2 = 'https://apissl.ksapisrv.com/rest/n/search/new?mod=Xiaomi%28MI%20NOTE%20LTE%29&lon=103.851351&country_code=cn&kpn=KUAISHOU&oc=XIAOMI&egid=DFPA173EA3BB8BE85E22CD7934EF7096B4144B61F96851209165B24819A8171E&sbh=55&hotfix_ver=&sh=1920&appver=7.5.50.14809&nbh=0&socName=Qualcomm%20MSM8974PRO-AC&newOc=XIAOMI&max_memory=128&isp=CUCC&kcv=193&browseType=4&kpf=ANDROID_PHONE&ddpi=440&did=ANDROID_dcdd918e3fa28010&net=WIFI&app=0&ud=1942009504&c=XIAOMI&sys=ANDROID_6.0.1&sw=1080&ftt=&ll=CTgQkgVMDD5AEa6a54h89llA&language=zh-cn&darkMode=false&iuid=&lat=30.048035&did_gt=1594796731736&ver=7.5'


salt = '382700b563f4'
str = 'app=0appver=6.9.2.11245browseType=1c=GENERICcancel=0client_key=3c2cd3f3country_code=CNdid=ANDROID_dcdd918e3fa28010did_gt=1587967311124egid=DFP16863507F58375C1E2BB942E29871964A9F84EC7038A5835B26F0E00B6DE3expTagList=CkgKQ2ZlZWRfcGhvdG98NTI1MTE5NzE5NzM4NDQ1MTcyNnwxMDA5Mjg2NTV8MV9pLzIwMDAwNzM4ODA2MjY4MzM3MTRfcDASATE=exp_tag0=exp_tag=1_i/2000073880626833714_p0ftt=hotfix_ver=isp=CMCCiuid=kpf=ANDROID_PHONEkpn=KUAISHOUkuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHkJlS_ajLHzGDzSJPxFhQuzQADae96bRnP4uDzr__YYLvjhUhagLtUUWCHlwBeDHWEzTQH00CdeTQLal6PJIWRcDXOoxs3lMZePlE6EYLdKNJMM0HHBf6kSRNuQ3I0FrvR3zbLU24GVWKf2fNFjqL2g-OdFOZ2MBp7xyk2L0Mz68QPo5dc16Tsweh6Mg0c8ZUJpVUax3Z_JK1q2GdRYHG_GhJPQv6ZTt1N5roF-otIWYG6ZJsiIPILxRzEZTkasZ6Mzmi9hDXDVjBd-B2zDUMm8iU25cEVKAUwAQlanguage=zh-cnlat=30.998763lon=108.567809max_memory=128mod=samsung(SM-N960F)net=WIFIoc=GENERICos=androidphoto_id=5251197197384451726photoinfo=100928655/_referer=ks://photo/100928655/5251197197384451726/3/1_i/2000073880626833714_p0#likeserverExpTag=feed_photo|5251197197384451726|100928655|1_i/2000073880626833714_p0sh=1600sw=900sys=ANDROID_5.1.1token=b5b832d5addd48c5889ee2b35d91a13d-1222084156ud=1222084156user_id=100928655ver=6.9'+salt
m = hashlib.md5(str.encode())



data = {'keyword': '啦啦',
'relatedTab': '',
'fromPage': '1',
'fromPageSessionId': '',
'queryId': '5ZWm5ZWmMTk0MjAwOTUwNDE1OTQ3OTcxMHcyNDAw',
'requestTabId': '',
'isRecoRequest': 'false',
'__NS_sig3': '2193793499da907beaa50199adef8f1c30f7352ed9',
'__NStokensig': 'f4df55e1710d2b6caa204200e373f32d416688edc09ba36049b313463799dc07',
'kuaishou.api_st': 'Cg9rdWFpc2hvdS5hcGkuc3QSsAEy1FUY_TH_3rRepTbKYmEwckGNi3BlypuWOyNtmWEhg52in9nSDkKxHwTdlqi8ziLqh79sA1YC9KcS3QKtJug2OimAsAmIXXgOH-DpUvYqGxdln0zlOJTkn6k34mSzqoxvi7bWB-EbjDl_I8GE-2mIZaKHQtk53iww4GntIF4_4OX3PE5jHl59S787qCzKyek0H6zoae11jmEt_MLhCfgGffqi7vmcXsmr2qrgeB7qCBoSZrSx75uARgqG_U7lMEEdWfwaIiD1jW_QCS2_a-F6IhdmZ_y41MnhWmQV84hnDI_1PML8oigFMAE',
'token': '0c49e124bdfb4a66baa9c202c5ac1037-1942009504',
'client_key': '3c2cd3f3',
'startSessionId': 'e877ada5-d39b-4413-99a3-dc4ad7c8bc86',
'os': 'android',
'sig': '5f6be79eaf78d5de32b9bff122d6866e',
}

result = requests.post(url = url2,data=data)
print(result.url)
print(result.headers)
print(result.text)
