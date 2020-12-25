#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Allen Luo
"""
服务启动入口，执行文件即可开启服务
"""
import os
import sys
# 通过在sys.path追加根目录来导入包，防止在dos命令出现找不到包的情况
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from lib.interface import server
from config.settings import SERVER_PORT, HOST

# server.run(host=HOST, port=SERVER_PORT, debug=True)
server.run(host=HOST, port=SERVER_PORT, debug=True, ssl_context=('../ssl_context/Apache/2_lerning.xyz.crt', '../ssl_context/Apache/3_lerning.xyz.key'))
