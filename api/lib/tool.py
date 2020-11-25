#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Allen Luo
import pymysql
from config.settings import MYSQL_INFO

"""
sql调用方法处理
"""


def mysql_exe(sql):
    """
    获取sql查询数据
    :param sql:
    :return:
    """
    db = pymysql.connect(**MYSQL_INFO)
    l = []
    try:
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        datas = cursor.fetchall()
        for data in datas:
            l.append(data)
        return l
    except BaseException as e:
        print("数据库执行失败", e)
    finally:
        db.close()
