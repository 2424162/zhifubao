path = "C:\\Users\\二筒\AppData\Local\Temp\\baidu\\"
file1 = 'ddms6808395202137435102.trace'
file2 = "ddms3553779955906186286.trace"
list1=[]
f1 = open(path+file1,"rb")
f2 = open(path+file2,"rb")
for i in f2.readlines():
    try:
        if "	"in i.decode():
            list1.append(i.decode().split("	")[1:])
            #print(i.decode())
    except:
        break
list2 =[]
for i in f1.readlines():
    try:
        if "	" in i.decode():
            #print(i.decode().split("	"))
            if i.decode().split("	")[1:] in list1:
                #print("有的")
                pass
            else:
                list2.append(i.decode())
    except:
        break
print(list2)
#for i in list2:
    #print(i)

f3 = open(path+file1,"rb+")
for i in f3.readlines():
    try:
        if "	" in i.decode():
            # print(i.decode().split("	"))
            if i.decode().split("	")[1:] in list1:
                print(i.decode())
                f3.writelines("")

    except:
        break
f3.close()


