#encoding:utf8
import itchat
import time
from config import screen_path,nichengs,rooms
from concurrent.futures import ThreadPoolExecutor


def keep_concent():
    itchat.auto_login(hotReload=True)
    while True:
        users = itchat.search_friends(name='诸葛飞飞')
        userName = users[0]['UserName']
        itchat.send('test message:keep connect!', toUserName=userName)
        print('test message:keep connect!')
        time.sleep(60 * 5)

def send_photo():
    itchat.auto_login(hotReload=True)
    while True:
        import redis
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        itchat_status = r.get('itchat_status')
        if itchat_status == '0':
            for nicheng in nichengs:
                users = itchat.search_friends(name=nicheng)
                userName = users[0]['UserName']
                itchat.send_image(screen_path, toUserName=userName)
                itchat.send('test message:send photo success to person!', toUserName=userName)
            for roomname in rooms:
                iRoom = itchat.search_chatrooms(roomname)
                for room in iRoom:
                    if room['NickName'] == roomname:
                        userName = room['UserName']
                        break
                itchat.send_msg('test message:send photo success to room!', userName)
                itchat.send_image(screen_path, userName)
            r.set('itchat_status', '1')
        r.connection_pool.disconnect()

if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=2)
    pool.submit(keep_concent)
    pool.submit(send_photo)