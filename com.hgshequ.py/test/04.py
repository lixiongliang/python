#!/usr/bin/python3
# Filename: 04.py
a, b = 0, 1
while b < 10:
    # print(b)
    #  print(b,end=',')
    a, b = b, a + b

list = [1, 2, 3, 4]
it = iter(list)

import sys

for x in it:
    print(x, end=" ")


class MyNumbers:
    def __iter__(self):
        print("init")
        self.a = 1
        return self

    def __next__(self):
        print("__next__")
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

# print('------------------------')

def fuvibacci(n):
    a,b,counter = 0,1,0


