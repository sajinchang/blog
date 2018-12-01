'''
 -*- coding: utf-8 -*-
 @Time : 18-11-30 下午3:43
 @Author : SamSa
 @Site : 
 @File : settings.py
 @Software: PyCharm
 @Statement:配置文件
'''


# 拼接连接数据库的参数
def get_db_uri(DATABASE):
    dialect = DATABASE.get('dialect')
    driver = DATABASE.get('driver')
    username = DATABASE.get('username')
    passwd = DATABASE.get('password')
    host = DATABASE.get('host')
    port = DATABASE.get('port')
    db = DATABASE.get('db')
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,driver,username,passwd,host,port,db)


class Config():

    #配置数据库环境
    TEST = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 防止数据持久化时报错
    SECRET_KEY = '123'

    # 配置邮箱验证
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = 'sajinde@163.com'
    MAIL_PASSWORD = 'sajinchang124816'



# 开发环境
class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'root',
        'password': '123456',
        'host': 'localhost',
        'port': 3306,
        'db': 'blog'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


#测试环境
class TestConfig(Config):
    TEST = True
    DATABASE = {
        'dialect':'mysql',
        'driver':'pymysql',
        'username':'root',
        'password':'123456',
        'host':'localhost',
        'port':3306,
        'db':'blog'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

# 演示环境
class ShowConfig(Config):
    DEBUG = True
    DATABASE = {
        'dialect':'mysql',
        'driver':'pymysql',
        'username':'root',
        'password':'123456',
        'host':'localhost',
        'port':3306,
        'db':'blog'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

# 生产环境
class ProductConfig(Config):
    DEBUG = True
    DATABASE = {
        'dialect':'mysql',
        'driver':'pymysql',
        'username':'root',
        'password':'123456',
        'host':'localhost',
        'port':3306,
        'db':'blog'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


# 定义环境名字
ENV_NAME = {
    'develop':DevelopConfig,
    'test':TestConfig,
    'show':ShowConfig,
    'product':ProductConfig
}