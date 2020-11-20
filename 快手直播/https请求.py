str = "fid=1942009504&cc=share_copylink&followRefer=151&shareMethod=TOKEN&docId=5&kpn=KUAISHOU&subBiz=LIVE_STREAM&shareId=233022176394&shareToken=X-ooDbp2t1sI1EN_A&shareResourceType=LIVESTREAM_OTHER&userId=2040441332&shareType=5&et=1_a%2F2000116729320291874_n86&shareMode=APP&originShareId=233022176394&appType=21&shareObjectId=1hO4sKwtFgI&shareUrlOpened=0&timestamp=1598605671830"
author = roomid = ""
list1 = str.split("&")
for i in list1:
    list2 = i.split("=")
    #print(list2)
    if list2[0] == "userId":
        author = list2[1]
    if list2[0] == "shareObjectId":
        roomid = list2[1]
print(author,roomid)
