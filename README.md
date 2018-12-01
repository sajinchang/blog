## Api文档

### 1.用户的增删改查

 用户的操作均为post请求

注册 	127.0.0.1:5000/account/

> username 
>
> password
>
> action			参数为:register
>
> email



登陆	 		127.0.0.1:5000/account/

> username
>
> password
>
> action			参数为:login




修改信息 			127.0.0.1:5000/modify/

> username		
>
> password
>
> action						参数为:modify
>
> email						可为空参
>
> new_password				可为空参



删除用户 				127.0.0.1:5000/modify/

> username
>
> password
>
> action			参数为:delete

blog

### 2.博客的增删改

均为post请求,首先需要登陆

添加博客			127.0.0.1:5000/blog/

> title
>
> content
>
> action		参数为:create

修改博客			127.0.0.1:5000/blog/

> action				参数为:modify
>
> content

删除博客 			127.0.0.1:5000/blog/

> action			参数为:delete
>
> title

### 3.blog与用户的操作

收藏博客   get请求   			127.0.0.1:5000/like/

> blog-id





查找用户所收藏的博客     get 请求    127.0.0.1:5000/search/

> action			参数为 :user
>
> user_id			

获取某个博客的所有收藏用户     get 请求    127.0.0.1:5000/search/

 >action			参数为:blog
 >
 >blog_id
 >
 >



### 4.数据模型

user 表

```mysql
  CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `flag` tinyint(1) DEFAULT NULL,
  `token` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token` (`token`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

```



blog表

``` mysql
CREATE TABLE `blog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text,
  `u_id` int(11) DEFAULT NULL,
  `last_time` time DEFAULT NULL,
  `title` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `u_id` (`u_id`),
  CONSTRAINT `blog_ibfk_1` FOREIGN KEY (`u_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

```



收藏表 like   (注意在查询时like为关键字)

```mysql
CREATE TABLE `like` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) DEFAULT NULL,
  `blog_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_id` (`blog_id`),
  KEY `u_id` (`u_id`),
  CONSTRAINT `like_ibfk_1` FOREIGN KEY (`blog_id`) REFERENCES `blog` (`id`),
  CONSTRAINT `like_ibfk_2` FOREIGN KEY (`u_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

```

