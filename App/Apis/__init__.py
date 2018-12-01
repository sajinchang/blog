'''
 -*- coding: utf-8 -*-
 @Time : 18-11-30 下午3:27
 @Author : SamSa
 @Site : 
 @File : __init__.py.py
 @Software: PyCharm
 @Statement:
'''
from flask_restful import Api
from App.Apis.accountApi import AccountResource
from App.Apis.activeApi import ActiveResource
from App.Apis.all_api import AllResource
from App.Apis.create_modify_blog import BlogResource
from App.Apis.get_like import GetLikeResource
from App.Apis.like_blog import LikeBlogResource
from App.Apis.modifyApi import ModifyResource

api = Api()


def init_api(app):
    api.init_app(app=app)


# 注册api
api.add_resource(AccountResource,'/account/')
api.add_resource(ActiveResource,'/active/')
api.add_resource(ModifyResource,'/modify/')
api.add_resource(BlogResource,'/blog/')
api.add_resource(LikeBlogResource,'/like/')
api.add_resource(GetLikeResource,'/get/')
api.add_resource(AllResource,'/user/')