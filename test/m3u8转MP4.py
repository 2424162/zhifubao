import os

file_path ="D:\\android视频\\video"
file_name = "playlist.m3u8"
str = ".ts"
#cmd_str =""
cmd_list = []
def m3u8_to_mp4():
    f = open(file_path+"\\"+file_name,"r")
    for i in f.readlines():
        if str in i:
            print(i.strip())
            cmd_list.append(i.strip())
    cmd_str = "+".join(cmd_list)
    print(cmd_str)
    command = "copy/b " + cmd_str +" haha.mp4"
    print(command)
    os.getcwd()
    os.chdir(file_path)
    print("haha"+os.getcwd())
    print(file_path)
    os.system(command)


m3u8_to_mp4()
