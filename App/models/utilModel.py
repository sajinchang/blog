'''
 -*- coding: utf-8 -*-
 @Time : 18-11-30 下午3:53
 @Author : SamSa
 @Site : 
 @File : utilModel.py
 @Software: PyCharm
 @Statement:工具模型类
'''
from App.models import db


class Util(object):
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            return {
                'status':'Failed',
                'msg':e
            }
        return 'Insert Successful!'

