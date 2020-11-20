import requests
import re
import time

index_url = "http://pic.netbian.com/shoujibizhi/"
photo_url =  "http://pic.netbian.com/downpic.php?id="#id=26134&classid=68
headers ={
'Host': 'pic.netbian.com',
'Proxy-Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Referer': 'http://pic.netbian.com/tupian/26134.html',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': '__cfduid=d8e6f91918f5a837a82cd374a69e0f4161602568070; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1602568071,1604295157; zkhanlastsearchtime=1604295251; PHPSESSID=gp4s7oolnn47celttvi58phik0; zkhanmlusername=qq507613159903; zkhanmluserid=3756219; zkhanmlgroupid=1; zkhanmlrnd=gOb8SH5YKutQthXvVDcR; zkhanmlauth=512de12627eef60a079ea5e6ebeecd23; zkhanecookieclassrecord=%2C65%2C55%2C56%2C68%2C; zkhanpayphome=BuyGroupPay; zkhanpaymoneybgid=2; zkhandownid26134=1; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1604295711'
}
def get_photo_id():
    for page in range(5,7):
        req = requests.get(url=index_url+"index_"+str(page)+".html",headers=headers)
        print(req.text)
        print(req.request)
        print(req.content)

        index_pat = '<a href="/tupian/(.*?).html.*?alt="(.*?)" /><b>'
        result = re.findall(index_pat,req.text)

        for id,j in result:
            download(id,page)
            time.sleep(3)


def download(id,page):
    url = photo_url+str(id)+"&classid=68"
    req = requests.get(url = url,headers =headers)

    file = open("页面"+str(page)+'/'+str(id)+".jpg","wb+")
    file.write(req.content)
    print("完成"+id)
get_photo_id()


