from flask import Flask
from flask import request
app = Flask(__name__)

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
        with open('sign.txt','a') as f:
            f.write('have a new post\n')
            f.flush()
        f.close()
        print('sign.txt生成成功！')
        return str1
    if request.method == 'GET':
        return content


if __name__ == '__main__':
    app.run()
