'''
 -*- coding: utf-8 -*-
 @Time : 18-11-30 下午8:19
 @Author : SamSa
 @Site : 
 @File : accountApi.py
 @Software: PyCharm
 @Statement:注册  登陆
'''
from uuid import uuid4

from flask import render_template, session
from flask.json import jsonify
from flask_mail import Message
from flask_restful import Resource, reqparse


from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import cache, mail
from App.models.userModel import User

parse_base = reqparse.RequestParser()
parse_base.add_argument('action', type=str, required=True, help='请输入请求的参数')
parse_base.add_argument('password', type=str, required=True, help='Please input your password')

# 注册
parse_register = parse_base.copy()
parse_register.add_argument('username', type=str, required=True, help='Please input your username')
parse_register.add_argument('email', type=str, required=True, help='Please input your email')

# 登陆
parse_login = parse_base.copy()
parse_login.add_argument('username', type=str, required=True, help='请输入用户名')


class AccountResource(Resource):
    def post(self):
        args = parse_base.parse_args()
        password = args.get('password')
        action = args.get('action')
        if action == 'register':
            info = parse_register.parse_args()
            username= info.get('username')
            email = info.get('email')
            print('+' * 50)
            print(username,password,email)
            print('+' * 50)
            # 密码加密
            password = generate_password_hash(password)

            # 创建user对象
            user = User()
            user.username = username
            user.password = password
            user.email = email

            # 获取一个唯一值
            token = str(uuid4())
            user.token = token
            user.save()

            # token存入缓存    进行邮箱验证
            cache.set(token, token, timeout=30)

            # 发送邮件
            message = Message(subject='邮箱验证激活', sender='sajinde@163.com', recipients=[email])
            url = 'http://127.0.0.1:5000/active/?token=' + token
            content = render_template('account.html',username=username, url=url)
            message.html = content
            mail.send(message)

            return jsonify({
                'status':'Successful',
                'msg':'注册成功,请前往邮箱激活',
            })
        elif action.__eq__('login'):
            info_login = parse_login.parse_args()
            username = info_login.get('username')
            users = User.query.filter_by(username=username)
            if users.count() > 0:
                user = users.first()
                if user.flag.__eq__(False):
                    return {
                        'status:': 403,
                        'msg': '账户逻辑删除'
                    }
                if check_password_hash(user.password, password):  # 判断密码
                    if user.active.__eq__(True):  # 判断状态是否激活

                        session['user_id'] = user.id
                        return {
                            'status': 'ok',
                            'msg': '登陆成功'
                        }

                    return {
                        'status': 'Falure',
                        'msg': '尚未激活,请先激活'
                    }
                return {
                    'status': 'Falure',
                    'msg': '密码错误!'
                }
            return {
                'status': 404,
                'msg': '尚未注册'
            }
        else:
            return {
                'msg':'请求参数有误'
            }