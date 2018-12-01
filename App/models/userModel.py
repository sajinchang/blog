'''
 -*- coding: utf-8 -*-
 @Time : 18-11-30 下午3:52
 @Author : SamSa
 @Site : 
 @File : userModel.py
 @Software: PyCharm
 @Statement:用户表
'''
from App.models import db
from App.models.utilModel import Util


class User(db.Model,Util):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)

    username = db.Column(db.String(32),unique=True,nullable=False)
    password = db.Column(db.String(256),nullable=False)
    email = db.Column(db.String(64),nullable=False)

    # 是否激活,默认否
    active = db.Column(db.Boolean,default=False, comment='是否激活')
    # 逻辑删除,注销用户flag,0为删除
    flag = db.Column(db.Boolean,default=True, comment='是否逻辑删除')
    token = db.Column(db.String(64), unique=True, comment='获取一个uuid,做邮箱激活验证')

    # db.relationship('Blog', backref='user', lazy='dynamic', cascade='all,delete-orphan', passive_deletes=True)