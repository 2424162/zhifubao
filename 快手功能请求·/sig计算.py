import requests
import hashlib
from urllib import parse

url = 'https://apissl.ksapisrv.com/rest/n/relation/follow?'

headers1 = {'mod': 'vivo(vivo X20A)',
            'lon': '115.569574',
            'country_code': 'CN',
            'kpn': 'KUAISHOU',
            'oc': 'GENERIC',
            'egid': 'DFP6D4CD0CA45A27D791D37D2FF6DE72A067885552254A33B89E76888361C1F1',
            'hotfix_ver': '',
            'sh': '1600',
            'appver': '6.9.2.11245',
            'max_memory': '128',
            'isp': 'CMCC',
            'browseType': '1',
            'kpf': 'ANDROID_PHONE',
            'did': 'ANDROID_4c1d96d144ad9668',
            'net': 'WIFI',
            'app': '0',
            'ud': '1942009504',
            'c': 'GENERIC',
            'sys': 'ANDROID_5.1.1',
            'sw': '900',
            'ftt': '',
            'language': 'zh-cn',
            'iuid': '',
            'lat': '39.001975',
            'did_gt': '1599889958395',
            'ver': '6.9',
            }
headers = {'mod': 'OPPO(OPPO R17)',
           'lon': '115.569574',
           'country_code': 'CN',
           'kpn': 'KUAISHOU',
           'oc': 'GENERIC',
           'egid': 'DFP4084137FA96075CC14A391BB509C31FA50EC9D2CFCA8980AD53AFA7C8BFCF',
           'hotfix_ver': '',
           'sh': '1600',
           'appver': '6.9.2.11245',
           'max_memory': '128',
           'isp': 'CMCC',
           'browseType': '1',
           'kpf': 'ANDROID_PHONE',
           'did': 'ANDROID_4c1d96d144ad9668',
           'net': 'WIFI',
           'app': '0',
           'ud': '0',
           'c': 'GENERIC',
           'sys': 'ANDROID_5.1.1',
           'sw': '900',
           'ftt': '',
           'language': 'zh-cn',
           'iuid': '',
           'lat': '39.001975',
           'did_gt': '1597479943975',
           'ver': '6.9',
           }

hah = {'sig': '8b27e3f9468ba46cd7db0ed5b1b9805a',
       '__NStokensig': '8195ec10fc8dee260771269fc368bd9d225b65ca528b6708123ec3fc51d1d83c',
       'kuaishou.api_st': 'Cg9rdWFpc2hvdS5hcGkuc3QSsAGou1xOHouy0GmFez_x1ed9cAOnpgSgjyVSFrrcmKVRe-8OgzoE3K91NemVL53caxmpTUWj1SdaawUbLCHCfTY5Q-QGIDXBrClB060nZMpQrVly0E9t4evD6kUnUo2LKMHhIh7Cg4pvfC32pUnoY--5kfL0_3J1d9AO_up1Lgd_klML0U0PEORbWwBNfEA-mo3LR-7gKIRvNThq61rwW8Tou82ciFClP-Us1zYRpDEKPhoS7NSeMi9xTlycVoW3yFZ8L6XpIiCnLkdfYULFmFAj7PakBeeidmrHc-GOdmhgemKCa_ZhqSgFMAE',
       'token': 'bc96393279ce409aa51a97e1338308ab-1942009504', 'client_key': '3c2cd3f3', 'os': 'android',
       'touid': '5192931883290214269', 'ftype': '1', 'act_ref': '5192931883290214269_2051658227_p6', 'page_ref': '16',
       'referer': 'ks://photo/5192931883290214269/2051658227/3/1_i/1_i/2000109797021177153_f102#follow',
       'exp_tag0': '_', 'exp_tag': '1_i/2000109797021177153_f102',
       'expTagList': 'CksKRmZlZWRfcGhvdG98NTE5MjkzMTg4MzI5MDIxNDI2OXwyMDUxNjU4MjI3fDFfaS8yMDAwMTI4MjI1ODkyOTE3OTM4X2YxMDISATE=',
       'photoinfo': '_/_', 'followSource': '0'}

