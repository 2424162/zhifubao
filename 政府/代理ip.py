# encoding: UTF-8
import requests
import time
import random

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
ip = ['27.129.32.', '60.9.60.', '59.48.112.', '1.71.0.', '1.24.200.', '1.180.233.', '42.52.128.', '42.185.192.',
      '42.244.64.', '1.51.120.', '27.148.0.', '39.178.128.', '27.207.141.', '27.16.125.', '42.48.63.', '14.25.0.',
      '61.236.141.', '1.207.163.', '1.80.156.', '43.242.180.', '42.91.0.', '14.204.220.', '61.157.217.', '14.18.244.',
      '42.49.105.', '27.23.134.', '202.205.131.', '222.66.83.', '61.155.235.', '60.191.45.', '1.51.16.', '36.111.192.',
      '58.192.32.', '61.155.108.', '112.25.61.', '121.229.0.', '180.111.0.', '183.208.0.', '202.102.81.', '221.226.2.',
      '222.67.124.', '219.228.80.', '1.14.128.', '27.115.0.', '42.196.0.', '222.70.133.','222.66.54.', '218.83.128.',
      '202.122.0.', '218.78.154.', '14.18.9.', '1.184.0.', '112.90.0.','45.119.64.','218.6.246.', '222.209.57.',
      '27.211.0.', '27.193.0.', '27.194.0.', '218.88.37.', '221.237.166.', '223.104.0.', '221.131.194.',
      '220.189.209.', '218.75.39.', '39.134.8.', '222.240.217.', '220.168.12.', '1.14.128.', '27.115.0.',
      '42.196.0.', '1.51.144.', '27.192.76.', '124.134.0.','218.65.83.','218.65.80.', '218.65.5.', '59.55.4.',
      '218.76.174.', '218.76.179.', '218.76.253.', '222.243.158.','183.68.227.','219.153.178.','219.148.122.'
    ,'221.192.231.','110.248.239.','120.4.0.', '39.134.35.', '61.178.172.', '124.152.63.']


# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--log-level=3")
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('https://www.wjx.cn/jq/29150603.aspx')
# s = driver.execute_script('jqnonce')
# print s

def jqsign(a, k):
    b = k % 10
    # b = 1
    c = ""
    d = 0
    for ch in a:
        e = ord(ch) ^ b
        c = c + chr(e)
    # print k
    # print c
    return c


