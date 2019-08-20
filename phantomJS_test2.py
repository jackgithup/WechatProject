#http://127.0.0.1:5000/
from selenium import webdriver
from config import file_path,screen_path,url,phantomjs_path
import os

class Produce_photo():
    def read_file(self):
        readfile = open(file_path,'r')
        return readfile.readlines()


    def write_file(self,content):
        with open(file_path, 'a') as f:
            f.write(content)
            f.flush()

    def judge_newfile(self):
        while True:
            # 判断标志文件是否存在
            if os.path.exists(file_path):
                lines = self.read_file()
                conetnt = self.read_file()
                length = len(conetnt)
                if length == 1:
                    self.produce_photo()
                    print("截图成功！")
                    self.write_file('produce a new photo\n')
            else:
                pass

    def produce_photo(self):
        # browser = webdriver.Chrome()
        browser = webdriver.PhantomJS(executable_path=phantomjs_path)
        # browser.get("http://www.baidu.com")
        browser.get(url)
        browser.save_screenshot(screen_path)
        browser.close()


if __name__ == '__main__':
    prod = Produce_photo()#
    prod.judge_newfile()