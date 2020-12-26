# sql语句配置文件

#  查询借用表数据
qsql = "select borrowname, borrowdate, borrowgoods, revertDate from BorrowTable order by id desc;"

# isql = " insert into BorrowTable (borrowname, borrowdate, borrowgoods, revertDate) VALUES ({},{},{},{})".format(borrowName, param1,
#                                                                                                                 param1, param1)

csql = "select count(id) from BorrowTable;"



#CREATE PROCEDURE insert_person()
#begin
#    declare c_id integer default 1;
#    while c_id<=100000 do
#    insert into person values(c_id, concat('name',c_id), c_id+100, date_sub(NOW(), interval c_id second));
#    set c_id=c_id+1;
#    end while;
#end
