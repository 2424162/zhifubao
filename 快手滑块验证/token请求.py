import requests
import json

url = ' https://api.zt.kuaishou.com/rest/zt/captcha/sliding/verify'
headers = {
'Host': 'api.zt.kuaishou.com',
'Connection': 'keep-alive',
'Content-Length': '1728',
'Accept': 'application/json, text/plain, */*',
'Origin': 'https://captcha.zt.kuaishou.com',
'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SKW-A0 Build/LMY49I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 Kwai/6.9.2.11245',
'Content-Type': 'text/plain',
'Referer': 'https://captcha.zt.kuaishou.com/iframe/index.html?captchaSession=Cgp6dC5jYXB0Y2hhErgBqsLuJR3Mi71a5pUIzFomLVu_JlHX4VSEQOeIS_D7ezguVEBomucaLV_r0G3xlb_H6VA1uPJwlyMiXO5atxlzjHY9ByML5aq3KJDf-y9J_ltuMfqhSAjGJa9b74HjTwjjv-C8mr8yx7ITQ3equb53R_hyg7ePtPoIf9V-Wn8mx4HdjOQxPe_JEzBwhedw8s2dtui4sHszaIsvYREVc9iVPBq8tCxsUwhuDN2gKAwAucebQNyC6astmxoSMyUzcK7eGp3-I_GJOrQSTdelKAUwAg&type=1&configUrl=https%3A%2F%2Fapi.zt.kuaishou.com%2Frest%2Fzt%2Fcaptcha%2Fsliding%2Fconfig',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,en-US;q=0.8',
'Cookie': 'mod=blackshark%28SKW-A0%29; lon=116.41025; country_code=cn; kpn=KUAISHOU; oc=GENERIC; egid=DFP1780926497C850F66E6B5F42508CEE26B65EBBD9172EA2D81EF8D44332619; hotfix_ver=; sh=1600; max_memory=192; isp=CMCC; browseType=1; kpf=ANDROID_PHONE; net=WIFI; app=0; ud=1942009504; c=GENERIC; sw=900; ftt=; language=zh-cn; iuid=; lat=39.916411; did_gt=1594347299450; ver=6.9; sys=ANDROID_5.1.1; appver=6.9.2.11245; did=ANDROID_d55ba519b285fe7d; token=46d50fb3c83d4dc8bb85e19be3be0d02-1942009504; client_key=3c2cd3f3; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSsAEdr8SsZFxgcrM03xxXBgcuefpD5pNrNn02hdQo_TQHYvnnmRTp-7_U5LjDVMU7jjgsvOleO4fWizEa_VUcOobHyOTTojMJL34CbBzjj1Du-5EqwalIfUJr8kpVqRRxur8ih2lsS6_R-55A2w_zwSeqVx4LOeTIhCDnBYTh_9oDanYaL3a9QDfPwElkoc5yXV2iJ4Wa3ut-sLQJBmx3RK7XhPzeL0NQh2W4-cTkzPDA5RoSzJ1EdK8FSN6I7LecEi4lYncRIiAk5CM2qLyviTACHlUS4p-F_UFl7HJ6A1PfSMaCyU75figFMAE; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAVTHWK2zzrIJPg8Q9EUVlG6c3UfGE11ea_AvULIKHj7MSMJFFir6NiR6jFj8Lwbsbvw6rvYVfXpZFEt9um4BTgS8UQpAm3r7wG-W-DFU3ilr6vML8bzyOyapSimHCfq-M00mU-cm3B4co9R6eXvOksHwUtMhXl7bUSGAN69GYdT8M6xAKq2J8PB30ZeIE3tZ806en-c_KWbmkL1vOgpBcJcaEuVzrJwrjFciNLdDbMoI5SeMUyIgcNO-Hpcgf_xqvlVrfLNe20WOe7GRPryP-4z5SeFHlcwoBTAB; sid=26c7c677-9f13-42a5-9d86-7bbcb9a45e75; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1594347894; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1594437265',
'X-Requested-With': 'com.smile.gifmaker',


}
data1 = {"type":7,"uri":"/rest/n/search/new","key":"-411541028829815805","input":"HEADCgp6dC5jYXB0Y2hhEtwB7W1hf9Yq0NhqsVd-eIRPGNJ6WC5mVOwz6-vUvGn7Qxv4Rzi8L3ql5nXIu6rNzb2sKgGLbOKHwGStkJJj6rhp1GghAAXM6UewRtNnRzk1uCsoEI_LrcTn9-MfzzbavM2DzSAKdROlaVnduxvKDNbQjy11ZU-RE16EJan7DdE-rpPydxBDXVLsg2hY-6FM1BLlePKti0hRVonQlZ4O51SZw-svyc-Tv6J8uAEAB128ZpYIL5PkobykdYqY71KECjvYwaowp_d1duHXNTtkx70G-9a7JTRb_Wy6DkkGfhoSV4gdhjwh95YCtMfPIXzXzFmCKAUwAgTAIL"}
data = 'Cy050N6ilGz9wMLJ/zpsaKZ4oRC68mfTm0YMpTalpHdLvH113clHXYgXuiersu9U9/+74FOr7PuSToOFIhJqIsImudavDF9UWnQ3vifOd5IjHZRArF0jzxwQKuz3JN7/gnLNcx2InxEqBW6mLFRKiuBATHK18KF6OQjN5PMifQXCrvM7qQufZthJsO7qTnNJT5HmKjxtIklmvG7+QPTL56SY8/7PQ/28rCsbp1j4TysPh05CJgYUqG1EwbUwGqaZTHcubnoBpDpiEoRTtI3Qabi9eWwOb6JwLbT/JOTwCV7PZf9PQsCx41OzQMznohAISfcpcvaS46l5XY9oLF8U3epn6QHgRv4YrqIU9EDvXm7GAF0ivOpJ12DOyre4nCv6jDcPZKKbuFJh1uOsQZ6Ik26AM0iW5i6aMW+3X8yJSlcKpMm9m3K7MEqB+ZhuuVPBPlNQoB7uwC4NwhbPoq5QjJs1JMx8aVU8a0i2SpgV77SNe7P4iv/uQ69YbtH8nAM7bu6SeM1t3HyL1V1IqC8IzFnBI6Rsy0QFkBNcxSSTtmMh6n5hSOVT6Yp7IlLpOwoIE1H/7BI5+RXj2IN4kmnt32YJ1SMcaZR+4qTghltVY2+s72ZTEYiSwp10yPRF8N1x2XH1JP5ELF5T9+r6aemrnQ3iVw56owUOSHfuDNpZHij0+74ajBciKqCcE8VIHVsf94QpzdiVdT9aOSUCi/XZ9mDmob/1bzLbK+1WmqPM1gkp1ga7sxo91ak8rbbMWT4g5ZY5QnWwmIUIsSVn6pkdmBrVGjixeZn3M96M6quydIBs59++jSYuITnRwiaE6XkxarhmMVccdrv54Nrb+Hs8WOhL7b32DsBUjmFwK7d730ZxV2r9EZ27HhUFcbe+xCwrnu6cxeD99SMES5gAVgBH8pIlGeG5roadmgziiJ4mUHg28Nq+2k/iqk1E4zsgIoY7I5Z5RiAIV+rtF4dB5EpMbStNbTyJAxkGCbCWch/MooC1Z8F4LHWpLS+u9Pj1lm6hDTk8p4B1RVVUJY5Gftid1f1b9LS/kn0Znq73TDGAtGkoXJUt98RWoR+lXTTNpP8Xl7o0beX55TUTFK1W2ANvCX/ScMgNOt24oPkguC3gsgHlIWNrOqWoxyJTjcD9+poZPnkCkEb2qwh2FM25O+061vkYJdWcjZsLG1H0g0WgkYQcPSZYjfaBgcmnXhLP5BTDyJUM7VzXTEb5qWQjaGRhHlV4neHgtbBvtj6IVlFuJQWmVYblQQYy+nNUvJvsnIZYqIeNWRTkhs9nVLyZjX4pYwBIDq6zUatMaMQOT/hD0CE8wRB0qUlTN/vtnM0d2zlbd7z8CDWgHEfMDtpp3i8nlLlV66ZTsU60CVFUndVT/bUKjeQtoOYZmWQtBfsFZnbFXPVAax++O8NYgd2OXo80wWlTqfV3I0cKJvuJWOFFOLmEd3V5GvVkyaNFE0Symde31q0VWkipWrvVu058EDz8rZf6ZPFjRUp4EdqLslqT7K4T2n1VSKNQinntN0StyMMHXi55sLgZDBn/78OmZihEhFSZt51T87dwv0F2WWhhZd2D1FTYTM5f8V33XPhzXTNfPn8DqGZIXiYdzHuj88UgKnZDWqrtW+tpl4gFb09nTy+Cv88ZFd4wIVrCRBQpHnumfjnqEy//d4VKdQEtF3EVb4KnH1JBKPvI1wM+vvbs80xYgRVIZf/yuQeSphRha3so'
print('kaishi')
data = json.dumps(data)
req = requests.post(url=url,headers=headers,data=data).json()
print(req)

