# for i in range(10):
#     print(i)


# 奖池自定义
# ['笔记本一台','冰箱一台','奔驰一辆','谢谢惠顾'...]
# 用户进行积分抽奖 20积分抽一次
# 如果未中奖，告知用户没有中奖，还剩？积分，还能抽多少次
# 如果抽中，告知用户抽到了什么，还剩多少积分，还能抽多少次
# 抽完一次之后，如果积分足够，要询问用户，是否继续抽奖
# ---是 继续抽
# ---否 结束抽奖
import random

list1 = ['笔记本一台', '冰箱一台', '奔驰一辆', '谢谢惠顾', '中性笔', '', '', '', '', '', '']
'''
jf = float(input('您有多少积分：'))
n = jf / 20
for i in list1:
    if jf >= 20:
        random_value = random.choice(list1)
        if random_value in ['', '谢谢惠顾']:
            jf = jf - 20
            n = n - 1
            print(f'您未中奖,还剩{jf}点积分,还能抽{n}次')
            h = input("是否要抽奖:")
            if h == '是':
                print('开始抽奖！')
                continue
            else:
                if h == '否':
                    print(f'您还剩{jf}点积分,还能抽{n}次')
                    break
                else:
                    print('回答错误，跳出系统')
                    break
        else:
            jf = jf - 20
            n = jf // 20
            print(f'您中了{random_value},还剩{jf}点积分,还能抽{n}次')
            h = input("是否还要抽奖:")
            if h == '是':
                print('开始抽奖！')
                continue
            else:
                if h == '否':
                    print(f'您还剩{jf}点积分,还能抽{n}次')
                    break
                else:
                    print('回答错误，跳出系统')
                    break
    else:
        break
print("积分不足")
'''
# jf = float(input('您有多少积分：'))
# n = jf // 20
# while n >= 1:
#     if jf >= 20:
#         random_value = random.choice(list1)
#         jf = jf - 20
#         n = n - 1
#         if random_value in ['', '谢谢惠顾']:
#             print(f'您未中奖,还剩{jf}点积分,还能抽{n}次')
#             h = input("是否要抽奖:")
#             if h == '是':
#                 print('开始抽奖！')
#                 continue
#             else:
#                 if h == '否':
#                     print(f'您还剩{jf}点积分,还能抽{n}次')
#                     break
#                 else:
#                     print('回答错误，跳出系统')
#                     break
#         else:
#             print(f'您中了{random_value},还剩{jf}点积分,还能抽{n}次')
#             h = input("是否还要抽奖:")
#             if h == '是':
#                 print('开始抽奖！')
#                 continue
#             else:
#                 if h == '否':
#                     print(f'您还剩{jf}点积分,还能抽{n}次')
#                     break
#                 else:
#                     print('回答错误，跳出系统')
#                     break
#     else:
#         break
# print("积分不足")

# ------------------------------------------------
# s = 0
# for i in range(100):
#     i = i + 1
#     s = s + i
# print(s)

# print('------------------------------------------------------------')
# # 利用循环求出1-100所有数字之积
# s = 1
# for i in range(1, 100):
#     s = s * i
# print(s)
#
# print('------------------------------')
# # 求1-2+3-4+5-6...99所有数的和
# n = 0
# for i in range(100):
#     if i % 2 == 0:
#         n = n - i
#     else:
#         n = n + i
# print(n)
#
# t = 0
# n = 0
# while t <= 100:
#     t = t + 1
#     n = n + t
# print(n)


# for i in 序列:
#     for i in 字符串:    会从第一个到最后一个，来个遍
# for i in 字典:
#     for i in 元组:
#         for i in 列表:

# for i in [{1, 4, 6.7}, 3, 67, 'll']:
#     print(i)
#
# for i in [3, 67, 'll']:
#     print(i)
#
# for i in (3, 67, 'll'):
#     print(i)
#
# for i in 'java':
#     print(i)
#
# dic={'name':'java','user':'ww','add':'sh'}
# for i in dic.keys():
#     print(i)
# for i in dic.values():
#     print(i)

# _______________________________________________________________----


# 7、1-200之间所有奇数的和
# n = 0
# for i in range(1, 100):
#     if i % 2 != 0:
#         n = n + i
#     else:
#         continue
# print(n)
#
# # 8、本金10000元存入银行，年利率是千分之三。每过1年，将本金和利息相加作为新的本金。计算5年后，获得的本金是多少。
# p = 10000
# for i in range(1, 6):
#     b = p + p * 0.003
#     p = b
#
# print(b)

# 9、有如下两个列表，将名字和成绩一一对应添加到字典中，使用循环
# ls_nm = ['丁强', 'Eric', 'Peter', '张三', 'Alice']
# ls_sc = ['3:11', '3:21', '3:16', '3:41', '3:22']
# 例如：
# {'丁强':'3:11'}

'''
dic = {}
i = 0
for nm in ls_nm:
    for sc in ls_sc:
        dic[nm] = sc
        ls_sc.pop(0)
        break
print(dic)
'''

# ls_nm = ['丁强', 'Eric', 'Peter', '张三', 'Alice']
# ls_sc = ['3:11', '3:21', '3:16', '3:41', '3:22']
# dic = {}
# for i in range(len(ls_nm)):
#     k = ls_nm[i]
#     v = ls_sc[i]
#     dic[k] = v
# print(dic)

# ===============================================================================
# a = 'python'
# i = 0
# while i <= len(a):
#     print(a[i:i+1])
#     i = i+1
#
# a = 'python'
# i = 0
# while i <= len(a):
#     if a[i] == 't':
#         break
#     print(a[i:i+1])
#     i = i+1


# 登录系统
# 使用用户名和密码登录，如果用户名和密码正确提示登录成功，结束登录
# 如果登录使用提示重新登录，总共有三次机会，机会结束，没有登录成功提示账号被锁定

# i = 0
# dis = {"name": "admin", 'password': '12345a'}
# for i in range(0, 5):
#     userN = input('请输入用户名：')
#     passd = input('请输入密码：')
#     if userN == dis['name'] and passd == dis['password']:
#         print('登录成功,结束登录')
#         break
#     else:
#         print(i)
#         i = i + 1
#         if i < 3:
#             print("用户名或密码错误")
#             t = input('是否重新登录：')
#             if t == '是':
#                 continue
#             else:
#                 if t == '否':
#                     print("再见")
#                     break
#                 else:
#                     print("选择错误，请重新登陆")
#                     break
#         else:
#             print("尝试三次错误，退出登录,账户失效，请找管理员")
#             dis.pop('name')
#             break
# print("再见")











