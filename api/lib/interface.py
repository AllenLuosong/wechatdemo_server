#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Allen Luo
"""
接口调用逻辑处理
"""
import time

import flask
import json

from flask import render_template

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
            "borrowname": results[0],
            "borrowdate": results[1],
            "borrowgoods": results[2],
            "revertDate": results[3]
        })
    responed = {
        "msg": "接口调用成功",
        "msg_code": "0",
        "data": data_l
    }

    return json.dumps(responed, ensure_ascii=False)


@server.route("/api/postBorrowGoods", methods=["post"])
def postBorrowGoods():
    borrowname = flask.request.values.get("borrowname")
    # borrowdate = flask.request.values.get("borrowdate")
    borrowdate = time.strftime("%Y/%m/%d", time.localtime())
    borrowgoods = flask.request.values.get("borrowgoods")
    # revertDate = flask.request.values.get("revertDate")
    isql = "insert into borrowTable (borrowname, borrowdate, borrowgoods, revertDate) VALUES ('{}','{}','{}','')".format(
        borrowname, borrowdate, borrowgoods)
    
    mysql_exe(isql)
    return "请求成功"
