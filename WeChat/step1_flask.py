from flask import Flask
from flask import request

app = Flask(__name__)
content = """
            <!DOCTYPE html>
            <html>
            <head>
            <meta charset="utf-8">
            <title>auto table</title>
            </head>
            <body>
            welcome send_table
            </body>
            <script type="text/javascript">
            document.body.style.background = '#FFFFF0';
            </script>
            </html>
            """
@app.route('/send_table',methods=['GET','POST'])
def hello_world():
    global content
    if request.method == 'POST':
        table = request.form.get('table')  #参数名为username
        content = str1 = """
            <!DOCTYPE html>
            <html>
            <head>
            <meta charset="utf-8">
            <title>auto table</title>
            </head>
            <body>
            {}
            </body>
            <script type="text/javascript">
            document.body.style.background = '#FFFFF0';
            </script>
            </html>
            """.format(table)
        import redis
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        r.set('flask_status','1')
        r.set('phantomjs_status','0')
        r.set('itchat_status','0')
        r.connection_pool.disconnect()
        return str1
    if request.method == 'GET':
        return content



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
