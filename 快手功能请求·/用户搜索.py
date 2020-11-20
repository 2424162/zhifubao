import requests
import hashlib
from urllib import parse


class SearchUser:

    def __init__(self, keyword):
        self.keyword = keyword

        self.pcursor = "0"
        self.headers = {'mod': 'OPPO(OPPO R17)',
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

        self.sig_data = {
            'keyword': keyword,
            'kuaishou.api_st': 'Cg9rdWFpc2hvdS5hcGkuc3QSsAGXm3HD4A3IE0-rOY2tpqjfMGN1fCZmXjtarSiB10ZS8gQ1WUKg-utQWlGACTRDLIC4kAr_VtjPgiiKRgA3X3qXSMBaigBBPLCN6WeLm4zoVJwC6rAXcIL0VJ59xIFTnhC6anQbrEuFGd7Fj-NhVxQg5JeH3EXHaap4pQ0w6-sxy_vEIK5_dmhJ1dMSkOjU-0y3kCXFsnRx9bpjlVi4RJhSTdoZG_xeUCnnaCE55DE-jhoS_p-fQlhnTN25qC7aiHAv_WWtIiD3S7b2NxIWHo0_Sm8tMH2j3J4FG5BLowT4w-DkJNRpISgFMAE',
            'token': '72f3226d45e449659f56e58a52c1478e-1942009504',
            'client_key': '3c2cd3f3',
            'os': 'android',
        }

    def sig_and_headers(self):
        sig_str = ""
        url_headers = {}
        head = list(self.headers)
        sig_key = self.headers
        sig_key.update(self.sig_data)
        for i in sorted(list(sig_key)):
            sig_str = sig_str + i + "=" + sig_key[i]

        self.sig_str = sig_str
        head.sort()
        for i in head:
            url_headers[i] = self.headers[i]
        self.url_tail = parse.urlencode(url_headers)

    def search_user(self):
        users_url_hair = 'https://apissl.ksapisrv.com/rest/n/search/user?'
        workpage_url_hair = "https://apikqcc2.ksapisrv.com/rest/n/search/new?"

        salt = '382700b563f4'
        str = self.sig_str + salt
        m = hashlib.md5(str.encode())
        sig = m.hexdigest()
        data = {'keyword': self.keyword,
                '__NS_sig3': '2194813079c6cec236ed6b20c856d3b1456bb6c7fd',
                '__NStokensig': '7d01066e884e4877eabfe7a8d520c7f14ec5f761eb5431d9a6d7f3292f7486b4',
                'kuaishou.api_st': 'Cg9rdWFpc2hvdS5hcGkuc3QSsAGXm3HD4A3IE0-rOY2tpqjfMGN1fCZmXjtarSiB10ZS8gQ1WUKg-utQWlGACTRDLIC4kAr_VtjPgiiKRgA3X3qXSMBaigBBPLCN6WeLm4zoVJwC6rAXcIL0VJ59xIFTnhC6anQbrEuFGd7Fj-NhVxQg5JeH3EXHaap4pQ0w6-sxy_vEIK5_dmhJ1dMSkOjU-0y3kCXFsnRx9bpjlVi4RJhSTdoZG_xeUCnnaCE55DE-jhoS_p-fQlhnTN25qC7aiHAv_WWtIiD3S7b2NxIWHo0_Sm8tMH2j3J4FG5BLowT4w-DkJNRpISgFMAE',
                'token': '72f3226d45e449659f56e58a52c1478e-1942009504',
                'client_key': '3c2cd3f3',
                'os': 'android',
                'sig': sig,
                }

        if(self.pcursor == "0"):
            pass
        else:
            data.update(self.users_follow_data)
        print(data)
        result = requests.post(url=users_url_hair + self.url_tail, data=data)
        self.result = result.json()

    def follow_up_users_search(self, pcursor):
        self.pcursor = str(pcursor)
        print("第多少页：",str(pcursor))
        self.users_follow_data = {'pcursor': pcursor,
                             'ussid': self.ussid,
                             }
        #print(self.ussid)
        self.sig_data.update(self.users_follow_data)


    def follow_up_workpage_search(self, pcursor):
        self.pcursor = pcursor
        workpage_follow_data = {
            'relatedTab': "",
            'pcursor': pcursor,
            'ussid': self.ussid,
            'fromPage': '0',
        }
        self.sig_data.update(workpage_follow_data)

    def users_data_process(self):

        data_json = self.result
        print(data_json)
        users = data_json['users']
        self.ussid = data_json['ussid']

        print(data_json['ussid'])
        for user in users:
            headurl = user["headurl"]
            fansCount = user['fansCount']
            try:
                kwaiId = user['kwaiId']
            except:
                kwaiId = ""
            user_id = user['user_id']
            user_name = user['user_name']
            user_sex = user['user_sex']
            user_text = user['user_text']
            #print(headurl, fansCount, kwaiId, user_id, user_name, user_text)


if __name__ == '__main__':

    search = SearchUser("老司机")
    search.sig_and_headers()
    search.search_user()
    search.users_data_process()

    num = 1
    while True:
        next = input("是否需要下一页(0不需要，1需要)：")
        if(next=="1"):
            search.follow_up_users_search(str(num))
            search.sig_and_headers()
            search.search_user()
            search.users_data_process()
            num = num+1
