import requests
url = "https://graphicriver.net/content/receive_upload?id=14554088-aa534e25b0d21019638bed0ff5a6818f0a717b43&type=textures"
headers = {
'Host': 'graphicriver.net',
'Connection': 'keep-alive',
'Content-Length': '87403',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
'Content-Type': 'multipart/form-data; boundary=AaB03x',
'Accept': '*/*',
'Origin': 'https://graphicriver.net',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://graphicriver.net/content/upload/form?utf8=%E2%9C%93&type=textures',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': '__cfduid=d100880ffc2364757777756b8277d3bb71604046584; market_experiment_Q4KMAh3BQ4qNUNsdMXdprg=1; market_experiment_eCQGElkrSVqkXjHjD14dBg=0; market_experiment_21yS8z6cQVyR9_77HH-PpQ=0; market_experiment_csat_survey=0; market_experiment_KPjrVT2lTZ6xjZWU2O4gng=0; market_experiment_38IZ2heHTeyVuJ9OGcqDnA=0; referring_user=-1; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1604046588511%2Cregion:%27HK%27}; _gcl_au=1.1.598832407.1604046589; _pin_unauth=dWlkPVlUVTVPVFF3Tm1NdE1UVmhZaTAwTWpKa0xXSm1aV0V0TTJVd05UVm1aalJoT1RRMA; signed_in=1; marketplace_banners=%7B%22global%22%3A%22elements_mkt-header_general_8Sept2020_B%22%7D; _gat_m=1; _gali=file-input-container; _uetsid=6f6acdc01a8311eba288114dacd00ca8; _uetvid=6f6b0dc01a8311ebafaa551cbb38fbb2; _fd_session=QpFw%2B2Hd9C6Z8P%2FJ7smH%2FGhMM1FzutsuOw3vvSJ6476ZcNfw8QE%2BQpc4dfTK8pxZ%2FixcHRQx5VMbYhqMezmEzynKMbaTgO9OfoIekXmnlN37%2Fka%2FUfROvnrxccRDue3vIVsSLCa0gu688iHGgy2O7ibBf4ptNRq6BPLmttDjU4Bs7%2BNmXEaX3nEOuJo5YiVKf0yknEU0steGAC71vgrN9zCF0O7Cg8SaaiQod82jiqJsEx54kPF7ixOZorYXoqJwDjEGogqyMBG2n%2FIdmI5FyLm0bvNf9z4%2FtnTkUqjxCa4EDbbvRBaMO6a1UfnZr9kuQpccJ3cGwUb%2Bo%2FGv53Dg2YInEZem6T1MDhkzji6YSjewoWQgblowec3mHnPG3%2BbkdlDG51OTU%2FvUpQDeXV8ENIAA2MCL0wPvp%2FkzTnOEgscGJsY0Qg%3D%3D--E6XT5uyRfjx6Hdkn--78Ps2YtmZeR7UyCyUk5wEw%3D%3D'
}

proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}

cc = open("1.PNG","rb")

print(str(cc.read()))

files = {
    'Filename':(None,'1.PNG'),
    'Upload':(None,'Submit Query'),
    'Filedata':('1.PNG',open('1.PNG','rb'),'image/png'),
}


Data = "--AaB03x\r\n" +"content-disposition: form-data; name=\"Filename\"\r\n" +"\r\n" + "1.PNG\r\n" +"--AaB03x\r\n" +'content-disposition: form-data; name="Upload"\r\n' +"\r\n" +"1.PNG\r\n" +"--AaB03x--\r\n"

data1 = "--AaB03x\r\n"+"Content-Disposition: form-data; name=\"Filename\"\r\n" +"\r\n" + "1.PNG\r\n" +"--AaB03x\r\n" +'Content-Disposition: form-data; name="Upload"\r\n'+"\r\n" + "Submit Query\r\n"+"--AaB03x\r\n"+'Content-Disposition: form-data; name="Filedata";filename="1.PNG"\n'+"Content-Type: image/png\r\n"+"\r\n"+str(cc.read())+"\r\n" +"--AaB03x--\r\n"
response = requests.request("POST", url=url, headers=headers,data =data1,proxies = proxies,verify=False)
print(response)
print(response.content)