# a = {'name': 'user', 'age': 22, 'addr': '苏州'}
#
# a['name'] = 'long'    # 修复键的值
# print(a)
# a['ph'] = 16587392789  # 加的键没有的话，默认增加一个键值对
# print(a)
# del a['ph']     # 删
# a.pop('addr')
# print(a)

# ---------------------------------------------------------------
# dic1 = {'name': 'user', 'age': 22, 'addr': '苏州'}
#
# k=dic1.keys()    # 返回所有的键
# print(k)
#
# v=dic1.values() # 返回所有的值
# print(v)
#
# i = dic1.items()   # 返回键值对
# print(i)

# ----------------------------------------------------------
# se = {'name','user','age',22,'addr','苏州'}   # 集合
# se1 = set()   # 空集合
# se2 = {1,4,6,1,7,343,4}   # 集合元素不能重复
# print(se2)


# se = {'name', 'user', 'age', 22, 'addr', '苏州'}
#
# se.add('phone')   # 增加元素
# print(se)
#
# se.pop()  # 随机删除
# print(se)
#
# se.remove(22)   # 指定元素删除
# print(se)
#
# se.discard('name')    # 错误保护机制   删除不存在的元素不包吃
# print(se)
#
# se.clear()   # 清空
# print(se)

# ----------------------------------------------------
# a = {'name', 'user', 'age', 22, 18, 40}
# b = {27, 22, 45}
# print(a - b)  # 去除相同的值
#
# print(a | b)  # 合并 去除重复
#
# print(a & b)  # 返回两个集合里相同的值
#
# print(a ^ b)  # 返回两个集合里不同的值


# _________________________________________________________________________________
# 字典专项练习
# 1、创建一个字典dic1 ，包含以下内容
# {'subject1': 'python', 'startdate': 'Monday', 'classroom': 411, 'student':['张三', '李四', '王小帅', '张三丰']}
dic1 = {'subject1': 'python', 'startdate': 'Monday', 'classroom': 411, 'student': ['张三', '李四', '王小帅', '张三丰']}
# 1）打印所有的值
print(dic1)
# 2）打印所有的键
print(dic1.keys())
# 3）打印所有学生的名字
print(dic1['student'])
# 4）修改学科为java
dic1['subject1'] = 'java'
print(dic1)
# 5）删除教室这一组键值对
dic1.pop('classroom')
print(dic1)
# 6）新增一个键值对 teacher : '老夫子'
dic1['teacher'] = '老夫子'
print(dic1)
# 7）新增一个学生'小峰'
dic1['student'].append('小峰')
print(dic1)
# 8）移除学生'张三'
dic1['student'].remove('张三')
print(dic1)

# 集合专项练习
# 创建一个集合，包含以下内容
yuwen = {'小明', '王凯', '李华', '周舟', '梁亮', '孟凡'}
tiyu = {'孟凡', '李华', '王凯', '张莉', '成华', '杨阳'}
# 1）找出只学了语文的学生
print(yuwen - tiyu)
# 2）找出既学习了语文的也学习了体育的学生
print(yuwen & tiyu)
# 3）找出只学了一门学科的学生
print(yuwen ^ tiyu)
# 4）找出学了语文或者学了体育其中任意一门的学生
print(yuwen | tiyu)
# 5）杨阳也学习语文，将他添加到yuwen中
yuwen.add('杨阳')
print(yuwen)
# 6）王凯没有时间学习体育，将他从体育中移除
tiyu.remove('王凯')
print(tiyu)
# 7）尝试删除学习yuwen的一个学生，王旺,(使用错误保护删除的方法）
yuwen.discard('王旺')
print(tiyu)
# 8）清空语文集合
yuwen.clear()
print(yuwen)

# 综合练习
list_test = [{'t1': [1, 2, 3], 't2': ('good', 'python')}, [233, True, ('java', 'fast')], 'apache']
# 1)往t1的值中追加一个数字4
list_test[0]['t1'].append(4)
print(list_test)
# 2)取出t2中的python，赋值给变量txt_01
txt_01 = list_test[0]['t2'][1]
print(txt_01)
# 3)定义一个变量num_02 = 2
num_02 = 2
# 格式化输出  I like python，今天是学习python的第2天
print(f'I like python，今天是学习python的第{num_02}天')
# 4)取出java中的ava
a = list_test[1]
b = a[2][0]
print(b[1::])
# 5)在233所在的列表中第2位插入一个元素  'China'
list_test[1].insert(1, 'china')
print(list_test)
# 6)修改True的值为字典中't1'对应的值
t1 = list_test[0]['t1']
list_test[1][2] = t1
print(list_test)
