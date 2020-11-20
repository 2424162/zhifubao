f = open("headers","r")
str = ''
for i in f.readlines():
    data = i.strip().split(": ")
    #print(data[0],data[1])
    str2 = "'"+data[0]+"'"+":"+" "+"'"+data[1]+"'"+","+"\n"
    str = str +str2
print(str)