sig_data = {'touid': '144033776',
            'ftype': '1',
            'act_ref': '144033776_52174201942859552_p9',
            'page_ref': '8',
            'referer': 'ks://photo/144033776/52174201943929552/3/1_i/20001094818220673_h30#follow',
            'exp_tag0': '_',
            'exp_tag': '1_i/200010948918220673_h30',
            'expTagList': 'CksKRmZlZWRfcGhvdG98NTIxNzQyMDE5NDM5Mjg1OTU1MnwxNDQwMzM3NzZ8MV9pLzIwMDAxMDk0ODk4MTgyMjA2NzNfaDMwNTISATEKSwpGZmVlZF9waG90b3w1MjE3NDIwMTk0MzkyODU5NTUyfDE0NDAzMzc3NnwxX2kvMjAwMDEwOTQ4OTgxODIyMDY3M19oMzA1MhIBMQ==',
            'photoinfo': '_/_',
            'followSource': '0',
            'client_key': '3c2cd3f3',
            'os': 'android',
            'kuaishou.api_st': 'Cg9rdWFpc2hvdS5hcGkuc3QSsAGou1xOHouy0GmFez_x1ed9cAOnpgSgjyVSFrrcmKVRe-8OgzoE3K91NemVL53caxmpTUWj1SdaawUbLCHCfTY5Q-QGIDXBrClB060nZMpQrVly0E9t4evD6kUnUo2LKMHhIh7Cg4pvfC32pUnoY--5kfL0_3J1d9AO_up1Lgd_klML0U0PEORbWwBNfEA-mo3LR-7gKIRvNThq61rwW8Tou82ciFClP-Us1zYRpDEKPhoS7NSeMi9xTlycVoW3yFZ8L6XpIiCnLkdfYULFmFAj7PakBeeidmrHc-GOdmhgemKCa_ZhqSgFMAE',
            'token': 'bc96393279ce409aa51a97e1338308ab-1942009504',
            }


def getNsTokenSig(sig):
    token_salt = '7d354f8ea4440a5c7f6344a1ba4f4650'
    str3 = sig + token_salt
    cc = bytearray(str3.encode())
    nstokensig = hashlib.sha256(bytearray(str3.encode())).hexdigest()
    return nstokensig


#
# workpage_follow_data = {
#
# }
# sig_data.update(workpage_follow_data)

