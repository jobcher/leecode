# python 变量
import keyword
# 不能使用的变量名称
print(keyword.kwlist)
# 变量的创建
num = 100
num = num - 20
print(num)
# 变量值的交换
a = 1
b = 2
print(a,b)

a,b = b,a
print(a,b)
# 变量的类型
name = "jobcher"
age = 18
height = 1.8
marry = False

print(type(name))
print(type(age))
print(type(height))
print(type(marry))

# 变量类型转换
age = str(age)
print("your name: "+name+"\nyour age： "+age)