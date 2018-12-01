'''
 -*- coding: utf-8 -*-
 @Time : 18-12-1 下午3:07
 @Author : SamSa
 @Site : 
 @File : create_modify_blog.py
 @Software: PyCharm
 @Statement:blog的创建与修改
'''
from datetime import datetime

from flask import session
from flask_restful import Resource, reqparse

from App.models import db
from App.models.blogModel import Blog

parse_base = reqparse.RequestParser()
parse_base.add_argument('action')
parse_base.add_argument('title', type=str, required=True, help='请输入博客标题')

parse_create = parse_base.copy()
parse_create.add_argument('content', type=str, required=True, help='请输入博客内容')

parse_modify = parse_base.copy()
parse_modify.add_argument('content', type=str, required=True, help='请输入修改后的博客内容')

class BlogResource(Resource):
    def post(self):
        user_id = session.get('user_id')
        args_base = parse_base.parse_args()
        _title = args_base.get('title')
        action = args_base.get('action')


        last_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if action.__eq__('create'):
            if Blog.query.filter_by(title=_title).first():
               return {
                   'msg':'相同标题的博客已经存在'
               }
            args_create = parse_create.parse_args()
            content = args_create.get('content')

            blog = Blog()
            blog.content = content
            blog.u_id = user_id
            blog.last_time = last_time
            blog.title = _title
            blog.save()
            return {
                'msg':'博客添加成功'
            }

        blog__ = Blog.query.filter_by(title=_title)
        if blog__.count() > 0:
            blog_ = blog__.first()
            if not blog_:
                return {
                    'msg':'博客不存在,无法操作'
                }
            if user_id != blog_.u_id:
                return {
                    'msg':'你没有权限修改或删除'
                }
            if action == 'modify':
                args_modify = parse_modify.parse_args()
                content = args_modify.get('content')
                blog_.content = content
                blog_.last_time = last_time
                blog_.save()
                return {
                    'msg':'修改成功',
                }
            if action == 'delete':
                db.session.delete(blog_)
                db.session.commit()

                return {
                    'msg':'删除博客成功'
                }





