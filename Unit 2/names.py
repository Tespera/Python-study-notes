# Author:Tespera
# Date:2017.8.14

import copy

names = "ZhangYang Guyua Xiangpeng XuliangChen"
names = ["ZhangYang", "Guyua", "Xiangpeng", ["Tespera","vvv"],"XuliangChen"]
names.append("LeiHaidong")   # 追加
names.insert(1,"ChenRonghua")    # 插队
names.insert(3,"XinZhiyu")    # 插队
names[2] = "XieDi"      # 更改
names.reverse()   #反转顺序
# names.clear()   #清空列表
# names.sort()    #排序（默认字母顺序，优先级：符号>数字>大写字母>小写字母）

# names2 = [1,2,3,4]
# names.extend()    # 合并列表
# del names2

names2 = names.copy()     # 复制
names[2] = "向鹏"
# names[3][0] = "TESPERA"   # 浅复制
names2 = copy.deepcopy(names)     # 深复制

# Delete    #删除
# names.remove("ChenRonghua")
# del names[1] = names.pop(1)
# names.pop(1)


print(names)
print(names[0],names[2])   # 取特定值
print(names[1:3])   # 切片
print(names[1:])   # 取第二个到最后一个
print(names[-1])   # 取最后一个
print(names[-3:-1])   # 取倒数第二第三
print(names[-3:])   # 取倒数后三个
print(names.index("XieDi"))    #取指定值的序号
print(names[names.index("XieDi")])
print(names.count("ChenRonghua"))  #统计相同个体的个数

