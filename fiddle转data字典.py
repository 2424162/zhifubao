f = open('data','r',encoding="utf-8")
str = '{'
for data in f.readlines():
    cc = data.strip().split("	")
    #print(cc)

    if len(cc)==1:
        cc.append('')
    str2 = "'"+cc[0]+"'"+":"+" "+"'"+cc[1]+"'"+","+"\n"
    str = str+str2
str=str+"}"
print(str)



