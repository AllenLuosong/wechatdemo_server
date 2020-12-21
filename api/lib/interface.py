#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Allen Luo
"""
接口调用逻辑处理
"""
import time

import flask
import json
from data.sql import qsql, csql
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
    # print(isql)
    return "请求成功"


@server.route("/api/updateBorrowGoods", methods=["post"])
def updateBorrowGoods():
    id = flask.request.values.get("id")
    now_date = time.strftime("%Y/%m/%d", time.localtime())
    count = mysql_exe(csql)[0][0]
    # print("count", count)
    # print("id", id)
    id_ = (int(count) - int(id))
    upsql = "update borrowTable set revertDate='{}' where id ={}".format(now_date, id_)
    print("upsql", upsql)
    mysql_exe(upsql)
    return "更新成功"
