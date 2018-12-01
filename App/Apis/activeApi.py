'''
 -*- coding: utf-8 -*-
 @Time : 18-11-30 下午10:23
 @Author : SamSa
 @Site : 
 @File : activeApi.py
 @Software: PyCharm
 @Statement: 邮箱激活
'''
from flask import request
from flask_restful import Resource

from App.models.userModel import User
from App.ext import cache
from App.models import db


class ActiveResource(Resource):
    def get(self):
        # 获取浏览器传过来的参数
        token = request.args.get('token')
        # 获取cache缓存传过来的token
        _token = cache.get(token)

        # 根据浏览器返回的参数查询
        user = User.query.filter(User.token==_token).first()
        if user:
            user.active = True
            user.save()
            return {
                'status':200,
                'msg':'激活成功!'
            }
        # 邮件过期则删除用户
        else:
            user = User.query.filter(User.token==token).first()
            db.session.delete(user)
            db.session.commit()
            return {
                'status':'200',
                'msg':'邮件过期',
            }