def sig_and_headers():
    sig_str = ""
    url_headers = {}
    head = list(headers)
    sig_key = headers
    sig_key.update(sig_data)
    key = sorted(list(sig_key))
    for i in range(0, len(key)):
        if key[i] == 'exp_tag0':
            print(i)
            print(key[i])
            key[i], key[i - 1] = key[i - 1], key[i]

    for i in key:
        sig_str = sig_str + i + "=" + sig_key[i]

    print(sig_str)

    salt = '382700b563f4'

    # sig_str =  "app=0appver=6.9.2.11245browseType=1c=GENERICcancel=0client_key=3c2cd3f3country_code=CNdid=ANDROID_4c1d96d144ad9668did_gt=1599889958395egid=DFP6D4CD0CA45A27D791D37D2FF6DE72A067885552254A33B89E76888361C1F1expTagList=CkkKRGZlZWRfcGhvdG98NTIxNzk4MzE1NjA1NDAzNzQ0MXw0MzQwNjYxMzB8MV9pLzIwMDAxMDg5NjgyNTMzODk3NDVfZjgwEgExexp_tag0=exp_tag=1_i/2000108968253389745_f80ftt=hotfix_ver=isp=CMCCiuid=kpf=ANDROID_PHONEkpn=KUAISHOUkuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSsAG5GvWs4OJAvbVMPm6ZsKqth1gYVPaM1zZAw7qFlYhb5BlRHgowGNGAb4FcOrA9NStTcAcJ8OlHsAt2zyFifSxJVN5tF-7I1rrMabDFUXQyv0J8_gnDKDoj3LT8mre_yYqZ9FniTJqWo2FOKewULyJTBWLB49pNcM0sGOuXZXMKGiyaqaS8urICD-rArkLhN_dZce2xk7K2q4lxxeBov69nR5kSboigepRzfoawZh30_RoS5h2kJMKVR1ybUg5DHtWBxh_0IiDCDXdM90Y0Fyj3-ydzYCjpdCgJhClti_lAj8bbAFsAsygFMAElanguage=zh-cnlat=39.001975lon=115.569574max_memory=128mod=vivo(vivo X20A)net=WIFIoc=GENERICos=androidphoto_id=5217983156054037441photoinfo=_/_referer=ks://photo/434066130/5217983156054037441/3/1_i/2000108968253389745_f80#likeserverExpTag=feed_photo|5217983156054037441|434066130|1_i/2000108968253389745_f80sh=1600sw=900sys=ANDROID_5.1.1token=aab48c12c7894f86b8ee785d1cb52017-1942009504ud=1942009504user_id=434066130ver=6.9"
    # sig_str = "app=0appver=6.9.2.11245browseType=1c=GENERICcancel=0client_key=3c2cd3f3country_code=CNdid=ANDROID_4c1d96d144ad9668did_gt=1599889958395egid=DFP6BF45042A7CFF4F24BB4A99354ED15A957C7E435A3D4282B5AD0B29D8C7A3expTagList=CkgKQ2ZlZWRfcGhvdG98NTIyNzU1MzMwNTc5NDg3MTQ4NHw0MzQwNjYxMzB8MV9pLzIwMDAxMDg1NjQwMjM3MTA3NjlfZjASATE=exp_tag0=exp_tag=1_i/2000108564023710769_f0ftt=hotfix_ver=isp=CMCCiuid=kpf=ANDROID_PHONEkpn=KUAISHOUkuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSsAGUSd0n6B877TjG9oXcOoM8yr0DhrF1sgDQScoD65QUYC5HmBkBN8qJhbn9e9qVAEEQfaswH8glP5ieAwMyk9Msfrujndh6AoqcysoiaPRDTPSDGs2Kqgfnuyc6ZpxxuOKUmhHFSMA2kF6eIo7wMtHOjaQIWNDU_ZaY6zaL-SmuhVnFbTnTMjPPl-_d6-6tze_NM8frJlb0MpEVvvyuEFUQ8StumTMNa8ON5rhJ2OR7vBoSXsvyHSXyTLeKCF7lcu0AFTTRIiDRRK0BNaCHriOHDrdCSUnF56rOo9DWXLDZx9OKyf0ORSgFMAElanguage=zh-cnlat=39.001975lon=115.569574max_memory=128mod=Xiaomi(MI 9)net=WIFIoc=GENERICos=androidphoto_id=5227553305794871484photoinfo=_/_referer=ks://photo/434066130/5227553305794871484/3/1_i/2000108564023710769_f0#likeserverExpTag=feed_photo|5227553305794871484|434066130|1_i/2000108564023710769_f0sh=1600sw=900sys=ANDROID_5.1.1token=05e4294930b744de8db9ca5240d304f5-1942009504ud=1942009504user_id=434066130ver=6.9"
    print(sig_str)
    str = sig_str + salt

    print(str)
    m = hashlib.md5(str.encode())
    sig = m.hexdigest()
    print(sig)
    return sig


def http():
    url_tail = parse.urlencode(headers)
    sig = sig_and_headers()
    haha = {'sig': sig,
            '__NStokensig': getNsTokenSig(sig)}
    sig_data.update(haha)
    # print(sig_data)

    result = requests.post(url=url + url_tail, data=sig_data)
    print(result.text)


sig_and_headers()
http()
