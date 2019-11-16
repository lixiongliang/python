'''
数据结构
'''

a = [1, 2, 3, 4.5, 6, 555.2, 99]

print(a.count(1), a.count(3), a.count(0))
a.insert(2, 222)

print(a)

print(a.index(2))

a.sort()
print(a)

print('(------------------------------')

statck = [3, 4, 5]
statck.append(6)
statck.append(7)
print(statck)

print(statck.pop())
print(statck.pop())
print(statck.pop())

from collections import deque

queue = deque(["eric", "mark", "alins"])
queue.append("Terry")
queue.append("lisi")
print(queue.popleft())

vex = [2, 4, 6]
for i in (3 * x for x in vex):
    print(i)

for i in [[x, x * 2] for x in vex]:
    print(i)

freshfuit = ['banana', 'huanggua', 'xihongsi']
print([pson.strip() for pson in freshfuit if pson == 'banana'])

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x * y for x in vec1 for y in vec2])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],

]

transposed = []
#transposed.append([[row[i] * 3 for row in matrix] for i in range(4)])
#print(transposed)

for i in range(4):
    transponsed_row = []
    for row in matrix:
        transponsed_row.append(row[i])
    transposed.append(transponsed_row)

print(transposed)


tt = 3,4,5,67,
print(tt[0])
u = tt,('a','b','c')
print(u)



basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('banana' in basket)


a = set('aaabaaaaaaaaa')
b =set('bbbbbbcbbbbbbb')

print(a)
print(b)


print(a -b)
print(b -a)
print(b -a)




'''
字典

'''

map = {"a":111,'b':2222}
print(map.get('a'))
print(map['a'])


print(list(map.keys()))

pp =dict([('a',133),('b',133)])
print(pp)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k,v in knights.items():
    print(k,v)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


