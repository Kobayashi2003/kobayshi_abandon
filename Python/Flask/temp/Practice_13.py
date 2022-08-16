# 会话

# 除了请求对象之外还有一种称为 session 的对象，允许你在不同请求 之间储存信息。这个对象相当于用密钥签名加密的 cookie ，即用户可以查看你的 cookie ，但是如果没有密钥就无法修改它。

# 使用会话之前你必须设置一个密钥。举例说明:

from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# 这里用到的 escape() 是用来转义的。如果不使用模板引擎就可以像上例 一样使用这个函数来转义。



# 如何生成一个好的密钥

# 生成随机数的关键在于一个好的随机种子，因此一个好的密钥应当有足够的随机性。 操作系统可以有多种方式基于密码随机生成器来生成随机数据。使用下面的命令 可以快捷的为 Flask.secret_key （ 或者 SECRET_KEY ）生成值:

# $ python -c 'import os; print(os.urandom(16))'
# b'_5#y2L"F4Q8z\n\xec]/'


# 基于 cookie 的会话的说明： Flask 会取出会话对象中的值，把值序列化后储存到 cookie 中。在打开 cookie 的情况下，如果需要查找某个值，但是这个值在请求中 没有持续储存的话，那么不会得到一个清晰的出错信息。请检查页面响应中的 cookie 的大小是否与网络浏览器所支持的大小一致。

# 除了缺省的客户端会话之外，还有许多 Flask 扩展支持服务端会话。