a = 21
b = 10
c = 0

c = a + b
print('a+b=', c)

c = a * b
print('a*b=', c)

# 运算符


c = a & b
print(c)

c = a | b
print(c)

c = a ^ b
print(c)

c = a << 2
print(c)

c = a >> 2
print(c)

import random

print ("uniform(5, 10) 的随机浮点数 : ",  round(random.uniform(5, 10),0))
print ("uniform(7, 14) 的随机浮点数 : ",  round(random.uniform(7, 14),0))


print ("randrange(1,100, 2) : ", random.randrange(0,100))

list = ['Google', 'Runoob', 1997, 2000]

print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)

del list[-1]
print("删除最后个元素 : ", list)

d  =  len(list)
print(d)
print(2 in [2,3])

list.append("haoweilai")
print(list)