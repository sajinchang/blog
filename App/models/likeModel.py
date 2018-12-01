'''
 -*- coding: utf-8 -*-
 @Time : 18-11-30 下午4:31
 @Author : SamSa
 @Site : 
 @File : likeModel.py
 @Software: PyCharm
 @Statement:收藏表
'''
from App.models import db
from App.models.blogModel import Blog
from App.models.userModel import User
from App.models.utilModel import Util


class Like(db.Model,Util):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    # 两个外键
    u_id = db.Column(db.Integer,db.ForeignKey(User.id))
    blog_id = db.Column(db.Integer,db.ForeignKey(Blog.id))