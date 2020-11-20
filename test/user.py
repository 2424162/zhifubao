import json

import requests

url = "https://live.kuaishou.com/m_graphql"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'Cookie': 'did=web_17f679b39ff1409aa7373f131fee7e10; didv=1592816174000; clientid=3; client_key=65890b29;'
          ' Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1594447676,1594706049,1594892726,1595902429; kuaishou.live.bfb1s=9b8f70844293bed778aade6e0a8f9942; userId=1942009504;'
          ' userId=1942009504; kuaishou.live.web_st=ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAQ01cLyQ6xvzEkK7JaZATG0yIFcgxVbTQDjCwD2vtXYKAsFUp0eYR5s4QfKBAWyaXAynKCIt1fEV6EWrTLflgZ-47V70KOl36uaXJz_2VVZypm18o7AJIFZHULqwZ2OA8XkPo0UUxWT88fzMtrQi8wtTYdKciovdRefI9XuwcDg9Foru0gtjGbCYEtvVjczONVwLzOkXpHh0XaAAqc7PN0gaEpwewD8CakIZrC7t8JEKqqml3iIgfj_W6Lqg0rsSbgx-BMP2Qv7PkCThDEqGGnF20yukNMAoBTAB; kuaishou.live.web_ph=e2bab168a06cdae3860f79ea632ac5a5d8b5; WEBLOGGER_HTTP_SEQ_ID=6226; WEBLOGGER_INCREAMENT_ID_KEY=6436',


}
data = {"operationName":"sensitiveUserInfoQuery","variables":{"principalId":"3xg4stx9ygsduqw"},"query":"query sensitiveUserInfoQuery($principalId: String) {\n  sensitiveUserInfo(principalId: $principalId) {\n    kwaiId\n    originUserId\n    constellation\n    cityName\n    counts {\n      fan\n      follow\n      photo\n      liked\n      open\n      playback\n      private\n      __typename\n    }\n    __typename\n  }\n}\n"}

cc = requests.post(url = url,headers = headers,json = data)
print(cc)
print(cc.content)
print(cc.text)