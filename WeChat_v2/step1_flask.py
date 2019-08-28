#encoding:utf8
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/send_table',methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        table = request.form.get('table')  #参数名为username
        table = "<!DOCTYPE html><html><head><meta charset='UTF-8'></head><body>{}</body></html>".format(table)
        import imgkit
        options = {'encoding': 'utf8'}
        imgkit.from_string(table, 'table.jpg',options=options)
        import redis
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        r.set('itchat_status','0')
        r.connection_pool.disconnect()
        return 'new photo produced!'
    if request.method == 'GET':
        return 'please send post request!'



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)