# Author:Tespera

'''
# while 循环
count = 0
while True:
    print("count",count)
    count = count + 1   # count +=1
    if count == 9:
        break             # break:结束整个循环。
'''

# for 循环
for i in range(0,10,2):   # 2 为步长
    print("loop",i)


for i in range(0,10):
    if i < 3:
        print("loop",i)
    else:
        continue           # contune:跳出本次循环继续下次循环。
    print("Yes...")




for i in range(10):
    print('----------',i )
    for j in range(10):
        print("j")
        if j >5:
            break
