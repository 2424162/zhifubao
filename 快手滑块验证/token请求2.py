import requests
import json

url = 'https://app.m.kuaishou.com/rest/wd/captcha/verify'
headers = {
'Host': 'app.m.kuaishou.com',
'Connection': 'keep-alive',
'Content-Length': '432',
'Accept': 'application/json',
'Origin': 'https://app.m.kuaishou.com',
'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SKW-A0 Build/LMY49I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 Kwai/6.9.2.11245',
'Content-Type': 'application/json; charset=UTF-8',
'Referer': 'https://app.m.kuaishou.com/verify/captcha.html?key=-7040463337507093132&type=7&uri=%2Frest%2Fn%2Fsearch%2Fnew',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,en-US;q=0.8',
'Cookie': 'mod=blackshark%28SKW-A0%29; lon=116.41025; country_code=cn; kpn=KUAISHOU; oc=GENERIC; egid=DFP1780926497C850F66E6B5F42508CEE26B65EBBD9172EA2D81EF8D44332619; hotfix_ver=; sh=1600; max_memory=192; isp=CMCC; browseType=1; kpf=ANDROID_PHONE; net=WIFI; app=0; ud=1942009504; c=GENERIC; sw=900; ftt=; language=zh-cn; iuid=; lat=39.916411; did_gt=1594347299450; ver=6.9; sys=ANDROID_5.1.1; appver=6.9.2.11245; did=ANDROID_d55ba519b285fe7d; token=46d50fb3c83d4dc8bb85e19be3be0d02-1942009504; client_key=3c2cd3f3; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSsAEdr8SsZFxgcrM03xxXBgcuefpD5pNrNn02hdQo_TQHYvnnmRTp-7_U5LjDVMU7jjgsvOleO4fWizEa_VUcOobHyOTTojMJL34CbBzjj1Du-5EqwalIfUJr8kpVqRRxur8ih2lsS6_R-55A2w_zwSeqVx4LOeTIhCDnBYTh_9oDanYaL3a9QDfPwElkoc5yXV2iJ4Wa3ut-sLQJBmx3RK7XhPzeL0NQh2W4-cTkzPDA5RoSzJ1EdK8FSN6I7LecEi4lYncRIiAk5CM2qLyviTACHlUS4p-F_UFl7HJ6A1PfSMaCyU75figFMAE; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAVTHWK2zzrIJPg8Q9EUVlG6c3UfGE11ea_AvULIKHj7MSMJFFir6NiR6jFj8Lwbsbvw6rvYVfXpZFEt9um4BTgS8UQpAm3r7wG-W-DFU3ilr6vML8bzyOyapSimHCfq-M00mU-cm3B4co9R6eXvOksHwUtMhXl7bUSGAN69GYdT8M6xAKq2J8PB30ZeIE3tZ806en-c_KWbmkL1vOgpBcJcaEuVzrJwrjFciNLdDbMoI5SeMUyIgcNO-Hpcgf_xqvlVrfLNe20WOe7GRPryP-4z5SeFHlcwoBTAB; sid=26c7c677-9f13-42a5-9d86-7bbcb9a45e75; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1594347894; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1594437265',
'X-Requested-With': 'com.smile.gifmaker',
}
data1 = {"type":"7",
         "uri":"/rest/n/search/new",
         "key":"-7040463337507093132",
         "input":"HEADCgp6dC5jYXB0Y2hhEt0BGxNi60UA_reU85Y7Ul-YQB4UreICWvpFXkkOe5ZTOw88NQhUZtuQd1kGl9ysiu4vLTNoftMny7ayWIRJS3cGOHcwmw27AnRbSA-ujooNZti3jqvJ-l6PU84QfC0iMFc7ShELy65nZIGdLwVJ9Mn6HB6a7HPBrbCtmejaEObj572j7uoC5noHpC9Ag0jEZH70KldKP2eVLgWAMfNF3EecadvSg7EARxtLAhha7RGZ-mi19hfbdFDokBRiGuaau8xE3Mfhowi9ul61lNTefqht8mv33W0Y17Io6XM0sqsaEuWSv3wG-CEzAb7RkgAiCsnppCgFMAITAIL"}

print('kaishi')
req = requests.post(url=url,headers=headers,json=data1).text
print(req)

