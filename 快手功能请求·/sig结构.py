sig="app=0appver=6.9.2.11245browseType=1c=GENERICclient_key=3c2cd3f3country_code=cndid=ANDROID_dcdd918e3fa28010did_gt=1595038232671egid=DFP7A28F2E28B8445FB1CFC15CD8D6F7BE6231EE5209B81DFB9654569AB09147fromPage=1ftt=K-T-Thotfix_ver=isp=CUCCiuid=keyword=六六六kpf=ANDROID_PHONEkpn=KUAISHOUkuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSsAHQGSJokveL1l172Uy_XxmAxBNAteBqMdoHXAi5O-ay88NiHqBn28aafMPspsj4F6Vho9kapL5AsV1sc4ZK56dvICXxP-Cf8yIDDq2qYPwXQk5FWlmsvngw8L1JDIJ4S7g9Qsi4i-UQpGC1NwTlX1w00vb7o-d_kE8V0oEE5IgGoGjSZwJu2akmzR9cZofGF2dGIFwXD9fQNFiPhUKRcIGGjKFdPU6SSTE_poTHulxEHRoSZkJiZF_qSRKoI0G7Sb9VLlZMIiCXvPYy0BEv89YxBN9nIpkCP28rrUy6GArqBV4qgN4BkCgFMAElanguage=zh-cnlat=30.047985lon=103.85135max_memory=128mod=Xiaomi(MI NOTE LTE)net=WIFIoc=GENERICos=androidrelatedTab=sh=1920sw=1080sys=ANDROID_6.0.1token=1801aa80f3d6418a93334401b1cb002f-1942009504ud=1942009504ver=6.9"

headers = '''mod
lon
country_code
kpn
oc
egid
hotfix_ver
sh
appver
max_memory
isp
browseType
kpf
did
net
app
ud
c
sys
sw
ftt
language
iuid
lat
did_gt
ver'''

print(sig.count("="))
cc = headers.split()
print(cc)
for j in sig.split("="):
    num =0
    for i in cc:
        if(i  not in j):
           num = num+1
    if num == 26:
        print(j)


