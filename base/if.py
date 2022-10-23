#!/usr/bin/python3
"""
if 语句包含零个或多个 elif 子句及可选的 else 子句。
关键字 'elif' 是 'else if' 的缩写，适用于避免过多的缩进。
if ... elif ... elif ... 序列可以当作其他语言中 switch 或 case 语句的替代品。
如果要把一个值与多个常量进行比较，或者检查特定类型或属性，match 语句更实用。
"""
# 基本用法
flag = False
# 输入参数
name = input("输入name：")
# 判断输入是否是python
if name == 'python':
    flag=True
    print(r"this is 'if' python func")
else:
    print(name)

# 判断条件 多个值
"""
可以用   >（大于）
        < (小于)
        ==（等于）
        >=（大于等于）
        <=（小于等于）
来表示其关系
"""
# 强制数据类型转换 input默认为string
num = int(input("请输入数字："))
if num < 10:
    print("<10")
elif num == 11:
    print("==11")
elif num >= 20:
    print (">=20")
else:
    print ("error 12-19")

# 多条件判断
"""
当if有多个条件时可使用括号来区分判断的先后顺序，
括号中的判断优先执行
and 和 or 的优先级 低于 >（大于）、<（小于）等判断符号，
即大于和小于在没有括号的情况下会比与或要优先判断
"""
