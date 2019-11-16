#!/usr/bin/python3
# Filename: 06.py
# 导入模块
import support
import test05

# 现在可以调用模块里包含的函数了
support.print_func("Runoob")
test05.sayHell()


#str = input("please input")
#print("you input content: ",str)
print('------------------------------------')



'''


while True:
    try:
        x = int(input("please enter a numer; "))
        break
    except ValueError:
        print("Oops that was no valid number,try again")




'''



import sys

try:
    f= open("./a.txt")
    s = f.readline()
    i =int(s.strip())
    print(i)
except OSError as err:
    print("Os error:{0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])



class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print("my exception occurred ,value,",e.value)

