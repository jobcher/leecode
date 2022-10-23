# python 循环函数

'''
while 循环
while 条件：
    条件满足：执行动作

continue 跳出本次循环，直接执行下一次循环
break   退出循环，执行循环外的代码
exit() 退出python程序，指定返回值

'''

i=10
while i>0:
    print(i,end=" \n")
    i-=1

# python for循环
# 用for循环来实现 1-100之间能被 5整除,同时能被3整除的数的和
sum1=0
for i in range(1,101):
    if i%5 == 0 and i%3 == 0:
        sum1+=i
print(sum1)

import random
num = random.randint(1,100)

while True:
    gnum = int(input("请输入数字:"))
    if gnum > num:
        print("bigger")
        continue
    elif gnum < num:
        print("smaller")
        continue
    else:
        print("right")
        break