# print jqsign("9e2d16b0-947e-4cc9-a572-19e5af6912ff")
def makeData(n):
    list = []
    for i in range(0, 200):
        list.append([1, 0])

    list[1] = [1, [1, 48], [2, 52]]
    list[2] = [1, [1, 0], [2, 0], [3, 0]]
    list[3] = [1, [1, 0], [2, 0], [3, 0], [4, 0]]
    list[4] = [1, [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
    list[5] = [1, [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]
    list[6] = [1, [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
    list[7] = [1, [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]]
    list[8] = [1, [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]

    list[9] = [1, [1, 0], [2, 0], [3, 5], [4, 45], [5, 50]]
    list[10] = [1, [1, 0], [2, 0], [3, 5], [4, 35], [5, 60]]
    list[11] = [1, [1, 0], [2, 0], [3, 5], [4, 55], [5, 40]]
    list[12] = [1, [1, 0], [2, 0], [3, 5], [4, 75], [5, 20]]
    list[13] = [1, [1, 0], [2, 0], [3, 5], [4, 65], [5, 30]]
    list[14] = [1, [1, 0], [2, 0], [3, 5], [4, 45], [5, 50]]
    list[15] = [1, [1, 0], [2, 0], [3, 5], [4, 35], [5, 60]]
    list[16] = [1, [1, 0], [2, 0], [3, 5], [4, 55], [5, 40]]
    list[17] = [1, [1, 0], [2, 0], [3, 5], [4, 75], [5, 20]]


    list[18] = [1, [1, 40], [2, 55], [3, 5], [4, 0], [5, 0]]
    list[19] = [1, [1, 50], [2, 45], [3, 5], [4, 0], [5, 0]]
    list[20] = [1, [1, 35], [2, 60], [3, 5], [4, 0], [5, 0]]
    list[21] = [1, [1, 60], [2, 35], [3, 5], [4, 0], [5, 0]]
    list[22] = [1, [1, 25], [2, 70], [3, 5], [4, 0], [5, 0]]
    list[23] = [1, [1, 45], [2, 50], [3, 5], [4, 0], [5, 0]]
    list[24] = [1, [1, 50], [2, 45], [3, 5], [4, 0], [5, 0]]
    list[25] = [1, [1, 60], [2, 35], [3, 5], [4, 0], [5, 0]]
    list[26] = [1, [1, 20], [2, 75], [3, 5], [4, 0], [5, 0]]
    list[27] = [1, [1, 43], [2, 57], [3, 5], [4, 0], [5, 0]]

    list[27] = [20,
                 [[1,0],[2,0],[3,5],[4,30],[5,65]],
                 [[1,0],[2,0],[3,5],[4,70],[5,25]],
                 [[1,0],[2,0],[3,5],[4,60],[5,35]],
                 [[1,0],[2,0],[3,5],[4,55],[5,40]],
                 [[1,0],[2,0],[3,5],[4,65],[5,30]],
                 [[1,0],[2,0],[3,5],[4,40],[5,55]],
                 [[1,0],[2,0],[3,5],[4,65],[5,30]],
                 [[1,0],[2,0],[3,5],[4,50],[5,45]]]


    list[28] = [20,
                 [[1,35],[2,60],[3,5],[4,0],[5,0]],
                 [[1,65],[2,30],[3,5],[4,0],[5,0]],
                 [[1,25],[2,70],[3,5],[4,0],[5,0]],
                 [[1,55],[2,40],[3,5],[4,0],[5,0]],
                 [[1,30],[2,65],[3,5],[4,0],[5,0]],
                 [[1,60],[2,35],[3,5],[4,0],[5,0]],
                 [[1,52],[2,43],[3,5],[4,0],[5,0]],
                 [[1,40],[2,55],[3,5],[4,0],[5,0]]]




    list[29] = [15, [['', 71],['没有', 8],['没', 8],['无', 8],['暂无', 5]]]

    data = ''
    for i in range(1, n + 1):
        #time.sleep(1)
        # print list[i]
        data = data + str(i) + '$'  # 序号

        dateTemp = ''
        if list[i][0] == 10:  # 多选
            length = len(list[i])
            slice = []
            while len(slice) == 0:
                for j in range(1, length):
                    rand = random.randint(0, 100)
                    if rand <= list[i][j][1]:
                        slice.append(list[i][j][0])
            # size = random.randint(1, length - 1)
            # print slice
            # slice = random.sample(list[i][1:], len(slice))
            random.shuffle(slice)
            for j in range(0, len(slice)):
                dateTemp = dateTemp + str(slice[j])
                if j < len(slice) - 1:
                    dateTemp = dateTemp + '|'
        elif list[i][0] == 11:  # 多选,最多选几项
            length = len(list[i])
            # size = random.randint(1, list[i][1])

            slice = []
            length = len(list[i])

            while len(slice) == 0 or len(slice) > list[i][1]:
                slice = []
                for j in range(2, length):
                    rand = random.randint(0, 100)
                    if rand <= list[i][j][1]:
                        slice.append(list[i][j][0])

            # slice = random.sample(list[i][2:], size)
            random.shuffle(slice)
            for j in range(0, len(slice)):
                dateTemp = dateTemp + str(slice[j])
                if j < len(slice) - 1:
                    dateTemp = dateTemp + '|'
        elif list[i][0] == 12:  # 多选,最少选几项
            length = len(list[i])
            slice = []
            length = len(list[i])

            while len(slice) == 0 or len(slice) < list[i][1]:
                slice = []
                for j in range(2, length):
                    rand = random.randint(0, 100)
                    if rand <= list[i][j][1]:
                        slice.append(list[i][j][0])
            random.shuffle(slice)
            for j in range(0, len(slice)):
                dateTemp = dateTemp + str(slice[j])
                if j < len(slice) - 1:
                    dateTemp = dateTemp + '|'
        elif list[i][0] == 15:  # 填空
            length = len(list[i])
            for j in range(1, length):
                length1 = len(list[i][j])
                slice = []
                for k in range(0, length1):
                    for x in range(0, list[i][j][k][1]):
                        slice.append(list[i][j][k][0])
                size = random.randint(0, len(slice) - 1)
                # slice
                dateTemp = dateTemp + str(slice[size])
                if j < length - 1:
                    dateTemp = dateTemp + '^'
        elif list[i][0] == 16:  # 矩阵填空
            for j in range(1, len(list[i])):
                dateTemp = dateTemp + str(j) + '!' + str(list[i][j][random.randint(0, len(list[i][j]) - 1)])
                if j != len(list[i]) - 1:
                    dateTemp = dateTemp + '^'
        elif list[i][0] == 1:  # 单选
            # 以下设置比例
            length = len(list[i])
            slice = []
            for j in range(1, length):
                for k in range(0, list[i][j][1]):
                    slice.append(list[i][j][0])
            # 以上设置比例
            length = len(slice)
            size = random.randint(1, length - 1)
            dateTemp = dateTemp + str(slice[size])
            length = len(list[i])
            sliceTemp = slice
            for j in range(1, length):
                #print i,sliceTemp[size],list[i][j][0]
                if len(list[i][j]) == 3 and sliceTemp[size] == list[i][j][0]:
                    slice = list[i][j][2]
                    for k in range(len(slice)):
                        if list[slice[k]][0] == 1 or list[slice[k]][0] == 10 or list[slice[k]][0] == 11 or \
                                list[slice[k]][0] == 12:
                            list[slice[k]] = [1, [-3, 100]]
                        elif list[slice[k]][0] == 15:
                            list[slice[k]] = [1, ['(跳过)', 100]]
                        elif list[slice[k]][0] == 20:
                            for x in range(1, len(list[slice[k]])):
                                list[slice[k]][x] = [[-3, 1]]
        elif list[i][0] == 20:  # 矩阵
            for j in range(1, len(list[i])):
                slice = []
                for k in range(len(list[i][j])):
                    for x in range(0, list[i][j][k][1]):
                        slice.append(list[i][j][k][0])
                # print slice
                dateTemp = dateTemp + str(j) + '!' + str(slice[random.randint(0, len(slice) - 1)])
                if j != len(list[i]) - 1:
                    dateTemp = dateTemp + ','
        elif list[i][0] == 25:
            slice = []
            length = len(list[i])
            while len(slice) != list[i][1]:
                slice = []
                for j in range(2, length):
                    rand = random.randint(0, 100)
                    if rand <= list[i][j][1]:
                        slice.append(list[i][j][0])
            random.shuffle(slice)
            for j in range(len(list[i]) - list[i][1] - 2):
                slice.append(-2)
            for j in range(0, len(slice)):
                dateTemp = dateTemp + str(slice[j])
                if j < len(slice) - 1:
                    dateTemp = dateTemp + ','
        elif list[i][0] == 30:
            # slice = random.sample(list[i][2:], list[i][1])
            slice = []
            length = len(list[i])

            while len(slice) != list[i][1]:
                slice = []
                for j in range(2, length):
                    rand = random.randint(0, 100)
                    if rand <= list[i][j][1]:
                        slice.append(list[i][j][0])
            # print slice
            random.shuffle(slice)
            for j in range(0, len(slice)):
                dateTemp = dateTemp + str(slice[j])
                if j < len(slice) - 1:
                    dateTemp = dateTemp + '|'
        str1 = '构造第' + str(i) + '题成功'
        # print(str1)
        data = data + dateTemp  # 答案

        if i < n:
            data = data + '}'  # 分隔符

    print(data)

    return data


def wjx(number, url, Cookie):
    sess = requests.session()
    data = {
        # 'submitdata': "SP%5C%17P%17%05J%5COUC%07%09%06OQE%1FDU%1C%0B%19JQ%16UD%0C%15SN%0FEQ6tuS%14W%1C%08%16TG%08%0BsVCU%02%18%02B%05JR%18%1E%19%0D%16%05%01%02%13WM%1A%18U%14%01%0C%05I%0BE%0B%15%00V%12%0BMWzbcMX%5D%19%0DG%5CP%18%1ElKEU%02%18%00V%10UJ%08%1B%14%0C%1B%07%1A%15%07OP%15%18R%14%08%14%16Q%1EV%09%18%02J%01%08%40Rgqc%40%5CC%0A%0AJYO%0B%1EaN%5DF%03%15%05O%03PG%0A%01%07%0F%16%02%01%06%0ABR%01%0B_%19%0A%01%04U%13P%15%0A%00G%00%15RTjp%7DRZN%0D%15XYB%0D%06sOPG%1A%07%07B%05JU%0E%0C%06%14%04%0E%0C%00"
        'submitdata': makeData(number)
        # 'submitdata':'1$1}2$3}3$17}4$7}5$4|7|9}6$1}7$3|5}8$3}9$3}10$2}11$-3}12$1|2}13$3|5|7}14$1}15$2}16$3}17$2}18$3}19$2^没有这么快}20$2}21$2|4}22$2|4}23$2}24$2}25$1}26$3}27$5'
    }
    # ipp = ip[random.randint(0, len(ip)-1)] + str(random.randint(0, 255))
    # 发送post请求
    ipp = ip[random.randint(0, len(ip) - 1)] + str(random.randint(0, 255))
    # print ipp
    headers = {
        "Accept": "text/plain, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
        "Connection": "close",
        "Content-Length": "519",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": Cookie,
        "Host": "www.wjx.cn",
        "Origin": "https://www.wjx.cn",
        "Referer": "https://www.wjx.cn/jq/63472023.aspx",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    proxies = {"http": "http://81.68.221.80:27881", "http": "http://81.68.221.80:27881"}

    res = sess.post(url, headers=headers, data=data, proxies=proxies)

    print('失败了')
    return False
    print(res.text)
    if res.text.find("so") != -1:
        return True
    return False


def getJq(curid):
    url = 'https://www.wjx.cn/m/' + curid + '.aspx'
    head = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'www.wjx.cn',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    s = requests.get(url, headers=head)
    ss = s.text
    pos1 = ss.find('jqnonce="')
    pos2 = ss.find('"', pos1 + 9)
    return ss[pos1 + 9:pos2]



if __name__ == '__main__':
    time1 = 20
    time2 = 180
    doNumber = 20  # 刷几次
    titleNumber = 1  # 多少个题目

    for i in range(doNumber):
        curid = 63472023
        rn = '3687874582'
        Cookie = 'UM_distinctid=173fa79598986b-0734ecf3f6a67-31667305-1ea000-173fa79598a976; ev_47338494=1; SojumpABX_4439=1; actidev_89888021=1; mqcount=15; spsswjx=89958267,89835134,90263412,90594241,87555614; actidev_93059739=1; ev_93481084=1; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1602295858,1602751276,1603091186,1603248618; MyQuesHid_wowo123123=1; .ASPXANONYMOUS=f41uN__h1gEkAAAAMGUxNmVmOTUtMThjYS00MWNhLThjZGUtMTRmMjU5MjBlYTFlwpkGI0KkgiYNuEcTYrZDSrWqiNo1; DeleteQCookie=1; ASP.NET_SessionId=byelvltpkmlkeaqvoczmmnkk; acw_tc=781bad0616037833294474476e206eba6d63fb09b653c132b08d833a8694ba; LastCheckUpdateDate=1; crudat=2018-12-13 21:58:09; SojumpSurvey=0102AE76EA1D497AD808FEAE16FCA46A7AD8080006710071002400BD7FBD7F659100012F00FF0794BB3331AC92650CFEFC39C887EC4A531081FE; WjxUser=UserName=15895861792; LastActivityJoin=95062446,107606808916; join_95062446=1; CNZZDATA4478442=cnzz_eid%3D1532795341-1597632979-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1603783545; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1603783679949; SERVERID=6142ed0ee68ecc71fb491c53c82ec4a0|1603783683|1603783329; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1603783684'

        jqnonce = getJq(str(curid))
        url = 'https://www.wjx.cn/joinnew/processjq.ashx?curid=' + str(
            curid) + '&starttime=2018%2F11%2F16%2023%3A58%3A40&source=directphone&submittype=1&ktimes=11&hlv=1&rn=' + str(
            rn) + '&t=' + str(int(round((time.time()) * 1000))) + '&jqnonce=' + jqnonce + '&jqsign=' + jqsign(jqnonce,
                                                                                                              1)
        needTime = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime((time.time() - random.randint(time1, time2))))
        pos1 = url.find('starttime=')
        pos2 = url.find('&', pos1)
        url = url[0:pos1] + 'starttime=' + needTime + url[pos2:]

        if wjx(titleNumber, url, Cookie) == False:
            print('失败了')
            i = i - 1
        time.sleep(random.randint(10, 20))