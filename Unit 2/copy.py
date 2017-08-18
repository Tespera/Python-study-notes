# Author:Tespera
# Date:2017.8.15

import copy

person = ['name',['a',100]]

"""
p1 = copy.copy(person)   # 浅复制
p2 = person[:]
p3 = list(person)    # 工厂函数
"""

p1 = person[:]
p2 = person[:]

p1[0] = 'Tespera'
p2[0] = 'VVV'

p1[1][1] = 50

print(p1)
print(p2)