import requests
import hashlib
from urllib import parse


class SearchUser:

    def __init__(self, keyword):
        self.keyword = keyword

        self.pcursor = "0"
        self.headers = {'mod': 'samsung(SM-N960F)',
                        'lon': '102.565041',
                        'country_code': 'CN',
                        'kpn': 'KUAISHOU',
                        'oc': 'GENERIC',
                        'egid': 'DFP019340B5EDC668F143EEE3BA02DD69775D064BA4397458E70EB7DB3346D41',
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
                        'lat': '31.998822',
                        'did_gt': '1587967311124',
                        'ver': '6.9',
                        }

        self.sig_data = {
            'relatedTab': '',
            'fromPage': '1',

            'keyword': self.keyword,
            'kuaishou.api_st': 'Cg9rdWFpc2hvdS5hcGkuc3QSsAFxzWpAbknUArXJOKEJDrDzBUA33zL3YnscgTuOHpNvwCEJK-i6z15kKrrQDth08TRtIUXhDmXTDlYnvoWfNli1fw7S1wib1cjMt8Lkfk4IjVltAsgJ6Eoe-C4fgCgJnM-BQdSErEmCoIbDNeRrdOer9bnrbMRjuD8qyc-7kcP6SIeOeCcg2a2ZZzFy7BFLtUCx96Ofa244F5sIEM31IrPGN6_dZ_RYAZhWhVCKZQk4hxoSV2uctxqfRjmHZQugthNjdfxMIiBUwG2Ji_TR0uNuoXc62y6Yu7MpCslAzON0cqhoLY2jJigFMAE',

            'token': '9f40c02016034f7b8c007e70a5d7d2f5-1942009504',
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
        workpage_url_hair = "http://apissl.gifshow.com/rest/n/search/feed?"
        new_url_hair = 'http://apissl.ksapisrv.com/rest/n/search/new?'

        salt = '382700b563f4'
        str = self.sig_str + salt
        m = hashlib.md5(str.encode())
        sig = m.hexdigest()
        print(sig)
        data = {'keyword': self.keyword,
                'relatedTab': '',
                'fromPage': '1',
                '__NS_sig3': '2194922439c64441f0a18be112046c9cb84a4f6455',
                '__NStokensig': '000bd8ef471db31d02c7059b40a64ded6fc852bb5670f64f458876dd355c8497',
                'kuaishou.api_st': 'Cg9rdWFpc2hvdS5hcGkuc3QSsAFxzWpAbknUArXJOKEJDrDzBUA33zL3YnscgTuOHpNvwCEJK-i6z15kKrrQDth08TRtIUXhDmXTDlYnvoWfNli1fw7S1wib1cjMt8Lkfk4IjVltAsgJ6Eoe-C4fgCgJnM-BQdSErEmCoIbDNeRrdOer9bnrbMRjuD8qyc-7kcP6SIeOeCcg2a2ZZzFy7BFLtUCx96Ofa244F5sIEM31IrPGN6_dZ_RYAZhWhVCKZQk4hxoSV2uctxqfRjmHZQugthNjdfxMIiBUwG2Ji_TR0uNuoXc62y6Yu7MpCslAzON0cqhoLY2jJigFMAE',
                'token': '9f40c02016034f7b8c007e70a5d7d2f5-1942009504',
                'client_key': '3c2cd3f3',
                'os': 'android',
                'sig': sig,
                }

        if (self.pcursor == "0"):
            pass
        else:
            data.update(self.workpage_follow_data)
        print(data)
        result = requests.post(url=workpage_url_hair + self.url_tail, data=data)
        self.result = result.json()

    def follow_up_users_search(self, pcursor):
        self.pcursor = str(pcursor)
        print("第多少页：", str(pcursor))
        self.users_follow_data = {'pcursor': pcursor,
                                  'ussid': self.ussid,
                                  }
        # print(self.ussid)
        self.sig_data.update(self.users_follow_data)

    def follow_up_workpage_search(self, pcursor):
        self.pcursor = pcursor
        self.workpage_follow_data = {
            'pcursor': pcursor,
            'ussid': self.ussid,

        }
        self.sig_data.update(self.workpage_follow_data)

    def users_data_process(self):

        data_json = self.result
        print(data_json)
        self.ussid = data_json['ussid']

        print(data_json['ussid'])
        for feed in data_json['feeds']:
            caption = feed['caption']
            url = feed['main_mv_urls'][0]['url']


if __name__ == '__main__':

    search = SearchUser("小辣鸡")
    search.sig_and_headers()
    search.search_user()
    search.users_data_process()

    num = 1
    while True:
        next = input("是否需要下一页(0不需要，1需要)：")
        if (next == "1"):
            search.follow_up_workpage_search(str(num))
            search.sig_and_headers()
            search.search_user()
            search.users_data_process()
            num = num + 1
