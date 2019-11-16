#input("\n\n enter exit"); input("yes")

age =10
if age>10:
    print("gather 10")
elif age ==10:
    print("equal 10")
else:
    print("small 10")

print("hello",end=" ")
print("hello",end=" ")

import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

from sys import  argv,path
#print('================python from import===================================')
#print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path


list = ['123','abc',222]
print(list)

list = [9]
print(list)


student  = {"lisi","wangwu","zhaoliu","zhaoliu"}

print(student)

if "lisi" in student:
    print("lisi in student")
else:
    print("list not in student")

a=set("abcwq3")
b=set("abc")
print(a)
print(a-b)


#Dictionary 字典
dict = {}
dict['one']=1
dict['one']=2
dict[2]=2
print(dict)
