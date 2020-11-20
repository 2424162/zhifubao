f = open('data','r')
str = ''
sjson='dataJson.put("'
for data in f.readlines():
    cc = data.strip().split("	")
    if len(cc)==1:
        cc.append("");
    str2 = sjson+cc[0]+'"'+','+'"'+cc[1]+'");'+'\n'
    str = str+str2
print(str)
