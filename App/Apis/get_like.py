'''
 -*- coding: utf-8 -*-
 @Time : 18-12-1 下午4:35
 @Author : SamSa
 @Site : 
 @File : get_like.py
 @Software: PyCharm
 @Statement:  获取某用户的所有收藏
    - 获取收藏某博客的所有用户
'''
from flask_restful import Resource, reqparse

from App.models.blogModel import Blog
from App.models.likeModel import Like
from App.models.userModel import User

parse_base = reqparse.RequestParser()
parse_base.add_argument('action', type=str, required=True, help='请输入请求的参数')
# 获取用户的收藏
parse_user = parse_base.copy()
parse_user.add_argument('user_id', type=int, required=True, help='请输入用户id')

# 获取某个博客的所有收藏用户
parse_blog = parse_base.copy()
parse_blog.add_argument('blog_id', type=int, required=True, help='请输入博客的id')
class GetLikeResource(Resource):
    def get(self):
        args_base = parse_base.parse_args()
        action = args_base.get('action')

        info = []
        if action.__eq__('user'):
            args_user = parse_user.parse_args()
            u_id = args_user.get('user_id')
            flag = User.query.filter_by(id=u_id)
            if not flag.first():
                return {
                    'msg':'用户不存在'
                }
            elif flag.first().flag == False:
                return {
                    'msg':'用户被逻辑删除'
                }

            blogs = Like.query.filter(Like.u_id==u_id)
            if blogs.count() > 0:
                for blog in blogs:
                    info.append('该用户收藏了主键为%s的blog'%blog.blog_id)

                return {
                    'msg':info
                }
        elif action.__eq__('blog'):

            args_blog = parse_blog.parse_args()
            blog_id = args_blog.get('blog_id')
            _blog = Blog.query.filter_by(id=blog_id)
            if not _blog.count() > 0:
                return {
                    'msg':'博客不存在'
                }

            users = Like.query.filter(Like.blog_id==blog_id)
            if users.count() > 0:
                for user in users:
                    info.append('主键为%s的用户收藏该博客'%user.u_id)
                return {
                    'msg':info
                }

        else:
            return {
                'msg':'请输入正确的请求参数'
            }

