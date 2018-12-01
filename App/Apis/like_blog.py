'''
 -*- coding: utf-8 -*-
 @Time : 18-12-1 下午4:19
 @Author : SamSa
 @Site : 
 @File : like_blog.py
 @Software: PyCharm
 @Statement: 收藏博客
'''
from flask import session
from flask_restful import Resource, reqparse

from App.models.likeModel import Like

parse = reqparse.RequestParser()
parse.add_argument('blog_id')

class LikeBlogResource(Resource):
    def get(self):
        u_id = session.get('user_id')
        args = parse.parse_args()
        blog_id = args.get('blog_id')

        like_blog = Like()
        like_blog.u_id = u_id
        like_blog.blog_id = blog_id
        like_blog.save()
        return {
            'msg':'收藏成功'
        }