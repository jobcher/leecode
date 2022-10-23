# 运算符计算
#is和==区别
#is 用于判断两个变量引用对象是否为同一个(同一个内存空间)， == 用于判断引用变量的值是否相等。
a=[1,2,3]
b=a[:]
c=a
print(b is a)
print(b == a)

print(c is a)
print(c == a)

# x+=y 等同于 x=x+y
x=3
y=2
x += y
print(x)

# x-=y 等同于 x=x-y
x=3
y=2
x -= y
print(x)

# 常用的运算符优先级: 算术 > 比较 > 逻辑 > 赋值
result = 3-4 >=0 and 4*(6-2)>15
print(result)