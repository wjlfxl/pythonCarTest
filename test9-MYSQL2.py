#  -*- coding:utf-8 -*-
import pymysql
import pandas as pd
import numpy as np


# object 是所有类的父类,__类的私有属性，只有通过实列访问，不能通过类直接访问
class MySQLConnector(object):
    __host = ""
    __user = ""
    __password = ""
    __database = ""
    __charset = "utf8"
    __mySqlConn = None

    # 连接数据库  exception(异常)
    def get_connection(self):
        try:
            # 获取数据库连接对象，连接对象相当于一个操作平台，一切操作都是在这个平台上做的
            self.__mySqlConn = pymysql.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database,
                charset=self.__charset
            )
            print("数据库连接成功")
        except:
            print("连接数据库异常")

    # 执行查询sql语句
    def execute_sql(self, sql):
        results = None
        # 取得数据库连接
        self.get_connection()
        if self.__mySqlConn is not None:
            dbCursor = None
            try:
                # 取得连接对象游标
                dbCursor = self.__mySqlConn.cursor()
                # 执行sql语句
                dbCursor.execute(sql)
                # 取得执行结果
                results = dbCursor.fetchall()
                print("sql语句执行完毕")
            except:
                print("执行sql语句异常")
            # 关闭数据库连接资源
            finally:
                # 关闭游标
                if dbCursor is not None:
                    try:
                        dbCursor.close()
                        print("游标关闭成功")
                    except:
                        print("游标关闭异常")
                # 关闭数据库连接
                try:
                    self.close_conn()
                    print("数据库连接已关闭")
                except:
                    print("数据库连接关闭异常")
        return results

    # 执行修改、删除、新增sql语句
    def update_sql(self, sql):
        results = None
        # 取得数据库连接
        self.get_connection()
        if self.__mySqlConn is not None:
            dbCursor = None
            try:
                # 取得连接对象游标
                dbCursor = self.__mySqlConn.cursor()
                # 执行sql语句
                dbCursor.execute(sql)
                # 数据表内容有更新，必须使用到该语句
                self.__mySqlConn.commit()
                # 取得执行结果
                results = dbCursor.rowcount
                print("sql语句执行完毕")
            except:
                print("执行sql语句异常")
            # 关闭数据库连接资源
            finally:
                # 关闭游标
                if dbCursor is not None:
                    try:
                        dbCursor.close()
                        print("游标关闭成功")
                    except:
                        print("游标关闭异常")
                # 关闭数据库连接
                try:
                    self.close_conn()
                    print("数据库连接已关闭")
                except:
                    print("数据库连接关闭异常")
        return results

    # 关闭数据库连接
    def close_conn(self):
        if self.__mySqlConn is not None:
            self.__mySqlConn.close()
        else:
            print("未取得mysql连接，不需要关闭")

    def get_host(self):
        return self.__host

    def get_password(self):
        return self.__password

    def get_user(self):
        return self.__user

    def get_database(self):
        return self.__database

    # user:连接数据库的用户名 password:连接数据库用户的密码  database:数据库名称
    def __init__(self, host, user, password, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database


#  sql 语句
# 学生信息
# 查询所有学生信息
def get_sql_student():
    sql = "SELECT id, NAME,CASE WHEN sex=0 THEN'男' WHEN sex=1 THEN'女'  END sex,stuid,class FROM student"
    return sql


# 根据学生名查询学生ID
def get_sql_student_name_id(args):
    sql = "SELECT id FROM student WHERE NAME='%s'" % args
    return sql


# 查询学生学号是否存在
def get_sql_student_id(args):
    sql = "SELECT * FROM student WHERE stuid=%d" % args
    return sql


# 查询最大的学号
def get_sql_student_idMax():
    sql = "SELECT MAX(stuid) FROM student"
    return sql


# 模糊查询学生信息
def get_sql_student_like(args):
    sql = "SELECT id, NAME,CASE WHEN sex=0 THEN'男' WHEN sex=1 THEN'女'  END sex,stuid,class FROM student where 1=1 "
    if args[0] != "":
        sql += " and  NAME LIKE '%s'" % ("%" + args[0] + "%")
    if args[1] != "":
        sql += " and sex=%d" % (args[1])
    if args[2] != "":
        sql += " and stuid LIKE  '%s'" % ("%" + args[2] + "%")
    if args[3] != "":
        sql += " and class LIKE  '%s'" % ("%" + args[3] + "%")
    if args[4] != "":
        sql += " and id LIKE '%s'" % ("%" + args[4] + "%")
    return sql


# 删除学生信息
def get_sql_del_student(id):
    sql = "delete FROM student where id=%s" % id
    return sql


# 修改学生信息
def get_sql_update_student(args):
    sql = "UPDATE student SET NAME='%s',sex=%d,stuid='%s',class='%s' WHERE id=%d" % (
    args[0], args[1], args[2], args[3], args[4])
    return sql


# 添加学生信息
def get_sql_inster_student(args):
    sql = "INSERT INTO `achievement`.`student` (`name`, `sex`, `stuid`, `class`) VALUES ('%s', %d, '%s', '%s'); " % (
    args[0], args[1], args[2], args[3])
    return sql


# 课程表
# 查询课程信息
def get_sql_curriculum():
    sql = "select * from curriculum "
    return sql


# 查询所有课程名称
def get_sql_curriculum_name():
    sql = "SELECT coursename FROM curriculum"
    return sql


# 根据课程名查询课程ID
def get_sql_curriculum_id(cname):
    sql = "SELECT id FROM curriculum where coursename='%s'" % cname
    return sql


# 查询课程id信息
def get_sql_curriculum_number(args):
    sql = "SELECT * FROM curriculum WHERE coursenumber='%s'" % args
    return sql


# 查询最大的课程编号
def get_sql_curriculum_number_Max():
    sql = "SELECT MAX(coursenumber) FROM curriculum"
    return sql


# 删除课程信息
def get_sql_del_curriculum(id):
    sql = "delete FROM curriculum where id=%s" % id
    return sql


# 修改课程信息
def get_sql_update_curriculum(args):
    sql = "UPDATE curriculum SET coursenumber='%s',coursename='%s',courshours=%d,coursscore=%d WHERE id=%d" % (
    args[1], args[2], args[3], args[4], args[0])
    return sql


# 添加课程信息
def get_sql_inster_curriculum(args):
    sql = "INSERT INTO `achievement`.`curriculum` (`coursenumber`, `coursename`, `courshours`, `coursscore`) VALUES ('%s', '%s', %d, %d); " % (
    args[0], args[1], args[2], args[3])
    return sql


# 模糊查询课程信息
def get_sql_curriculum_like(args):
    sql = "select * from curriculum where 1=1 "
    if args[1] != "":
        sql += " and  coursenumber LIKE '%s'" % ("%" + args[1] + "%")
    if args[2] != "":
        sql += " and coursename LIKE  '%s'" % ("%" + args[2] + "%")
    if args[3] != "":
        sql += " and courshours LIKE  '%s'" % ("%" + args[3] + "%")
    if args[4] != "":
        sql += " and coursscore LIKE  '%s'" % ("%" + args[4] + "%")
    if args[0] != "":
        sql += " and id LIKE '%s'" % ("%" + args[0] + "%")
    return sql


# 成绩信息
# 查询全部成绩信息
def get_sql_result():
    sql = """SELECT student.`id`,student.`name`,curriculum.`coursename`,   result.`resulting`
    FROM  result,curriculum,student WHERE result.`Course_id`=curriculum.`id` AND student.`id`=result.`student_id` 
    """
    return sql


# 多条件模糊查询学生成绩信息
def get_sql_result_like(args):
    sql = """SELECT student.`id`,student.`name`,curriculum.`coursename`,   result.`resulting`
            FROM  result,curriculum,student WHERE result.`Course_id`=curriculum.`id` AND student.`id`=result.`student_id` """
    if args[0] != "":
        sql += " AND  student.`name` LIKE '%s' " % ('%' + args[0] + '%')
    if args[1] != "":
        sql += "AND curriculum.`coursename` LIKE '%s'" % ('%' + args[1] + '%')
    return sql


# 新增成绩信息
def insert_sql_result(args):
    sql = "INSERT INTO `achievement`.`result` (`Course_id`, `student_id`, `resulting`) VALUES (%d, %d, %d) " % (
    args[0], args[1], args[2])
    return sql


# 删除学生课程信息
def delete_sql_result(id):
    sql = "DELETE FROM result WHERE  student.`id`=%d" % id
    return sql


# 修改学生课程信息
def update_sql_result(args):
    sql = "UPDATE result SET resulting=%d WHERE student_id=%d AND Course_id=%d" % (args[0], args[1], args[2])
    return sql


# 主函数
if __name__ == '__main__':
    # 初始化Mysql连接工具类
    dbConnector = MySQLConnector("localhost", "root", "123456", "achievement")
