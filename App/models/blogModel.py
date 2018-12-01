'''
 -*- coding: utf-8 -*-
 @Time : 18-11-30 下午4:15
 @Author : SamSa
 @Site : 
 @File : blogModel.py
 @Software: PyCharm
 @Statement:blog 模型
'''
from App.models import db
from App.models.userModel import User
from App.models.utilModel import Util


class Blog(db.Model,Util):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    content = db.Column(db.TEXT, comment='博客内容')
    u_id = db.Column(db.Integer,db.ForeignKey(User.id,ondelete='CASCADE'))
    title = db.Column(db.String(64),unique=True,nullable=False)
    last_time = db.Column(db.DateTime, comment='最近修改时间')


