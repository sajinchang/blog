'''
 -*- coding: utf-8 -*-
 @Time : 18-11-30 下午3:34
 @Author : SamSa
 @Site : 
 @File : ext.py
 @Software: PyCharm
 @Statement:第三方库加载
'''
from flask_cache import Cache
from flask_mail import Mail
from flask_migrate import Migrate

from App.models import db

mail = Mail()
cache = Cache(config={'CACHE_TYPE':'redis'})
def init_ext(app):
    # 命令行参数使用
    migrate = Migrate()
    migrate.init_app(app=app,db=db)
    # 数据库初始化
    db.init_app(app=app)

    # cache初始化
    cache.init_app(app=app)
    #邮箱邮箱初始化
    mail.init_app(app=app)
