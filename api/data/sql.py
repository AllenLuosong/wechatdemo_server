# sql语句配置文件

#  查询借用表数据
qsql = "select borrowname, borrowdate, borrowgoods, revertDate from borrowTable order by id desc limit 0 ,7;"

# isql = " insert into borrowTable (borrowname, borrowdate, borrowgoods, revertDate) VALUES ({},{},{},{})".format(borrowName, param1,
#                                                                                                                 param1, param1)
