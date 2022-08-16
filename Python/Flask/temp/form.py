from venv import main
from werkzeug.routing import BaseConverter
from flask import Flask, render_template, request, redirect, url_for, make_response, json, jsonify, abort
from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['JSON_ASCII'] = False

# @app.route('/index/')
# def index():
#     if request.method == 'GET':
#         return render_template('myproject/index.html')
#     elif request.method == 'POST':
#         return 'this is a post'




# @app.route('/index')
# def index():
#     data = {
#         'name' : '张三'
#     }
#     # response = make_response(json.dumps(data), ensure_ascii=False)
#     # response.mimetype = 'application/json'
#     # return response
#     return jsonify(data)


# if __name__ == '__main__':
#     app.run()

# raise abort

# app = Flask(__name__)

# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         return make_response('index.html')
#     elif request.method == 'POST':
#         name = request.method.get('name')
#         password = request.form.get('password')
#         if name == 'kobayashi' and password == '123':
#             return 'login sucess'
#         else:
#             abort(404)
#             return None


# 模板 jinja2