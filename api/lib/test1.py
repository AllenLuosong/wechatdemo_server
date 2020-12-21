#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Allen Luo

import flask, time, json

server = flask.Flask(__name__)


@server.route('/login')
def login():
    username = flask.request.values.get('username')
    pwd = flask.request.values.get('pwd')
    if username == 'wind' and pwd == '123456':
        session_id = tools.my_md5(username + time.strftime('%Y%m%d%H%M%S'))
        key = 'wind_session:%s' % username
        tools.op_redis(key, session_id, 6000)
        res = {'session_id': session_id, 'error_code': 0, 'msg': '登录成功',
               'login_time': time.strftime('%Y%m%d%H%M%S')}  # 给用户返回的信息
        json_res = json.dumps(res, ensure_ascii=False)  # 返回结果为json格式
        res = flask.make_response(json_res)  # cookie 构造成返回结果的对象
        res.set_cookie(key, session_id, 6000)  # 最后的数字是cookie的失效时间
        return res


@server.route('/posts')
def posts():
    print('all_cookies', flask.request.cookies)  # 字典形式
    cookies = flask.request.cookies  # 获取到所有的cookie
    username = ''  # 定义这两个变量是为了在没有传cookie时用的
    session = ''
    for cookie in cookies:
        if cookie.startswith('wind_session'):  # 判断cookie以syz_session开头的话，取到它
            username = cookie  # 或者username = key   session = value
            session = cookies.get(cookie)  # 调用接口时，用户传的session
    redis_session = tools.op_redis(username)  # 从redis中获取的
    if redis_session == session:  # 判断传过来的session和redis中存的一样
        title = flask.request.values.get('title')  # 获取文章标题
        content = flask.request.values.get('content')  # 获取文章内容
        article_key = 'article:%s' % title  # key以article开头
        tools.op_redis(article_key, content)  # 把文章写入redis
        res = {'msg': '文章发表成功！', 'code': 0}
    else:
        res = {'msg': '用户未登录', 'code': 2009}
    # print('username:',username)
    # print('session:',session)
    return json.dumps(res, ensure_ascii=False)



