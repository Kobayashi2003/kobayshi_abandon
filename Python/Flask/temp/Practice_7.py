# 操作请求数据

# 对于 web 应用来说对客户端向服务器发送的数据作出响应很重要。在 Flask 中由全局 对象 request 来提供请求信息。

# 本地环境

# 请求对象

from flask import Flask, request, render_template, valid_login, log_the_user_in

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST': # 通过使用 method 属性可以操作当前请求方法
        if valid_login(request.form['username'], # 通过 form 属性处理表单数据
                        request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username or password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)