import random
import random as rd
from lib import pywin32_bootstrap



class Js():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Add(self):
        return self.a + self.b

    def c(self):
        return self.a * self.b

    def p(self):
        return self.a / self.b

    def j(self):
        return self.a - self.b


s1 = float(input('请输入：'))
s2 = float(input('请输入：'))
d = Js(s1, s2)
print("请选择：")
sf = input('"请输入是否要 1 乘、2 除、3 加、4 减："')
if sf == '1':
    print('法', d.Add())
else:
    if sf == '2':
        print('法' + d.c())
    else:
        if sf == '3':
            print('法' + d.p())
        else:
            if sf == '4':
                print('法' + d.j())
            else:
                print('pass')

