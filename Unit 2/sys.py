# Author:Tespera
# Date:2017.8.14

# import sys
# print(sys.path)

import os

# cmd_res = os.system("dir")   # 执行命令，不保存结果
cmd_res = os.popen("dir").read()
print("-->", cmd_res)
# os.mkdir("new_dir")  # 创建文件夹

"""
# 三元运算
result = 值1 if 条件 else 值2
a,b,c = 1,2,3
d = a if a > b else c

"""


#数据类型
msg = "我爱北京天安门"
print(msg)
print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8")).decode(encoding = "utf-8")
