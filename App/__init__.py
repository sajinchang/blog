'''
 -*- coding: utf-8 -*-
 @Time : 18-11-30 下午3:27
 @Author : SamSa
 @Site : 
 @File : __init__.py.py
 @Software: PyCharm
 @Statement:初始化app
'''

from flask import Flask

from App import settings
from App.Apis import init_api
from App.ext import init_ext
from App.models.blogModel import Blog
from App.models.likeModel import Like
from App.models.userModel import User


def create_app(ENV_NAME):
    app = Flask(__name__)
    app.config.from_object(settings.ENV_NAME.get(ENV_NAME))
    user = User()
    blog = Blog()
    like_ = Like()

    # 浏览器乱码
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    init_api(app=app)
    init_ext(app=app)
    return app