from selenium import webdriver
from config import screen_path,url,phantomjs_path
import redis
import time

class Produce_photo():

    def judge_newfile(self):
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        phantomjs_status = r.get('phantomjs_status')
        if phantomjs_status == '0':
            self.produce_photo()
            r.set('phantomjs_status','1')
        r.connection_pool.disconnect()

    def produce_photo(self):
        browser = webdriver.PhantomJS(executable_path=phantomjs_path)
        browser.get(url)
        millis = int(round(time.time() * 1000))
        browser.save_screenshot(screen_path)
        browser.close()


if __name__ == '__main__':
    while True:
        prod = Produce_photo()#
        prod.judge_newfile()
