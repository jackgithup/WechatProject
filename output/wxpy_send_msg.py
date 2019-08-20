from wxpy import *
# bot = Bot()
bot = Bot(console_qr=True, cache_path=True)
# bot.file_helper.send("hello")
my_friends =bot.friends()

my_friend = bot.friends().search(u'诸葛飞飞')[0]
print(my_friend)

# 发送图片
my_friend.send_image('/Users/edz/Desktop/zhengmangProject/WeChat/a.jpg')
# 发送文本
my_friend.send('Hello, WeChat!')
# 发送视频
# my_friend.send_video('my_video.mov')
# # 发送文件
# my_friend.send_file('my_file.zip')
# # 以动态的方式发送图片
# my_friend.send('@img@a.jpg')