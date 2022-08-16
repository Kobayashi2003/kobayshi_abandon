# 变量规则

from flask import Flask, escape

app = Flask(__name__)

@app.route('user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the sibpath after /path/
    return 'Subpath %s' % escape(subpath) # escape() 函数可以对字符串中所有可能被解释为正则运算符的字符进行转义

if __name__ == '__main__':
    app.run()


# 转换器类型：
# string （缺省值）接受任何不包含斜杠的文本
# int 接受正整数
# float 接受正浮点数
# path 类似 string，但可以包含斜杠
# uuid 接受 UUID 字符串
