#encoding:utf8
import itchat
import time
from config import file_path,screen_path,nicheng
import os
from concurrent.futures import ThreadPoolExecutor
import threading

def keep_concent():
    itchat.auto_login(hotReload=True)
    myfriends = itchat.get_friends()
    rooms = itchat.get_chatrooms(update=True)
    while True:
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
        import redis
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        phantomjs_status = r.get('phantomjs_status')
        itchat_status = r.get('itchat_status')
        if phantomjs_status == '1' and itchat_status == '0':
            users = itchat.search_friends(name=nicheng)
            userName = users[0]['UserName']
            itchat.send_image(screen_path,toUserName=userName)
            itchat.send('send photo success', toUserName=userName)
            r.set('itchat_status','1')
        r.connection_pool.disconnect()

if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=2)
    pool.submit(keep_concent)
    pool.submit(send_photo)
