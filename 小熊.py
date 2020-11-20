import requests
import time
import json
url = "http://www.xxdws.com/ajax.php?act=gettool&cid={}&info=1"
f = open("小熊.txt","a+")
list1 = []
list2 = [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]
for i in list2:
    print(i)
    result = requests.post(url.format(i))
    result = result.json()
    for data in result['data']:
        name = data['name']
        tid = data['tid']
        str = name +" : "+ tid +"\n"
        print(str)
        f.write(str)






    time.sleep(1)
