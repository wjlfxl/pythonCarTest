# lis = [1, 1.23, "apple", [1, 2, '上海', [8, 9, "apple", "orange"]], (1, 2), {'x': 'y', 'z': 1}]
# print(lis[4][1])  # 取 2
# lis[1] = 7.21
# print(lis)  # 修改单个列表值
#
# lis[:2:] = '改了值'
# print(lis)  # 修改多个列表值，会被拆分
# lis[:2] = ['改了值']
# print(lis)  # 修改多个列表值，以列表的方式就是一个整体
# lis[:3] = ['改了值', 'www']
# print(lis)  # 修改多个列表值，以列表的方式就是一个整体

# print(lis[::-2])
# lis[::-2] = ['改了值',23456,'ddddd']
# print(lis)  # 修改多个列表值，以列表的方式就是一个整体

# list1 = [123, 'dsdsff', 'dssfeewwrwr', 8.94]
# list1.append('eeeee')  # 末尾追加元素
# print(list1)
#
# list1.insert(2,'eeeee')
# print(list1)  # 按所有加元素
#
# list2 = [1,4,2.3,'rrrr']
# list1.extend(list2)
# print(list1)

#
# list1 = [123, 'dsdsff', 'dssfeewwrwr', 8.94,7,1067]
# list1.pop(-2)    # 按索引删
# print(list1)
#
# list1.remove(123)
# print(list1)      # 按内容删
#
# del list1[2]     # 按索引删
# print(list1)

# -----------------------------------------------------------------------------
# list1 = [123, 'dsdsff', 'dssfeewwrwr', 8.94, 7, 1067, 'dsdsff']
# print(list1.count('d'))  # 不完整元素无用
# print(list1.count('dsdsff'))  # 对元素统计出现次数
#
# print(list1.index('dsdsff', 2))  # 按内容查索引，可以添加次数
#
# list1.reverse()  # 反转列表
# print(list1)
#
# list1.clear()   # 请空
# print(list1)


# list1 = [1, 45, 7.3, 694, 909, 12.7]
# list1.sort()  # 永久排序
# print(list1)
#
# list1 = [1, 45, 7.3, 694, 909, 12.7]
# print(sorted(list1))   # 临时排序
# print(list1)  # 列表本质顺序没变
#
#
# print(len(list1))
# print(max(list1))
#
# print(min(list1))
# print(sum(list1))

# a = 20
# b = 'sdfsdg'
# print(list(a))
# print(list(b))

#
# list1 = (1, 45, 7.3, 694, 909, 12.7)
# list1[1] = 222

# -----------------------------------------------------------------------------------------
# 列表专项练习
# 定义一个列表list1，内容如下
# [9, 2, 3, 88, 'day', 'month', True, 'year',['great', 'day', 33]]
list1 = [9, 2, 3, 88, 'day', 'month', True, 'year', ['great', 'day', 33]]
# 1）取出列表中的数字，打印出来
a = list1[0:4]
b = list1[8][2]
list2 = [a, b]
print(list2)
# 2）判断布尔值True是否在列表中
print('True' in list1)
# 3）删除小列表最后一个值
del list1[8][2]
print(list1)
# 4）往大列表中最后追加一个值‘god’
list1.append('god')
print(list1)
# 5）指定在第二位添加一个值‘warning’
list1.insert(2, 'warning')
print(list1)
# 6）使用指定索引的方法删除‘warning’
list1.pop(2)
print(list1)
# 7）修改god的值为‘sorry’
list1[9] = 'sorry'
print(list1)
# 8）直接删除sorry（使用remove方法）
list1.remove('sorry')
print(list1)
# 9）查看当前列表的长度（有多少个值）
print(len(list1))
# 10）在小列表中第二位插入一个值‘super’
list1[8].insert(2, 'super')
print(list1)
# 11）清空小列表
list1[8].clear()  # 请空
print(list1)
# 12）取出前四个数字，然后永久降序排序
a = list1[0:4]
a.sort()
print(a)


lis = [1, 2, 50, 'good', 'nice', 'perf', 'bad']
# 1、取出'bad'
print(lis[6])
# 2、取出50,'good','nice'
print(lis[2:5])
# 3、添加 'apple'在列表末尾
lis.append('apple')
print(lis)
# 4、在nice后面加一个'orange'
lis.insert(5, 'orange')
print(lis)
# 5、在修改50的值为500
lis[2] = 500
print(lis)
# 6、在列表后加一个[60,70,80.3,'banala']
# lis2 = [60, 70, 80.3, 'banala']
# lis.append(lis2)
# print(lis)
lis2 = [60, 70, 80.3, 'banala']
lis.extend(lis2)
print(lis)

# 8、在修改'perf','bad'为 perfect
lis[6:8] = ['perfect']
print(lis)
# 9、取出2,'good'
lis3 = lis[1:4:2]
print(lis3)
# 10、取出'perf','bad'
lis4 = lis[6:8]
print(lis4)
# 11、修改1,'nice' 为80,'nicely'
lis[0] = 80
lis[4] = 'nicely'
print(lis)
# 12、删除'good'
lis.remove('good')
print(lis)
# 13、删除bad
lis.remove('bad')
print(lis)
#
#
# 元组专项练习
# 1）创建一个元组，命名为tup1
# ，包含以下内容('python', True, 2.88, 'day', (1, 2, 3), ['java', 'c++', 'python'])
tup1 = ('python', True, 2.88, 'day', (1, 2, 3), ['java', 'c++', 'python'])
# 2)取出元组中所有的python
a = tup1[0]
b = tup1[5][2]
print(a + b)
# 3）取出java和c++
print(tup1[5][:2:])
# 4）取出数字2
print(tup1[4][1])
# 5）打印java的对应下标   要先切出[]
i = tup1[-1].index('java')
print(i)

# 6）打印元组的长度
print(len(tup1))
# 8）返回列表中的python对应的索引下标
print(tup1.index('python'))
print(tup1[-1].index('python'))
# 9）倒着输出元组
print(tup1[::-1])
# 10）打印（1,2,3）子元组
print(tup1[4])
