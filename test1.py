import sys

# print(input("请输入数字："))

# name1='www'
# name2='有钱'
# print(name1+name2)

# print('我们%s，但是%s' % ('有钱', '累'))


# x = 10
# y = 2
# print(x * y, x + y, x - y, x / y, x % y)

# x = 1999
# y = 35.9
# z = 'eeee'
# a = 'wwww'

# str1='whdsjshdfsfamngdf'
# print(str1[-3])
# str1=['whdsjshdfsfamngdf','sdhhjikhggf']
# print(str1[1][3])


# str1='whdsjshdfsfamngdf'
# print(str1[0:3])
# print(str1[3:7])
# print(str1[3:100])
# print(str1[:])    # 取所有的
# print(str1[3:])    # 可以单个省略，从第三个开始取
# print(str1[-3:6])    # 可以左右同时取
#
# str1=['whdsjshdfsfamngdf','sdhhjikhggf']
# print(str1[1][0:3])


# str1='容器是用来存放数据的，是一种把多个元素组织在一起的数据结构，容器中的元素可以逐个地迭代获取'
# print(str1[0:15:1])  # 一步一取
# print(str1[0:20:2])  # 两步一取
# print(str1[20:0:-2])  # 倒着两步一取
# print(str1[:-30:-1])  # 倒着两步一取


# -------------------------------------------------------------------------------------------------------------
# str1 = '字符串就是表示一串字符，字符可以是中文，英文或者数字，或者混合的文本'
# print(str1.index('中文'))  # 到中字
# print(str1.index('文'))  # 到第一个文字
# print(str1.index('文', 20, 30))  # 从20开始取，30结束，取第一个‘文’字

# print(str1.count('文'))  # 统计字出现的次数


# str2 = 'd hjkjcdfu ciDGHSKd cJdfs gjcHUIH'
#
# print(str2.lower())  # 变小写
# print(str2.upper())   # 变大写
# print(str2.swapcase())  # 大小写互换
# print(str2.title())  # 首字母大写

# str3 = 'my name is username , you are ok?'
#
# print(str3.split())  # 默认空格切割
# print(str3.split('m'))  # 以m切割 m不显示
# print(str3.split('m',1))  # 以m割  , 指定次数只切一次


# str5 = 'my name is 1234'
# str6 = '1234'
# print(str5.isdigit())
# print(str6.isdigit())


# str7 = 'my name is 1234'
# print('a' in str7)   # a 是否在str7中
# print('a' not in str7)

# a = 29.0
# print(type(a))
# str8 = str(a)
# print(type(str8))

# name1 = '有钱'
# name2 = '辛苦'
# print('我们%s,但是%s' %(name1, name2))   # 字符串拼接，占位符 老方法
#
# name1 = '有钱'
# name2 = '辛苦'
# print(f'我们{name1},但是{name2}')   # 格式化输出

# -------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# 定义变量passage，赋值为字符串，内容如下: '123Process finished with exit& code 0%'
passage='123Process finished with exit& code 0%'
# 1）倒着输出打印该字符串
print(passage[::-1])
# 2）截取'ss finished w’
print(passage[8:21])
# # 3）截取字符串的'exit'（使用正序和倒序两种）
print(passage[25:29])
print(passage[-13:-9:])
# # 5）截取后7位
print(passage[-7::])
# # 6）截取第4位到第12位
print(passage[3:11:])
print(passage[-35:-28:])

# 7）截取出exit，并且打印一句话'hello， please exit'（可以多种方法）
print('hello， please ' + passage[25:29])
# 8）判断‘fin’是否在该字符串中
print('fn' in passage)
# 9）将字符串所有单词首字母大写
print(passage.upper())
# 10）将字符串根据空格分割
print(passage.split())
# 11）判断字符串的前三位是否是纯数字组成
print(passage[:3:].isdigit())

message_01 = '十九届六中全会'
num_02 = 10
message_02 = '具体'
# 打印如下一句话   '十九届六中全会决议中的10个明确,10个明确具体指什么?'
print(f'{message_01}决议中的{num_02}个明确,{num_02}个明确{message_02}指什么?')

str1 = 'https://www.ctrip.com/?allianceid=1328&sid=40636030'
# 1、统计w出现的次数
print(str1.count('w'))
# 2、判断str1字符串是否是全数字组成
print(str1.isdigit())
# 3、判断1328是否在这个字符串中
print('1328' in str1)
# 4、all在字符串中的索引位置
print(str1.index('all'))
# 5、使用python替换字符串sid
print(str1.replace('sid', 'www'))
# 6、使用=对字符串进行切割
print(str1.split('='))
# 7、使用/对字符串进行切割
print(str1.split('/'))
# 8、分别将字符串全部转换成大写，小写
print(str1.upper())
print(str1.lower())
print(str1.swapcase())
# 9、统计字符串的长度
print(len(str1))
