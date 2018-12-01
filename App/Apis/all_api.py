'''
 -*- coding: utf-8 -*-
 @Time : 18-12-1 下午10:33
 @Author : SamSa
 @Site : 
 @File : all_api.py
 @Software: PyCharm
 @Statement:查询所有

'''
from flask_restful import Resource

from App.models.userModel import User


class AllResource(Resource):
    def get(self):
        users = User.query.all()
        infos = []
        for user in users:
            username = user.username
            email = user.email
            flag = user.flag
            active = user.active
            token = user.token
            id = user.id
            info = {
                'id': id,
                'username': username,
                'email': email,
                'flag': flag,
                'active': active,
                'token': token,
            }
            infos.append(info)
        return {
            'msg':infos
        }