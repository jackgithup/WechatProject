import os
from multiprocessing import Pool

def f1():
    os.system('python3 step1_flask.py')
def f2():
    os.system('python3 step2_phantomjs.py')
def f3():
    os.system('python3 step3_itchat.py')

pool = Pool(3)
pool.apply_async(f1)
pool.apply_async(f2)
pool.apply_async(f3)
pool.close()
pool.join()
