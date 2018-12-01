'''
 -*- coding: utf-8 -*-
 @Time : 18-12-1 上午11:48
 @Author : SamSa
 @Site : 
 @File : modifyApi.py
 @Software: PyCharm
 @Statement:用户信息修改  逻辑删除
'''
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash, generate_password_hash

from App.models import db
from App.models.userModel import User

parse_base = reqparse.RequestParser()
parse_base.add_argument('username', type=str, required=True, help='请输入用户名')
parse_base.add_argument('action',type=str, required=True, help='请输入请求参数')
parse_base.add_argument('password', type=str, required=True, help='请输入密码')

parse_modify = parse_base.copy()
parse_modify.add_argument('new_password', type=str)
parse_modify.add_argument('email',type=str)

class ModifyResource(Resource):
    def post(self):
        args_base = parse_base.parse_args()
        _username = args_base.get('username')
        _password = args_base.get('password')
        action = args_base.get('action')

        args_modiyf = parse_modify.parse_args()
        new_password = args_modiyf.get('new_password')
        new_email = args_modiyf.get('email')

        # 验证用户是否可操作
        user = User.query.filter_by(username=_username).first()
        if user:
            if not user.flag:
                return {
                    'msg':'用户已经删除'
                }
            if not user.active:
                return {
                    'msg':'用户尚未激活'
                }
            if not check_password_hash(user.password,_password):
                return {
                    'msg':'密码不对'
                }

            if action == 'modify':
                if new_password:
                    user.password = generate_password_hash(new_password)
                if new_email:
                    user.email = new_email
                user.save()
                return {
                    'status':'ok',
                    'msg':'信息修改成功'
                }

            elif action == 'delete':
                user.flag = False
                user.save()
                return {
                    'status':'ok',
                    'msg':'删除成功'
                }
            else:
                return {
                    'status':'Falure',
                    'msg':'请输入正确的请求参数'
                }


