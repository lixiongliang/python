class Myclass:
    i = 12345
    def f(self):
        return "hello world"
    def __init__(self,a):
        self.data = a
        print("init")


x = Myclass(1)

print("Myclass i ",x.i)
print("Myclass f out  ",x.f())
print("Myclass f out  ",x.data)


'''
类的方法
'''
class People:
    name =''
    age = 0
    _weight = 0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self._weight=w

    def speak(self):
        print("%s speark: I %d old" %(self.name
              ,self.age))

p = People('root',10,30)
p.speak()

'''
继承

'''

class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

s = Student('ken',10,60,3)
s.speak()

class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic =t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class sample(Student,speaker):
    a = ""
    def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample('tem',24,90,4,'Python')
test.speak()



'''
方法重写

'''

class Parent:
    def spark(self):
        print("parent method")

class Child(Parent):
    def speak(self):
        print("child method")

c = Child()
c.speak()

super(Child,c).spark()


'''
类属性与方法
'''

