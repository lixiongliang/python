#!/usr/bin/python3
# Filename:  test05.py

def sayHell():
    print("Hello World")


def area(withs, height):
    return withs * height


print(area(20, 10))

sayHell()


# 传不可变对象实例
def changeInt(aa):
    aa = 10


b = 2
changeInt(b)
print(b, end=" ")


# 传可变对象实例
def changeme(mylist):
    "update list"
    mylist.append([1,2,3,4])
    print("print innr my list:", mylist)

mylist = [10, 20, 30]
changeme(mylist)
print("print  out my list:",mylist)

def printInfo(age ,name):
    print("name:",name)
    print("age:",age)
    return

printInfo(name='zhangsan',age=40)


#不定长参数
# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50,88)


# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)


sum = lambda arg1,agr2: arg1+ agr2

print("add ",sum(10,20))
