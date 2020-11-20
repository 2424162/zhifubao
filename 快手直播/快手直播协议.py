import requests
import urllib3
import urllib

class GifShowLive:
    def __init__(self,url):
        self.url = url
    def get_param(self):
        http = urllib3.PoolManager()
        r = http.request("GET", self.url, redirect=False)
        str = r.headers["Location"]
        author = roomid = ""
        list1 = str.split("&")
        for i in list1:
            list2 = i.split("=")
            # print(list2)
            if list2[0] == "userId":
                author = list2[1]
            if list2[0] == "shareObjectId":
                roomid = list2[1]
        print(author, roomid)
        return author,roomid

    def startplay(self):
        startplay_url = "https://apikqcc2.ksapisrv.com/rest/n/live/startPlay/v2?"



if __name__ == '__main__':
    gifshow = GifShowLive("https://v.kuaishou.com/8Uz5Ay")
    gifshow.get_param();


