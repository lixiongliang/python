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