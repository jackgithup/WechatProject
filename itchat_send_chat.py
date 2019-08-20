import itchat
import time
from config import file_path,screen_path,nicheng
import os
from concurrent.futures import ThreadPoolExecutor
import threading

def keep_content():
    itchat.auto_login(hotReload=True)
    myfriends = itchat.get_friends()
    rooms = itchat.get_chatrooms(update=True)  # 是获得所有群
    while True:
        # 保持登陆状态
        users = itchat.search_friends(name=nicheng)
        message = 'status login'
        userName = users[0]['UserName']
        itchat.send(message, toUserName=userName)  # myfriends["UserName"])
        print('status login success!')
        time.sleep(60 * 5)

def send_photo():
    itchat.auto_login(hotReload=True)
    while True:
        users = itchat.search_friends(name=nicheng)
        # 给好友发截图
        if os.path.exists(file_path):
            readfile = open(file_path,'r')
            conetnt = readfile.readlines()
            length = len(conetnt)
            if length == 2:
                users = itchat.search_friends(name=nicheng)
                userName = users[0]['UserName']
                itchat.send_image(screen_path,toUserName=userName) #如果是其他文件可以直接send_file
                print('send photo success')
                os.remove(file_path)

if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=10)
    pool.submit(keep_content)
    pool.submit(send_photo())
