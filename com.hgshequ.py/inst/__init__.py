'''


num1 = input("input ")
num2 = input("input")

sum = float(num1) + float(num2)

print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))

print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))


'''
# n = float(input("input"))
# n_sqrt = n**2
#
# print('%0.0f的平方根为 %0.0f'%(n,n_sqrt))




#
# import cmath
#
# num = int(input("请输入一个数字: "))
# num_sqrt = cmath.sqrt(num)
# print('{0} 的平方根为 {1:0.3f}+{2:0.3f}'.format(num ,num_sqrt.real,num_sqrt.imag))
#
# #
#
# a = float(input("请输入一个实数字: "))
# b = float(input("请输入一个虚数字: "))
# num_sqrt = cmath.sqrt(complex(a, b))
# print('{0:0.3f}+ {1:0.3f}j 8的平方根为 {2:0.3f}+{3:0.3f}j'.format(a, b, num_sqrt.real, num_sqrt.imag))


#celsius = (fahrenheit - 32) / 1.8
#fahrenheit = (celsius * 1.8) + 32
#
# celsius = float(input("input 摄氏度："))
# fahrenheit = (celsius*1.8)+32
# print("%0.1f 摄氏度转为华氏度为 %0.1f "%(celsius,fahrenheit))
#
#
# x = input("x:")
# y= input("y:")
# x,y = y,x
# print('x:{}'.format(x))
# print('y:{}'.format(y))

#
# year = int(input("input a year: "))
# if(year % 4)==0:
#     if(year % 100) == 0:
#         if(year % 400) == 0:
#             print("{0} is run nian".format(year))
#         else:
#             print("{0} is not run nian".format(year))
#     else:
#         print("{0} is run nian".format(year))
# else:
#     print("{0} is not run nian".format(year))
#

#九九乘法表
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}x{}={}".format(j,i,j*i),end=' ')
#     print()

#
# dec = int(input("inpt a:"))
# print("十进制：",dec)
# print("十进制到二进制：",bin(dec))
# print("十进制到八进制：",oct(dec))
# print("十进制到十六进制：",hex(dec))

#
# str = 'Runoob'
# print(str[::-1])
#
# print(''.join(reversed(str)))

def partition(arr,low,high):
    i = low -1
    print('start low:',low)
    print('start high:', high)
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high]= arr[high],arr[i+1]
    return i+1


def quickSort(arr,low,high):
    if low< high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr, pi+1, high)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("排序后的数组:")
for i in range(n):
    print ("%d" %arr[i]),


import pip

print(pip.__version__)












































