#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Allen Luo
"""
接口调用逻辑处理
"""
import flask
import json
from data.sql import qsql
from lib.tool import mysql_exe

server = flask.Flask(__name__)


@server.route("/api/getBorrowGoods", methods=["get"])
def getBorrowGoods():
    global res, responed
    data = mysql_exe(qsql)
    data_l = []
    for results in data:
        data_l.append({
            "借用人": results[0],
            "借用日期": results[1],
            "借用物资": results[2],
            "归还日期": results[3]
        })
    responed = {
                "msg": "接口调用成功",
                "msg_code": "0",
                "data": data_l
                }

    return json.dumps(responed, ensure_ascii=False)