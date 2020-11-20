f = open("header","r")
str =''
sjson='mBuilder.addHeader("'
for data in f.readlines():
    cc = data.strip().split("	")
    print(cc)
    if len(cc)==1:
        cc.append("")
    str2 = sjson + cc[0] + '"' + ',' + '"' + cc[1] + '")' + '\n'
    str=str+str2
print(str)
