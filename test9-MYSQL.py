import pymysql

# 连接数据库
conn = pymysql.connect(host='192.168.203.129', user='root', password='1qaz@WSX', database='bankDB')

# 创建游标对象
cursor = conn.cursor()
# 执行SQL语句
sql = "SELECT * FROM userInfo"
cursor.execute(sql)

# 查询数据
rows = cursor.fetchall()
for row in rows:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()

# =================================================================
conn = pymysql.connect(host='192.168.203.129', user='root', password='1qaz@WSX', database='bankDB')
# 创建一个游标对象
cursor = conn.cursor()
# 执行SQL插入语句
# cursor.execute("INSERT INTO userInfo (customerID,customerName,PID,telephone,address) VALUES (%s,%s,%s,%s,%s)",
#                ('8', 'John', '567891321242345614', '15683450856', '江苏苏州'))
# cursor.execute("update userInfo set customerName = %s, address = %s where customerID = 7 ", ('jj', '湖北武汉'))
cursor.execute("delete from userInfo where customerID = %s ", 8)
# 提交更改
conn.commit()
# 关闭连接
conn.close()
