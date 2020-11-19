# wechatdemo_server
server of wechatdemo
我的第一个demo版本小程序服务端
项目整体架构

api--

     bin--
          wechat_sever_start.py
		
     config--
          settings.py
		
     data--
          sql.py
		
     lib--
          interface.py
          tool.py

bin目录下的wechat_server_shart.py是整个项目的启动入口，运行该文件即运行程序。
config下settings.py文件是配置文件，保存，服务器地址，端口，及mysql数据库配置相关
data下的sql.py文件即编写的数据库文件，用户查询数据库数据
lib下interface.py为接口调动文件，主要的接口处理逻辑都在这个文件中
tool.py为调用sql语句的执行文件
     
