str0 = "中"
def str_byte(ch,rs,cal):
    str1 = ord(ch)
    re_bs = ""
    str2 = str1>>rs
    str3 = str2 | cal
    bs = bin(str3)
    for i in range(3, len(bs)):
        if(bs[i]=="1"):
            re_bs=re_bs+"0"
        else:
            re_bs=re_bs+"1"
    re_bs = int(re_bs,2)+int("1",2)
    if(bs[2]=="1"):
        re_bs="-"+str(re_bs)
    print(re_bs)
def last_array(ch):
    re_bs = ""
    str1 = ord(ch)
    str2 = str1&63
    str3 = str2|128
    bs = bin(str3)
    for i in range(3, len(bs)):
        if (bs[i] == "1"):
            re_bs = re_bs + "0"
        else:
            re_bs = re_bs + "1"
    re_bs = int(re_bs, 2) + int("1", 2)
    if (bs[2] == "1"):
        re_bs = "-" + str(re_bs)
    print(re_bs)
def ch_byte(ch):
    str_byte(str0, 12, 224)
    str_byte(str0, 6, 128)
    last_array(ch)
ch_byte(str0)
