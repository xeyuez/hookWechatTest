# coding=utf-8


# i = "你好,这个世界"
# print(i)
#
# if True:
#     print("true")
# else:
#     print("false")
#
# day = ["mon", "th", "thre"
#        "rhir", "fri"]
#
# word = 'word'
# swnt = "这是一个句子"
# para = """这厮i 一个段落
#
# print"""  #可以标记一个大段落
#
# '''
# 这是多行注释，使用单引号。
# 这是多行注释，使用单引号。
# 这是多行注释，使用单引号。
# '''
#
# """
# 这是多行注释，使用双引号。
# 这是多行注释，使用双引号。
# 这是多行注释，使用双引号。
# """
#
# #raw_input("按下 enter 键退出, 其他任意键显示 \n")
# x = "换行输出"
# y = "不换行输出"
# print(x)
#
#
# print(y),
# print(x),

# print(100 + 200 / 2 * 2)


# if 语句
# a = 00
# if a == 100 :
#     print(a)
# elif a == 200:
#     print(200)
# else:
#     print("elsesssss")


# for i in range(10):
#     print(i)

# for i in range(10, 9):
#     print(i)
#


# def fibb(n):
#     a,b = 0,1
#     while a < n:
#         print(a, end=', ')
#         a, b = b, a+b
#
# fibb(2000)


# print('hello, nideyue $: %s' % 22123000)
# lastYear = 72
# nowYear = 85
#
# upValue = nowYear - lastYear
#
# print('小明的成绩提升了%s个百分点'%upValue)

# 数组
# arr1 = ["1", "city", "good12","22"]
# print(arr1)
# # 增
# arr1.append("end")
# print(arr1)
# # 移
# b = arr1.pop()
# # 删
# arr1.remove("1")
# arr1.reverse(
# print(b)
# print((arr1))

# 元祖

# tu = ("s", "eee", 123, "")
# print(tu)
# tu2 = ("s")
# print(tu2)
#
# tu3 = ()
# print(tu3)

#
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[2][2])

# IF 循环
# s = input('请输入你的年龄: ')
# year = int(s)
# if year >= 1990 :
#     print("你好90后")
# elif year >= 1980:
#     print("你好80后")
# else :
#     print("你好")

# sum = 0
# for i in range(100):
#     sum = sum + i
#
# print(sum)
#


# value = 99
#
# while value > 0 :
#     value = value - 2
#     print(" value为:%s " %  value)
#
# print("结束")

# L = ['Bart', 'Lisa', 'Adam']
#
# for name in L :
#     print('hello: %s' % name)

# n = 1
# while n <= 100:
#     print('start')
#     if n > 10: # 当n = 11时，条件满足，执行break语句
#         break # break语句会结束当前循环
#     print(n)
#     n = n + 1
# print('END')

# for i in range(10) :
#     print('st')
#     if i > 5: continue //直接退出本次循环 开始下次循环
#             # break  直接退出循环
#
#     print(i)
#
# i = 2
# while i > 1 :
#     print(i)
#     i = i + 1

#

# 可变不可变数组
# let = {'a': 123} // 不可变
# var = {'b': ['123','456']} 可变
#
# print(let)
# print(var)
#
# 函数
# a = 500
# b = 12
#
# hex(a)
#
# print(hex(a))
# print(hex(b))
# 函数
# def return16jinzhi(intvalue) :
#     return  hex(intvalue)

# print(return16jinzhi(10.123873))

# 函数解 一元二次方程
# import math
# def quadict(a,b,c):
#     det =  (b*b-4*a*c)
#     if det < 0 :
#         print("abc三值错误, 无解")
#         return
#     x1 = (-b+math.sqrt(det))/(2*a)
#     x2 = (-b-math.sqrt(det))/(2*a)
#     return x1,x2
#
#
# value1 = quadict(2,10,3)
#
# print(value1)

# 函数 x的N次方 默认参数2次方
# def xn(x, n = 2):
#     value = x
#     while n>1:
#         value = value * x
#         n = n-1
#     return value
#
# sq = xn(2,2)
#
# print(sq)

# 函数默认参数
# def inputBody(name, sex, contry='中国', city='南京'):
#     print(name)
#     print(sex)
#     print(contry)
#     print(city)
#
# inputBody('abis','f',city="hangzhou")

# // 默认参数
# def addend(L=[]):
#     L.append('end')
#     return L
#
#
# a = ['1','2']
# b = addend(a)
# print(b)
#
# c = addend()
# print(c)
#
#
# d = addend()
# print(d)


#  *nums表示把nums这个list的所有元素作为可变参数传进去 *将参数作为默认参数穿进去 ** 是作为默认字典

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

# 命名关键字函数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
#
# def person(name, age, *, city, job):
#     print(name, age, city, job

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数 =、可变参数*、命名关键字参数*,key.  和关键字参数**


# 迭代
# import itertools

# a = {'s': 123, '123': "sd"}
# result = isinstance(a, Iterable)
#
# print(result)

# for 循环类似 swift  for item in items,  需要下标则使用 enmu


# 序列数组生成器
# value = [x * x for x in range(2,7) if x % 2 == 0]
# print(value)
#
# value2 = [x + y for x in ['x','y','z'] for y in ['1','2','3']]
#
# print(value2)

# import os
# a = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
# print(a)

# L = ['Hello', 'World', 18, 'Apple', None]
#
# a = [s.lower() for s in L if isinstance(s, str)] //列表生成式
# print(a)

# a = (x * x for x in range(2,7) if x % 2 == 0) #列表生成器
#
# for it in a:
#     print(it)


# 杨辉三角

# 1
# def triangles(x):
#     L = [1]
#     while x < 10:
#         yield L
#         L = [sum(i) for i in zip([0]+L, L+[0])]
#         x = x + 1
#
# 2
# def YangHui (num = 10):
#     LL = [[1]]
#     for i in range(1,num):
#         # value1 =
#         result = [(0 if j== 0 else LL[i-1][j-1])+ (0 if j ==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)]
#         LL.append(result)
#     return LL
#
# a = YangHui()
#
# # a = triangles(0)
#
# for i in a:
#     print(i)
#     print('\n')j
#
#

# 杨辉三角  for 循环方式
# def yanghui(maxLine):
#     lineArr = []  # 行
#     for i in range(0, maxLine+1):
#         hangArr = []  # 列
#         for j in range(0, i+1):
#             num = 1
#             if j == 0 or j == i:
#                 num = 1
#             else:
#                 num = lineArr[i-1][j-1] + lineArr[i-1][j]
#             hangArr.append(num)
#         lineArr.append(hangArr)
#
#     return lineArr

# 高阶函数
# c = abs
# def addAnyNum(x, y, f):
#     return  f(x) + f(y)
#
# a = addAnyNum(-100, 200, c)
#
# print(a)
#

# map 函数 类似于swift的闭包 //将首字母大写, 后面的大写转小写
# def normalize(name):
#     value: str = ''
#     for index, i in enumerate(name):
#         a = ord(i)
#         if index == 0 and a > 96:
#             a = a - 32
#         elif 64 < a < 96:
#             a = a + 32
#         b = chr(a)
#         value = value + b
#     return value
#
# L1 = ['adAm', 'LISA', 'baZT']
# L2 = list(map(normalize, L1))
# print(L2)

# 计算乘积
# def chji(x, y):
#     return x*y
#
# def prod(L):
#     return reduce(chji, L)
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# 将字符串转为浮点数

#
# from functools import reduce
#
# CHAR_TO_INT = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9
# }
#
# CHAR_TO_FLOAT = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '.': -1
# }
#
#
# def str2int(s):
#     ints = map(lambda ch: CHAR_TO_INT[ch], s)
#     return reduce(lambda x, y: x * 10 + y, ints)
#
# #
# # print(str2int('0'))
# # print(str2int('12300'))
# # print(str2int('0012345'))
#
#
#
# def str2float(s):
#     nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
#     point = 0
#
#     def to_float(f, n):
#         nonlocal point
#         if n == -1:
#             point = 1
#             return f
#         if point == 0:
#             return f * 10 + n
#         else:
#             point = point * 10
#             return f + n / point
#
#     return reduce(to_float, nums, 0.0)
#

# print(str2float('0'))
# print(str2float('123.456'))
# print(str2float('123.45600'))
# print(str2float('0.1234'))
# print(str2float('.1234'))
# print(str2float('120.0034'))


# 匿名函数改造代码
#
# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(lambda n : n % 2 == 0, range(1, 20)))
#
# print(L)


# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。 // 好像swift的扩展?
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# # 把@log放到now()函数的定义处，相当于执行了语句：
# # now = log(now)
# @log
# def now():
#     print('2019')
#
# now() # 添加在函数执行前运行的函数


# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# functools.partial(Int, base = 2) //给Int转换函数添加默认值
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。


# 类和实例
# del s.name # 如果删除实例的name属性

# class Student(object):
#     sex = 'f'
#     __score = '私有变量' # 私有变量对象无法访问
#     score1 = '成员变量'  # 属性可以访问
#
#     def __init__(self, name, age):
#         self.__score = name
#         self.age = age
#
#     def printscorevalue(self):
#         print(self.__score)
#
#     def getscore(self): # 返回给外部访问
#         return self.__score
#
#     def set_score(self,sqre):
#         self.__score = sqre
#
# b = Student('dddd', 22)
# b.count = 12 # 也是蛮6的  不需要先声明, 直接可以. 添加属性
#
# print(b.age)
# print(b.count)
# print(b.score1)
# b.printscorevalue()
#
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#     def set_gender(self, gender):
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#
#
#
# # 测试:
# bart = Student('Bart', 'male')
#
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# 继承和多态  python 是动态语言
#
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
# class Dog(Animal):
#     def run(self):
#         print('dog is running...')
#     def eat(self):
#         print('Eating meat...')
#
#
# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')
#
#
# dog = Dog()
# dog.run()
#
# cat = Cat()
# cat.run()
#
# print(isinstance(dog, Cat)) # 判断值是否是某种类型

# type 函数  判断类型
# print(type(224.0))  # float
# print(type(224))    # int
# print(type(str))    # type

# hasattr(obj, 'x') # 判断对象  有属性'x'吗？
# setattr(obj, 'y', 19) #给对象obj 设置一个属性'y'
# getattr(obj, 'y') # 获取对象obj的 属性'y' 如果试图获取不存在的属性，会抛出AttributeError的错误：
# 可以传入一个default参数，如果属性不存在，就返回默认值：
# getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404

# fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# fn() # 调用fn()与调用obj.power()是一样的

# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None
#
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
#
# 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。

# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count = Student.count + 1
#
# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')


# __slots__变量，来限制该class实例能添加的属性： 只对当前类起作用, 对子类不起作用
# class Student(object):  //只允许有name 与age两个属性
#     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称


# @property 可以吧get set 方法变成属性调用
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# >>> s = Student()
# >>> s.score = 60 # OK，实际转化为s.set_score(60)
# >>> s.score # OK，实际转化为s.get_score()


# 多继承   通过继承不同的类 获取不同的功能
# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):

# 定义好__str__()方法，返回一个好看的字符串
# >>> class Student(object):
# ...     def __init__(self, name):
# ...         self.name = name
# ...     def __str__(self):
# ...         return 'Student object (name: %s)' % self.name
# ...
# >>> print(Student('Michael'))
# Student object (name: Michael)

# __repr__()返回程序开发者看到的字符串, __str__()返回用户看到的字符串
# 定义方法返回字符串

# __iter__ 定义 该方法返回一个迭代对象, 然后不停的返回迭代对象返回的next()方法
# class Omg(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return  self
#
#     def __next__(self):
#         if self.a + self.b > 50 :
#             raise StopIteration  # 停止迭代
#         else:
#             print('a %d, b %d'%(self.a, self.b))
#             self.a, self.b = self.a+5, self.b+5
#             return self.a
# og = Omg()  # 迭代对象
# for n in og :
#     print(n)

# __getitem__
# Omg实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int): # n是索引
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice): # n是切片
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return Lclass Fib(object):
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# 最后，还有一个__delitem__()方法，用于删除某个元素。


# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
# class Student(object):
#
#     def __init__(self):
#         self.name = 'Michael'
#
#     def __getattr__(self, attr):
#         if attr=='score':
#             return 99
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
# ，这样，我们就有机会返回score的值
# 返回函数也是完全可以的：
# class Student(object):
#     def __getattr__(self, attr):
#         if attr=='age':
#             return lambda: 25
#
# 注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
#
# class Student(object):
#
#     def __getattr__(self, attr):
#         if attr=='age':
#             return lambda: 25
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


#   type()     函数既可以返回一个对象的类型，又可以创建出新的类型，比如，
# 我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
# >>> def fn(self, name='world'): # 先定义函数
# ...     print('Hello, %s.' % name)
# ...
# >>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class


# metaclass  可以创建出一个类, 动态的改变类的创建方法


# try
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
# 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
# 即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:           // 可以抛出不同类型的错误
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')
#
# finally 可以省略
# resutValue = open('notefound.txt','r')
#
# print(resutValue)
#
#
# 打开文件
# >>> f = open('/Users/michael/test.txt', 'r')

# from  tkinter import  *
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()
#
#
#     def
#
#
#
#
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()


# 在1966年，Seymour Papert和Wally Feurzig发明了一种专门给儿童学习编程的语言——LOGO语言，它的特色就是通过编程指挥一个小海龟（turtle）在屏幕上绘图。
#
# 海龟绘图（Turtle Graphics）后来被移植到各种高级语言中，Python内置了turtle库，基本上100%复制了原始的Turtle Graphics的所有功能。
#
# 我们来看一个指挥小海龟绘制一个长方形的简单代码：

# 导入turtle包的所有内容:
# from turtle import *

# 设置笔刷宽度:  话了一个长方形
# width(4)
#
# # 前进:
# forward(200)
# # 右转90度:
# right(90)
#
# # 笔刷颜色:
# pencolor('red')
# forward(100)
# right(90)
#
# pencolor('green')
# forward(200)
# right(90)
#
# pencolor('blue')
# forward(100)
# right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
# done()
# 在命令行运行上述代码，会自动弹出一个绘图窗口，然后绘制出一个长方形：
#
# rect
#
# 从程序代码可以看出，海龟绘图就是指挥海龟前进、转向，海龟移动的轨迹就是绘制的线条。要绘制一个长方形，只需要让海龟前进、右转90度，反复4次。
#
# 调用width()函数可以设置笔刷宽度，调用pencolor()函数可以设置颜色。更多操作请参考turtle库的说明。
#
# from turtle import *
#
# # 设置色彩模式是RGB:
# colormode(255)
#
# lt(90)
#
# lv = 14
# l = 120
# s = 45
#
# width(lv)
#
# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)
#
# penup()
# bk(l)
# pendown()
# fd(l)
# 画画1
# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()
#
#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)
#
#     l = 3.0 / 4.0 * l
#
#     lt(s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)
#
#     # restore the previous pen width
#     width(w)
#
# speed("fastest")
#
# draw_tree(l, 4)
#
# done()


# 画画2
# from turtle import *
# from random import *
# from math import *
#
# def tree(n, l):
#     pd() # 下笔
#     # 阴影效果
#     t = cos(radians(heading() + 45)) / 8 + 0.25
#     pencolor(t, t, t)
#     pensize(n / 3)
#     forward(l) # 画树枝
#
#
#     if n > 0:
#         b = random() * 15 + 10 # 右分支偏转角度
#         c = random() * 15 + 10 # 左分支偏转角度
#         d = l * (random() * 0.25 + 0.7) # 下一个分支的长度
#         # 右转一定角度，画右分支
#         right(b)
#         tree(n - 1, d)
#         # 左转一定角度，画左分支
#         left(b + c)
#         tree(n - 1, d)
#
#         # 转回来
#         right(c)
#     else:
#         # 画叶子
#         right(90)
#         n = cos(radians(heading() - 45)) / 4 + 0.5
#         pencolor(n, n*0.8, n*0.8)
#         circle(3)
#         left(90)

# # 添加0.3倍的飘落叶子
# if(random() > 0.7):
#     pu()
#     # 飘落
#     t = heading()
#     an = -40 + random()*40
#     setheading(an)
#     dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
#     forward(dis)
#     setheading(t)
#
#
#     # 画叶子
#     pd()
#     right(90)
#     n = cos(radians(heading() - 45)) / 4 + 0.5
#     pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
#     circle(2)
#     left(90)
#     pu()
#
#     #返回
#     t = heading()
#     setheading(an)
#     backward(dis)
#     setheading(t)
#
#     pu()
#     backward(l)# 退回
#
#
# bgcolor(0.5, 0.5, 0.5) # 背景色
# ht() # 隐藏turtle
# speed(0) # 速度，1-10渐进，0最快
# tracer(0, 0)
# pu() # 抬笔
# backward(100)
# left(90) # 左转90度
# pu() # 抬笔
# backward(300) # 后退300
# tree(12, 100) # 递归7层
# done()


# a = {"s": "s1"}
# print(a)
#
# a["s"] = "6666"
#
# print(a)


# 打开文件 read() 读取全部文件 read(Size) d读取一部分
# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
# 'r'以只读模式打开文件  //可以传入编码默认  或者默认
# with open('/Users/yuez/Downloads/移動產品定位.txt', 'r', encoding= 'gbk') as f:
#     for index, line in enumerate(f.readlines()): # 打印行
#         print('index: %d:  %s'%(index,line))

# with open('/Users/yuez/Downloads/WEB前端助手(FeHelper)_v2019.01.0714.crx', 'rb') as f:
#     print(f.read())

#  f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore') # errors 遇到非法编码的错误处理方式 ignore: 忽略错误

# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
# 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
# with open('/Users/yuez/Downloads/移動產品定位.txt', 'a') as f:  # 'w': 写模式,已存在会覆盖重写,  'a': 追加写
#     f.write('这次是追加模式, Hello, world2!')


# StringIO和BytesIO  内存中读写

# StringIO和BytesIO
# 阅读: 163018
# StringIO
# 很多时候，数据读写不一定是文件，也可以在内存中读写。
#
# StringIO顾名思义就是在内存中读写str。
#
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：

# from io import StringIO
# f = StringIO()
# f.write('hello')
# 5
# f.write(' ')
# 1
# f.write('world!')
# 6
# print(f.getvalue())
# hello world!

# >>> from io import StringIO
# >>> f = StringIO()
# >>> f.write('hello')
#
# BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
#
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
#
# >>> from io import BytesIO
# >>> f = BytesIO()
# >>> f.write('中文'.encode('utf-8'))
# 6
# >>> print(f.getvalue())


# 操作文件和目录
# import os
# os.name # 操作系统类型 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# print(os.uname()) //系统详细信息
# 环境变量
# print(os.environ) # 要获取某个环境变量的值，可以调用os.environ.get('key')：

# 查看当前目录的绝对路径:
# print(os.path.abspath('.'))  #/Users/yuez/Downloads/Python

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# a = os.path.join('/Users/yuez/Downloads', 'testdir6666')  # 标示出要建立的文件路径: /Users/yuez/Downloads/testdir6666
# os.mkdir(a)  # 建立文件夹
# os.rmdir(a) # 删除文件夹

# 两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2
# 而Windows下会返回这样的字符串：
# part-1\part-2

# 拆分路径也是一样:
# os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
#
# >>> os.path.split('/Users/michael/testdir/file.txt')
# ('/Users/michael/testdir', 'file.txt')
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
#
# >>> os.path.splitext('/path/to/file.txt')
# ('/path/to/file', '.txt')


# 对文件重命名:
# >>> os.rename('test.txt', 'test.py')
# # 删掉文件:
# >>> os.remove('test.py')
# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

# 获得当前目录下的所有文件夹
# a = [x for x in os.listdir('.') if os.path.isdir(x)]
# print(a)


# 序列化与反序列化 pickle
# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。 Python提供了pickle模块来实现序列化。
# 对象序列化并写入文件：

# import pickle
# d = dict(name='jack', age=18, scro=100)
# path = '/Users/yuez/Downloads/移動產品定位.txt'
# print(pickle.dumps(d)) # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# with open(path, 'wb') as f:
#     pickle.dump(d, f) # 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object 写入文件
#
#
# # 从文件打开  反序列化 从文件读取字符串
# with open(path, 'rb') as f:
#     d = pickle.load(f)
#     print(d)

# JSON
# import json
# d = dict(name='jack', age=18, scro=100, classs=dict(year=6, clases='1班'))
# j = json.dumps(d)  # dumps 把对象序列化为一个str,  dump 是吧对象序列化到文件中通pickle用法shi
# print(j)
#
# dic2 = json.loads(j)  # loads是json反序列化, load是从文件反序列化
# print(dic2)
# 打印结果:
# {"name": "jack", "age": 18, "scro": 100, "classs": {"year": 6, "clases": "1\u73ed"}}
# {'name': 'jack', 'age': 18, 'scro': 100, 'classs': {'year': 6, 'clases': '1班'}}


# 序列化类
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     @staticmethod
#     def student2dict(std):
#         return {
#             'name': std.name,
#             'age': std.age,
#             'score': std.score
#         }
#
#     @staticmethod
#     def dictToStudent(d):
#         return Student(d['name'], d['age'], d['score'])
#
# #序列化类
# s = Student('Bob', 20, 88)
# a = json.dumps(s, default=Student.student2dict)
# print(a)
# #反序列化类
# stu1 = json.loads(a, object_hook=s.dictToStudent)
# print(stu1)

# obj = dict(name='小明', age=20)
# s = json.dumps(obj, ensure_ascii=True) # ensure_ascii 编码格式
# print(s)


# 进程与线程
# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()   # pork出了一个子线程  fork存在 类Unix系统中
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# from multiprocessing import Process # 多系统可用
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#     for i in range(1,100):
#         print('child process %d'%i)
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()   # 启动
#     p.join()   #  join()  方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#     for i in range(1, 100):
#         print('Parent process %d' % i)
#     print('Child process end.')

# pool 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

# 多进程
# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     # for i in range(1,10000):
#     #     continue
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)  # 默认进程数
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))  # 异步执行 // 同时执行数为cpu核心数
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# 子进程
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)
#

# # 如果子进程还需要输入，则可以通过communicate()方法输入：
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode) # 上面的代码相当于在命令行执行命令nslookup，
# 然后手动输入：
# set q=mx
# python.org
# exit


# 进程间通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

# from multiprocessing import Process, Queue
# import os, time, random

# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate() #强行终止
#

#
# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，
# 因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# 所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。


# subprocess 模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
# 下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：

# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)
#

# # 如果子进程还需要输入，则可以通过communicate()方法输入：
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n') # 则可以通过communicate 继续启动
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)
# 上面的代码相当于在命令行执行命令nslookup，然后手动输入：
# set q=mx
# python.org
# exit


# 进程间通信
#
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
#
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:# coding=utf-8
#
#
# # i = "你好,这个世界"
# # print(i)
# #
# # if True:
# #     print("true")
# # else:
# #     print("false")
# #
# # day = ["mon", "th", "thre"
# #        "rhir", "fri"]
# #
# # word = 'word'
# # swnt = "这是一个句子"
# # para = """这厮i 一个段落
# #
# # print"""  #可以标记一个大段落
# #
# # '''
# # 这是多行注释，使用单引号。
# # 这是多行注释，使用单引号。
# # 这是多行注释，使用单引号。
# # '''
# #
# # """
# # 这是多行注释，使用双引号。
# # 这是多行注释，使用双引号。
# # 这是多行注释，使用双引号。
# # """
# #
# # #raw_input("按下 enter 键退出, 其他任意键显示 \n")
# # x = "换行输出"
# # y = "不换行输出"
# # print(x)
# #
# #
# # print(y),
# # print(x),
#
# # print(100 + 200 / 2 * 2)
#
#
# # if 语句
# # a = 00
# # if a == 100 :
# #     print(a)
# # elif a == 200:
# #     print(200)
# # else:
# #     print("elsesssss")
#
#
# # for i in range(10):
# #     print(i)
#
# # for i in range(10, 9):
# #     print(i)
# #
#
#
# # def fibb(n):
# #     a,b = 0,1
# #     while a < n:
# #         print(a, end=', ')
# #         a, b = b, a+b
# #
# # fibb(2000)
#
#
# # print('hello, nideyue $: %s' % 22123000)
# # lastYear = 72
# # nowYear = 85
# #
# # upValue = nowYear - lastYear
# #
# # print('小明的成绩提升了%s个百分点'%upValue)
#
# # 数组
# # arr1 = ["1", "city", "good12","22"]
# # print((arr1))
# # arr1.append("end")
# # print((arr1))
# #
# # b = arr1.pop()
# # print(b)
# # print((arr1))
#
# # 元祖
#
# # tu = ("s", "eee", 123, "")
# # print(tu)
# # tu2 = ("s")
# # print(tu2)
# #
# # tu3 = ()
# # print(tu3)
#
# #
# # L = [
# #     ['Apple', 'Google', 'Microsoft'],
# #     ['Java', 'Python', 'Ruby', 'PHP'],
# #     ['Adam', 'Bart', 'Lisa']
# # ]
# #
# # # 打印Apple:
# # print(L[0][0])
# # # 打印Python:
# # print(L[1][1])
# # # 打印Lisa:
# # print(L[2][2])
#
# # IF 循环
# # s = input('请输入你的年龄: ')
# # year = int(s)
# # if year >= 1990 :
# #     print("你好90后")
# # elif year >= 1980:
# #     print("你好80后")
# # else :
# #     print("你好")
#
# # sum = 0
# # for i in range(100):
# #     sum = sum + i
# #
# # print(sum)
# #
#
#
# # value = 99
# #
# # while value > 0 :
# #     value = value - 2
# #     print(" value为:%s " %  value)
# #
# # print("结束")
#
# # L = ['Bart', 'Lisa', 'Adam']
# #
# # for name in L :
# #     print('hello: %s' % name)
#
# # n = 1
# # while n <= 100:
# #     print('start')
# #     if n > 10: # 当n = 11时，条件满足，执行break语句
# #         break # break语句会结束当前循环
# #     print(n)
# #     n = n + 1
# # print('END')
#
# # for i in range(10) :
# #     print('st')
# #     if i > 5: continue //直接退出本次循环 开始下次循环
# #             # break  直接退出循环
# #
# #     print(i)
# #
# # i = 2
# # while i > 1 :
# #     print(i)
# #     i = i + 1
#
# #
#
# # 可变不可变数组
# # let = {'a': 123}
# # var = {'b': ['123','456']}
# #
# # print(let)
# # print(var)
# #
# # 函数
# # a = 500
# # b = 12
# #
# # hex(a)
# #
# # print(hex(a))
# # print(hex(b))
# # 函数
# # def return16jinzhi(intvalue) :
# #     return  hex(intvalue)
#
# # print(return16jinzhi(10.123873))
#
# # 函数解 一元二次方程
# # import math
# # def quadict(a,b,c):
# #     det =  (b*b-4*a*c)
# #     if det < 0 :
# #         print("abc三值错误, 无解")
# #         return
# #     x1 = (-b+math.sqrt(det))/(2*a)
# #     x2 = (-b-math.sqrt(det))/(2*a)
# #     return x1,x2
# #
# #
# # value1 = quadict(2,10,3)
# #
# # print(value1)
#
# # 函数 x的N次方 默认参数2次方
# # def xn(x, n = 2):
# #     value = x
# #     while n>1:
# #         value = value * x
# #         n = n-1
# #     return value
# #
# # sq = xn(2,2)
# #
# # print(sq)
#
# # 函数默认参数
# # def inputBody(name, sex, contry='中国', city='南京'):
# #     print(name)
# #     print(sex)
# #     print(contry)
# #     print(city)
# #
# # inputBody('abis','f',city="hangzhou")
#
# # // 默认参数
# # def addend(L=[]):
# #     L.append('end')
# #     return L
# #
# #
# # a = ['1','2']
# # b = addend(a)
# # print(b)
# #
# # c = addend()
# # print(c)
# #
# #
# # d = addend()
# # print(d)
#
#
# #  *nums表示把nums这个list的所有元素作为可变参数传进去 *将参数作为默认参数穿进去 ** 是作为默认字典
#
# # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
#
# # 命名关键字函数
# # 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# #
# # def person(name, age, *, city, job):
# #     print(name, age, city, job
#
# # 参数组合
# # 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# # 但是请注意，参数定义的顺序必须是：必选参数、默认参数 =、可变参数*、命名关键字参数*,key.  和关键字参数**
#
#
# # 迭代
# # import itertools
#
# # a = {'s': 123, '123': "sd"}
# # result = isinstance(a, Iterable)
# #
# # print(result)
#
# # for 循环类似 swift  for item in items,  需要下标则使用 enmu
#
#
# # 序列数组生成器
# # value = [x * x for x in range(2,7) if x % 2 == 0]
# # print(value)
# #
# # value2 = [x + y for x in ['x','y','z'] for y in ['1','2','3']]
# #
# # print(value2)
#
# # import os
# # a = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
# # print(a)
#
# # L = ['Hello', 'World', 18, 'Apple', None]
# #
# # a = [s.lower() for s in L if isinstance(s, str)] //列表生成式
# # print(a)
#
# # a = (x * x for x in range(2,7) if x % 2 == 0) #列表生成器
# #
# # for it in a:
# #     print(it)
#
#
# # 杨辉三角
#
# # 1
# # def triangles(x):
# #     L = [1]
# #     while x < 10:
# #         yield L
# #         L = [sum(i) for i in zip([0]+L, L+[0])]
# #         x = x + 1
# #
# # 2
# # def YangHui (num = 10):
# #     LL = [[1]]
# #     for i in range(1,num):
# #         # value1 =
# #         result = [(0 if j== 0 else LL[i-1][j-1])+ (0 if j ==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)]
# #         LL.append(result)
# #     return LL
# #
# # a = YangHui()
# #
# # # a = triangles(0)
# #
# # for i in a:
# #     print(i)
# #     print('\n')j
# #
# #
#
# # 杨辉三角  for 循环方式
# # def yanghui(maxLine):
# #     lineArr = []  # 行
# #     for i in range(0, maxLine+1):
# #         hangArr = []  # 列
# #         for j in range(0, i+1):
# #             num = 1
# #             if j == 0 or j == i:
# #                 num = 1
# #             else:
# #                 num = lineArr[i-1][j-1] + lineArr[i-1][j]
# #             hangArr.append(num)
# #         lineArr.append(hangArr)
# #
# #     return lineArr
#
# # 高阶函数
# # c = abs
# # def addAnyNum(x, y, f):
# #     return  f(x) + f(y)
# #
# # a = addAnyNum(-100, 200, c)
# #
# # print(a)
# #
#
# # map 函数 类似于swift的闭包 //将首字母大写, 后面的大写转小写
# # def normalize(name):
# #     value: str = ''
# #     for index, i in enumerate(name):
# #         a = ord(i)
# #         if index == 0 and a > 96:
# #             a = a - 32
# #         elif 64 < a < 96:
# #             a = a + 32
# #         b = chr(a)
# #         value = value + b
# #     return value
# #
# # L1 = ['adAm', 'LISA', 'baZT']
# # L2 = list(map(normalize, L1))
# # print(L2)
#
# # 计算乘积
# # def chji(x, y):
# #     return x*y
# #
# # def prod(L):
# #     return reduce(chji, L)
# #
# #
# # print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# # if prod([3, 5, 7, 9]) == 945:
# #     print('测试成功!')
# # else:
# #     print('测试失败!')
#
# # 将字符串转为浮点数
#
# #
# # from functools import reduce
# #
# # CHAR_TO_INT = {
# #     '0': 0,
# #     '1': 1,
# #     '2': 2,
# #     '3': 3,
# #     '4': 4,
# #     '5': 5,
# #     '6': 6,
# #     '7': 7,
# #     '8': 8,
# #     '9': 9
# # }
# #
# # CHAR_TO_FLOAT = {
# #     '0': 0,
# #     '1': 1,
# #     '2': 2,
# #     '3': 3,
# #     '4': 4,
# #     '5': 5,
# #     '6': 6,
# #     '7': 7,
# #     '8': 8,
# #     '9': 9,
# #     '.': -1
# # }
# #
# #
# # def str2int(s):
# #     ints = map(lambda ch: CHAR_TO_INT[ch], s)
# #     return reduce(lambda x, y: x * 10 + y, ints)
# #
# # #
# # # print(str2int('0'))
# # # print(str2int('12300'))
# # # print(str2int('0012345'))
# #
# #
# #
# # def str2float(s):
# #     nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
# #     point = 0
# #
# #     def to_float(f, n):
# #         nonlocal point
# #         if n == -1:
# #             point = 1
# #             return f
# #         if point == 0:
# #             return f * 10 + n
# #         else:
# #             point = point * 10
# #             return f + n / point
# #
# #     return reduce(to_float, nums, 0.0)
# #
#
# # print(str2float('0'))
# # print(str2float('123.456'))
# # print(str2float('123.45600'))
# # print(str2float('0.1234'))
# # print(str2float('.1234'))
# # print(str2float('120.0034'))
#
#
# # 匿名函数改造代码
# #
# # def is_odd(n):
# #     return n % 2 == 1
# #
# # L = list(filter(lambda n : n % 2 == 0, range(1, 20)))
# #
# # print(L)
#
#
# # 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# # 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。 // 好像swift的扩展?
# # def log(func):
# #     def wrapper(*args, **kw):
# #         print('call %s():' % func.__name__)
# #         return func(*args, **kw)
# #     return wrapper
# #
# #
# # # 把@log放到now()函数的定义处，相当于执行了语句：
# # # now = log(now)
# # @log
# # def now():
# #     print('2019')
# #
# # now() # 添加在函数执行前运行的函数
#
#
# # 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# # functools.partial(Int, base = 2) //给Int转换函数添加默认值
# # 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
#
#
# # 类和实例
# # del s.name # 如果删除实例的name属性
#
# # class Student(object):
# #     sex = 'f'
# #     __score = '私有变量' # 私有变量对象无法访问
# #     score1 = '成员变量'  # 属性可以访问
# #
# #     def __init__(self, name, age):
# #         self.__score = name
# #         self.age = age
# #
# #     def printscorevalue(self):
# #         print(self.__score)
# #
# #     def getscore(self): # 返回给外部访问
# #         return self.__score
# #
# #     def set_score(self,sqre):
# #         self.__score = sqre
# #
# # b = Student('dddd', 22)
# # b.count = 12 # 也是蛮6的  不需要先声明, 直接可以. 添加属性
# #
# # print(b.age)
# # print(b.count)
# # print(b.score1)
# # b.printscorevalue()
# #
# # 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
#
# # class Student(object):
# #     def __init__(self, name, gender):
# #         self.name = name
# #         self.__gender = gender
# #     def set_gender(self, gender):
# #         self.__gender = gender
# #
# #     def get_gender(self):
# #         return self.__gender
# #
# #
# #
# # # 测试:
# # bart = Student('Bart', 'male')
# #
# # if bart.get_gender() != 'male':
# #     print('测试失败!')
# # else:
# #     bart.set_gender('female')
# #     if bart.get_gender() != 'female':
# #         print('测试失败!')
# #     else:
# #         print('测试成功!')
#
# # 继承和多态  python 是动态语言
# #
# # class Animal(object):
# #     def run(self):
# #         print('Animal is running...')
# #
# # class Dog(Animal):
# #     def run(self):
# #         print('dog is running...')
# #     def eat(self):
# #         print('Eating meat...')
# #
# #
# # class Cat(Animal):
# #     def run(self):
# #         print('Cat is running...')
# #
# #
# # dog = Dog()
# # dog.run()
# #
# # cat = Cat()
# # cat.run()
# #
# # print(isinstance(dog, Cat)) # 判断值是否是某种类型
#
# # type 函数  判断类型
# # print(type(224.0))  # float
# # print(type(224))    # int
# # print(type(str))    # type
#
# # hasattr(obj, 'x') # 判断对象  有属性'x'吗？
# # setattr(obj, 'y', 19) #给对象obj 设置一个属性'y'
# # getattr(obj, 'y') # 获取对象obj的 属性'y' 如果试图获取不存在的属性，会抛出AttributeError的错误：
# # 可以传入一个default参数，如果属性不存在，就返回默认值：
# # getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
#
# # fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn # fn指向obj.power
# # <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# # fn() # 调用fn()与调用obj.power()是一样的
#
# # def readImage(fp):
# #     if hasattr(fp, 'read'):
# #         return readData(fp)
# #     return None
# #
# # 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
# #
# # 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
#
# # class Student(object):
# #     count = 0
# #
# #     def __init__(self, name):
# #         self.name = name
# #         Student.count = Student.count + 1
# #
# # # 测试:
# # if Student.count != 0:
# #     print('测试失败!')
# # else:
# #     bart = Student('Bart')
# #     if Student.count != 1:
# #         print('测试失败!')
# #     else:
# #         lisa = Student('Bart')
# #         if Student.count != 2:
# #             print('测试失败!')
# #         else:
# #             print('Students:', Student.count)
# #             print('测试通过!')
#
#
# # __slots__变量，来限制该class实例能添加的属性： 只对当前类起作用, 对子类不起作用
# # class Student(object):  //只允许有name 与age两个属性
# #     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
#
#
# # @property 可以吧get set 方法变成属性调用
# # class Student(object):
# #
# #     @property
# #     def score(self):
# #         return self._score
# #
# #     @score.setter
# #     def score(self, value):
# #         if not isinstance(value, int):
# #             raise ValueError('score must be an integer!')
# #         if value < 0 or value > 100:
# #             raise ValueError('score must between 0 ~ 100!')
# #         self._score = value
# # >>> s = Student()
# # >>> s.score = 60 # OK，实际转化为s.set_score(60)
# # >>> s.score # OK，实际转化为s.get_score()
#
#
# # 多继承   通过继承不同的类 获取不同的功能
# # class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#
# # 定义好__str__()方法，返回一个好看的字符串
# # >>> class Student(object):
# # ...     def __init__(self, name):
# # ...         self.name = name
# # ...     def __str__(self):
# # ...         return 'Student object (name: %s)' % self.name
# # ...
# # >>> print(Student('Michael'))
# # Student object (name: Michael)
#
# # __repr__()返回程序开发者看到的字符串, __str__()返回用户看到的字符串
# # 定义方法返回字符串
#
# # __iter__ 定义 该方法返回一个迭代对象, 然后不停的返回迭代对象返回的next()方法
# # class Omg(object):
# #     def __init__(self):
# #         self.a, self.b = 0, 1
# #
# #     def __iter__(self):
# #         return  self
# #
# #     def __next__(self):
# #         if self.a + self.b > 50 :
# #             raise StopIteration  # 停止迭代
# #         else:
# #             print('a %d, b %d'%(self.a, self.b))
# #             self.a, self.b = self.a+5, self.b+5
# #             return self.a
# # og = Omg()  # 迭代对象
# # for n in og :
# #     print(n)
#
# # __getitem__
# # Omg实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# # class Fib(object):
# #     def __getitem__(self, n):
# #         if isinstance(n, int): # n是索引
# #             a, b = 1, 1
# #             for x in range(n):
# #                 a, b = b, a + b
# #             return a
# #         if isinstance(n, slice): # n是切片
# #             start = n.start
# #             stop = n.stop
# #             if start is None:
# #                 start = 0
# #             a, b = 1, 1
# #             L = []
# #             for x in range(stop):
# #                 if x >= start:
# #                     L.append(a)
# #                 a, b = b, a + b
# #             return Lclass Fib(object):
# # 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# # 最后，还有一个__delitem__()方法，用于删除某个元素。
#
#
# # __getattr__
# # 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
# # class Student(object):
# #
# #     def __init__(self):
# #         self.name = 'Michael'
# #
# #     def __getattr__(self, attr):
# #         if attr=='score':
# #             return 99
# # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
# # ，这样，我们就有机会返回score的值
# # 返回函数也是完全可以的：
# # class Student(object):
# #     def __getattr__(self, attr):
# #         if attr=='age':
# #             return lambda: 25
# #
# # 注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
# #
# # class Student(object):
# #
# #     def __getattr__(self, attr):
# #         if attr=='age':
# #             return lambda: 25
# #         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
#
#
# #   type()     函数既可以返回一个对象的类型，又可以创建出新的类型，比如，
# # 我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
# # >>> def fn(self, name='world'): # 先定义函数
# # ...     print('Hello, %s.' % name)
# # ...
# # >>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
#
#
# # metaclass  可以创建出一个类, 动态的改变类的创建方法
#
#
# # try
# # 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
# # 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
# # 即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
# # try:
# #     print('try...')
# #     r = 10 / int('2')
# #     print('result:', r)
# # except ValueError as e:           // 可以抛出不同类型的错误
# #     print('ValueError:', e)
# # except ZeroDivisionError as e:
# #     print('ZeroDivisionError:', e)
# # else:
# #     print('no error!')
# # finally:
# #     print('finally...')
# # print('END')
# #
# # finally 可以省略
# # resutValue = open('notefound.txt','r')
# #
# # print(resutValue)
# #
# #
# # 打开文件
# # >>> f = open('/Users/michael/test.txt', 'r')
#
# # from  tkinter import  *
# #
# # class Application(Frame):
# #     def __init__(self, master=None):
# #         Frame.__init__(self, master)
# #         self.pack()
# #         self.createWidgets()
# #
# #     def createWidgets(self):
# #         self.helloLabel = Label(self, text='Hello, world!')
# #         self.helloLabel.pack()
# #         self.quitButton = Button(self, text='Quit', command=self.quit)
# #         self.quitButton.pack()
# #
# #
# #     def
# #
# #
# #
# #
# # app = Application()
# # # 设置窗口标题:
# # app.master.title('Hello World')
# # # 主消息循环:
# # app.mainloop()
#
#
# # 在1966年，Seymour Papert和Wally Feurzig发明了一种专门给儿童学习编程的语言——LOGO语言，它的特色就是通过编程指挥一个小海龟（turtle）在屏幕上绘图。
# #
# # 海龟绘图（Turtle Graphics）后来被移植到各种高级语言中，Python内置了turtle库，基本上100%复制了原始的Turtle Graphics的所有功能。
# #
# # 我们来看一个指挥小海龟绘制一个长方形的简单代码：
#
# # 导入turtle包的所有内容:
# # from turtle import *
#
# # 设置笔刷宽度:  话了一个长方形
# # width(4)
# #
# # # 前进:
# # forward(200)
# # # 右转90度:
# # right(90)
# #
# # # 笔刷颜色:
# # pencolor('red')
# # forward(100)
# # right(90)
# #
# # pencolor('green')
# # forward(200)
# # right(90)
# #
# # pencolor('blue')
# # forward(100)
# # right(90)
#
# # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
# # done()
# # 在命令行运行上述代码，会自动弹出一个绘图窗口，然后绘制出一个长方形：
# #
# # rect
# #
# # 从程序代码可以看出，海龟绘图就是指挥海龟前进、转向，海龟移动的轨迹就是绘制的线条。要绘制一个长方形，只需要让海龟前进、右转90度，反复4次。
# #
# # 调用width()函数可以设置笔刷宽度，调用pencolor()函数可以设置颜色。更多操作请参考turtle库的说明。
# #
# # from turtle import *
# #
# # # 设置色彩模式是RGB:
# # colormode(255)
# #
# # lt(90)
# #
# # lv = 14
# # l = 120
# # s = 45
# #
# # width(lv)
# #
# # # 初始化RGB颜色:
# # r = 0
# # g = 0
# # b = 0
# # pencolor(r, g, b)
# #
# # penup()
# # bk(l)
# # pendown()
# # fd(l)
# # 画画1
# # def draw_tree(l, level):
# #     global r, g, b
# #     # save the current pen width
# #     w = width()
# #
# #     # narrow the pen width
# #     width(w * 3.0 / 4.0)
# #     # set color:
# #     r = r + 1
# #     g = g + 2
# #     b = b + 3
# #     pencolor(r % 200, g % 200, b % 200)
# #
# #     l = 3.0 / 4.0 * l
# #
# #     lt(s)
# #     fd(l)
# #
# #     if level < lv:
# #         draw_tree(l, level + 1)
# #     bk(l)
# #     rt(2 * s)
# #     fd(l)
# #
# #     if level < lv:
# #         draw_tree(l, level + 1)
# #     bk(l)
# #     lt(s)
# #
# #     # restore the previous pen width
# #     width(w)
# #
# # speed("fastest")
# #
# # draw_tree(l, 4)
# #
# # done()
#
#
# # 画画2
# # from turtle import *
# # from random import *
# # from math import *
# #
# # def tree(n, l):
# #     pd() # 下笔
# #     # 阴影效果
# #     t = cos(radians(heading() + 45)) / 8 + 0.25
# #     pencolor(t, t, t)
# #     pensize(n / 3)
# #     forward(l) # 画树枝
# #
# #
# #     if n > 0:
# #         b = random() * 15 + 10 # 右分支偏转角度
# #         c = random() * 15 + 10 # 左分支偏转角度
# #         d = l * (random() * 0.25 + 0.7) # 下一个分支的长度
# #         # 右转一定角度，画右分支
# #         right(b)
# #         tree(n - 1, d)
# #         # 左转一定角度，画左分支
# #         left(b + c)
# #         tree(n - 1, d)
# #
# #         # 转回来
# #         right(c)
# #     else:
# #         # 画叶子
# #         right(90)
# #         n = cos(radians(heading() - 45)) / 4 + 0.5
# #         pencolor(n, n*0.8, n*0.8)
# #         circle(3)
# #         left(90)
#
# # # 添加0.3倍的飘落叶子
# # if(random() > 0.7):
# #     pu()
# #     # 飘落
# #     t = heading()
# #     an = -40 + random()*40
# #     setheading(an)
# #     dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
# #     forward(dis)
# #     setheading(t)
# #
# #
# #     # 画叶子
# #     pd()
# #     right(90)
# #     n = cos(radians(heading() - 45)) / 4 + 0.5
# #     pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
# #     circle(2)
# #     left(90)
# #     pu()
# #
# #     #返回
# #     t = heading()
# #     setheading(an)
# #     backward(dis)
# #     setheading(t)
# #
# #     pu()
# #     backward(l)# 退回
# #
# #
# # bgcolor(0.5, 0.5, 0.5) # 背景色
# # ht() # 隐藏turtle
# # speed(0) # 速度，1-10渐进，0最快
# # tracer(0, 0)
# # pu() # 抬笔
# # backward(100)
# # left(90) # 左转90度
# # pu() # 抬笔
# # backward(300) # 后退300
# # tree(12, 100) # 递归7层
# # done()
#
#
# # a = {"s": "s1"}
# # print(a)
# #
# # a["s"] = "6666"
# #
# # print(a)
#
#
# # 打开文件 read() 读取全部文件 read(Size) d读取一部分
# # 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
# # 'r'以只读模式打开文件  //可以传入编码默认  或者默认
# # with open('/Users/yuez/Downloads/移動產品定位.txt', 'r', encoding= 'gbk') as f:
# #     for index, line in enumerate(f.readlines()): # 打印行
# #         print('index: %d:  %s'%(index,line))
#
# # with open('/Users/yuez/Downloads/WEB前端助手(FeHelper)_v2019.01.0714.crx', 'rb') as f:
# #     print(f.read())
#
# #  f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore') # errors 遇到非法编码的错误处理方式 ignore: 忽略错误
#
# # 写文件
# # 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
# # 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
# # with open('/Users/yuez/Downloads/移動產品定位.txt', 'a') as f:  # 'w': 写模式,已存在会覆盖重写,  'a': 追加写
# #     f.write('这次是追加模式, Hello, world2!')
#
#
# # StringIO和BytesIO  内存中读写
#
# # StringIO和BytesIO
# # 阅读: 163018
# # StringIO
# # 很多时候，数据读写不一定是文件，也可以在内存中读写。
# #
# # StringIO顾名思义就是在内存中读写str。
# #
# # 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
#
# # from io import StringIO
# # f = StringIO()
# # f.write('hello')
# # 5
# # f.write(' ')
# # 1
# # f.write('world!')
# # 6
# # print(f.getvalue())
# # hello world!
#
# # >>> from io import StringIO
# # >>> f = StringIO()
# # >>> f.write('hello')
# #
# # BytesIO
# # StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# #
# # BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
# #
# # >>> from io import BytesIO
# # >>> f = BytesIO()
# # >>> f.write('中文'.encode('utf-8'))
# # 6
# # >>> print(f.getvalue())
#
#
# # 操作文件和目录
# import os
# # os.name # 操作系统类型 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# # print(os.uname()) //系统详细信息
# # 环境变量
# # print(os.environ) # 要获取某个环境变量的值，可以调用os.environ.get('key')：
#
# # 查看当前目录的绝对路径:
# # print(os.path.abspath('.'))  #/Users/yuez/Downloads/Python
#
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# # a = os.path.join('/Users/yuez/Downloads', 'testdir6666')  # 标示出要建立的文件路径: /Users/yuez/Downloads/testdir6666
# # os.mkdir(a)  # 建立文件夹
# # os.rmdir(a) # 删除文件夹
#
# # 两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# # 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# # part-1/part-2
# # 而Windows下会返回这样的字符串：
# # part-1\part-2
#
# # 拆分路径也是一样:
# # os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
# #
# # >>> os.path.split('/Users/michael/testdir/file.txt')
# # ('/Users/michael/testdir', 'file.txt')
# # os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
# #
# # >>> os.path.splitext('/path/to/file.txt')
# # ('/path/to/file', '.txt')
#
#
# # 对文件重命名:
# # >>> os.rename('test.txt', 'test.py')
# # # 删掉文件:
# # >>> os.remove('test.py')
# # shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
#
# # 获得当前目录下的所有文件夹
# # a = [x for x in os.listdir('.') if os.path.isdir(x)]
# # print(a)
#
#
# # 序列化与反序列化 pickle
# # 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# # 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# # 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# # 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。 Python提供了pickle模块来实现序列化。
# # 对象序列化并写入文件：
#
# # import pickle
# # d = dict(name='jack', age=18, scro=100)
# # path = '/Users/yuez/Downloads/移動產品定位.txt'
# # print(pickle.dumps(d)) # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# # with open(path, 'wb') as f:
# #     pickle.dump(d, f) # 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object 写入文件
# #
# #
# # # 从文件打开  反序列化 从文件读取字符串
# # with open(path, 'rb') as f:
# #     d = pickle.load(f)
# #     print(d)
#
# # JSON
# import json
# # d = dict(name='jack', age=18, scro=100, classs=dict(year=6, clases='1班'))
# # j = json.dumps(d)  # dumps 把对象序列化为一个str,  dump 是吧对象序列化到文件中通pickle用法shi
# # print(j)
# #
# # dic2 = json.loads(j)  # loads是json反序列化, load是从文件反序列化
# # print(dic2)
# # 打印结果:
# # {"name": "jack", "age": 18, "scro": 100, "classs": {"year": 6, "clases": "1\u73ed"}}
# # {'name': 'jack', 'age': 18, 'scro': 100, 'classs': {'year': 6, 'clases': '1班'}}
#
#
# #序列化类
# # class Student(object):
# #     def __init__(self, name, age, score):
# #         self.name = name
# #         self.age = age
# #         self.score = score
# #
# #     @staticmethod
# #     def student2dict(std):
# #         return {
# #             'name': std.name,
# #             'age': std.age,
# #             'score': std.score
# #         }
# #
# #     @staticmethod
# #     def dictToStudent(d):
# #         return Student(d['name'], d['age'], d['score'])
# #
# # #序列化类
# # s = Student('Bob', 20, 88)
# # a = json.dumps(s, default=Student.student2dict)
# # print(a)
# # #反序列化类
# # stu1 = json.loads(a, object_hook=s.dictToStudent)
# # print(stu1)
#
# # obj = dict(name='小明', age=20)
# # s = json.dumps(obj, ensure_ascii=True) # ensure_ascii 编码格式
# # print(s)
#
#
# # 进程与线程
# # import os
# #
# # print('Process (%s) start...' % os.getpid())
# # # Only works on Unix/Linux/Mac:
# # pid = os.fork()   # pork出了一个子线程  fork存在 类Unix系统中
# # if pid == 0:
# #     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# # else:
# #     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
#
#
# # from multiprocessing import Process # 多系统可用
# # import os
# #
# # # 子进程要执行的代码
# # def run_proc(name):
# #     print('Run child process %s (%s)...' % (name, os.getpid()))
# #     for i in range(1,100):
# #         print('child process %d'%i)
# #
# # if __name__=='__main__':
# #     print('Parent process %s.' % os.getpid())
# #     p = Process(target=run_proc, args=('test',))
# #     print('Child process will start.')
# #     p.start()   # 启动
# #     p.join()   # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
# #     for i in range(1, 100):
# #         print('Parent process %d' % i)
# #     print('Child process end.')
#
# # pool 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
# # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#
# # 多进程
# # from multiprocessing import Pool
# # import os, time, random
# #
# # def long_time_task(name):
# #     print('Run task %s (%s)...' % (name, os.getpid()))
# #     # for i in range(1,10000):
# #     #     continue
# #     start = time.time()
# #     time.sleep(random.random() * 3)
# #     end = time.time()
# #     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
# #
# # if __name__=='__main__':
# #     print('Parent process %s.' % os.getpid())
# #     p = Pool(4)  # 默认进程数
# #     for i in range(5):
# #         p.apply_async(long_time_task, args=(i,))  # 异步执行 // 同时执行数为cpu核心数
# #     print('Waiting for all subprocesses done...')
# #     p.close()
# #     p.join()
# #     print('All subprocesses done.')
#
# # 子进程
# # 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
# # subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
# # import subprocess
# #
# # print('$ nslookup www.python.org')
# # r = subprocess.call(['nslookup', 'www.python.org'])
# # print('Exit code:', r)
# #
#
# # # 如果子进程还需要输入，则可以通过communicate()方法输入：
# # print('$ nslookup')
# # p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# # print(output.decode('utf-8'))
# # print('Exit code:', p.returncode) # 上面的代码相当于在命令行执行命令nslookup，
# # 然后手动输入：
# # set q=mx
# # python.org
# # exit
#
#
# # 进程间通信
# # Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
# # Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
# # 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
#
# from multiprocessing import Process, Queue
# import os, time, random
#
# # # 写数据进程执行的代码:
# # def write(q):
# #     print('Process to write: %s' % os.getpid())
# #     for value in ['A', 'B', 'C']:
# #         print('Put %s to queue...' % value)
# #         q.put(value)
# #         time.sleep(random.random())
# #
# # # 读数据进程执行的代码:
# # def read(q):
# #     print('Process to read: %s' % os.getpid())
# #     while True:
# #         value = q.get(True)
# #         print('Get %s from queue.' % value)
# #
# # if __name__=='__main__':
# #     # 父进程创建Queue，并传给各个子进程：
# #     q = Queue()
# #     pw = Process(target=write, args=(q,))
# #     pr = Process(target=read, args=(q,))
# #     # 启动子进程pw，写入:
# #     pw.start()
# #     # 启动子进程pr，读取:
# #     pr.start()
# #     # 等待pw结束:
# #     pw.join()
# #     # pr进程里是死循环，无法等待其结束，只能强行终止:
# #     pr.terminate() #强行终止
# #
#
# #
# # 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，
# # 因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# # 所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。
#
#
#
# # subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
# #
# # 下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
#
# import subprocess
#
# # print('$ nslookup www.python.org')
# # r = subprocess.call(['nslookup', 'www.python.org'])
# # print('Exit code:', r)
# #
#
# # # 如果子进程还需要输入，则可以通过communicate()方法输入：
# # print('$ nslookup')
# # p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # output, err = p.communicate(b'set q=mx\npython.org\nexit\n') # 则可以通过communicate 继续启动
# # print(output.decode('utf-8'))
# # print('Exit code:', p.returncode)
# # 上面的代码相当于在命令行执行命令nslookup，然后手动输入：
# # set q=mx
# # python.org
# # exit
#
#
# # 进程间通信
# #
# # Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
# #
# # 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
#
# # from multiprocessing import Process, Queue
# # import os, time, random
# #
# # # 写数据进程执行的代码:
# # def write(q):
# #     print('Process to write: %s' % os.getpid())
# #     for value in ['A', 'B', 'C']:
# #         print('Put %s to queue...' % value)
# #         q.put(value)
# #         time.sleep(random.random())
# #
# # # 读数据进程执行的代码:
# # def read(q):
# #     print('Process to read: %s' % os.getpid())
# #     while True:
# #         value = q.get(True)
# #         print('Get %s from queue.' % value)
# #
# # if __name__=='__main__':
# #     # 父进程创建Queue，并传给各个子进程：
# #     q = Queue()
# #     pw = Process(target=write, args=(q,))
# #     pr = Process(target=read, args=(q,))
# #     # 启动子进程pw，写入:
# #     pw.start()
# #     # 启动子进程pr，读取:
# #     pr.start()
# #     # 等待pw结束:
# #     pw.join()
# #     # pr进程里是死循环，无法等待其结束，只能强行终止:
# #     pr.terminate()
# #
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()
#


# 线程
# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
#
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
#
# import time, threading
#
# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running1...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t2 = threading.Thread(target=loop, name='LoopThread2')
# t2.start()
# t2.join()
# t.start()
# t.join()   #join同步执行, 等待子线程执行结束, 没有join异步执行
# print('thread %s ended1.' % threading.current_thread().name)

#  lock 线程锁
#       先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()


#  死循环  会占据100%cpu, python的多线程是假的,解释器还会添加一个锁, 锁住执行代码, 一百行换一次线程
# import threading, multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

#
# import base64
# a = base64.b64encode(b'321')
# print(a)

# import hashlib
#
# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
#
# def login(user, password):
#     apsw = db[user]
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     amd5str = md5.hexdigest()
#     print("how%s: apsw: %s  amd5: %s" % (user,apsw,amd5str))
#
#     if apsw == amd5str:
#         return True
#     else: return False
#
# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')


# # 第一个python图形程序  等待输入 显示
#
# from tkinter import *
# import tkinter.messagebox as messagebox
#
# class abc(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)
#
# app = abc()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()


# turtle包本身只是一个绘图库，但是配合Python代码，就可以绘制各种复杂的图形。例如，通过循环绘制5个五角星：

# from turtle import *
#
# def drawStar(x, y):
#     pu()
#     goto(x, y)
#     pendown()
#     # set heading: 0
#     seth(0)
#     for i in range(5):
#         forward(40)
#         right(144)
#         # fd(40)
#         # rt(144)
#
# for x in range(0, 50, 50):
#     print("%s " % x)
#     drawStar(x, 0)
#
# done()

# fd = forward
# bk = back
# backward = back
# rt = right
# lt = left
# position = pos
# setpos = goto
# setposition = goto
# seth = setheading


# # 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))
#
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 使用递归，可以绘制出非常复杂的图形。例如，下面的代码可以绘制一棵分型树：
#
# from turtle import *
# import random
#
# # 设置色彩模式是RGB:
# colormode(255)
#
# left(90)  # 初始方向从左向右 转90度则从下向上
#
# lv = 8   # 最大层数
# l = 12   # 初始长度
# s = 20    # 转向角度
#
# width(lv)
# penup()
# bk(l)  # back 返回
# pendown()
# fd(l)  # forward 前进
#
# def draw_tree(l, level):
#     print('长度l: %s 层级level: %s' % (l, level))
#
#     global r, g, b
#     # save the current pen width
#     w = width()
#     # narrow the pen width
#     width(w * 3.0 / 4.0)  # 宽度 越来越窄
#     # set color:  # 固定颜色
#     # r = r + 1
#     # g = g + 2
#     # b = b + 3
#     pencolor(random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))    #随机颜色
#
#     l = 0.9 * l  # 长度 越来越短
#
#     left(s)
#     forward(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)   # 向左画到lv累加
#     back(l)    # 在层下一层返回 向右画
#     right(2 * s) # 向右画, 初始是左转, 右转转一次角度为原来方向再一次为向右方
#     forward(l)
#
#     if level < lv:   # 右一层也画完 再向左
#         draw_tree(l, level + 1)
#     back(l)
#     left(s)
#
#     # restore the previous pen width
#     width(w)
#
#
# speed("fastest")
#
# draw_tree(l, 1)
# done()

#
# from turtle import *
# from random import *
# from math import *
# def tree(n, l):
#     pd()
#     t = cos(radians(heading() + 45)) / 8 + 0.25
#     pencolor(t, t, t)
#     pensize(n / 4)
#     forward(l)
#     if n > 0:
#         b = random() * 15 + 10
#         c = random() * 15 + 10
#         d = l * (random() * 0.35 + 0.6)
#         right(b)
#         tree(n - 1, d)
#         left(b + c)
#         tree(n - 1, d)
#         right(c)
#     else:
#         right(90)
#         n = cos(radians(heading() - 45)) / 4 + 0.5
#         pencolor(n, n, n)
#         circle(2)
#         left(90)
#
#     pu()
#     backward(l)
#
#
#
# bgcolor(0.5, 0.5, 0.5)
# ht()
# speed(0)
# tracer(0, 0)
# left(90)
# pu()
# backward(300)
# tree(13, 100)
# done()


# python 绘图
# from turtle import *
# from random import *
# from math import *
#
# def tree(n, l):
#     pd() # 下笔
#     # 阴影效果
#     t = cos(radians(heading() + 45)) / 8 + 0.25
#     pencolor(t, t, t)
#     pensize(n / 3)
#     forward(l) # 画树枝
#
#
#     if n > 0:
#         b = random() * 15 + 10 # 右分支偏转角度
#         c = random() * 15 + 10 # 左分支偏转角度
#         d = l * (random() * 0.25 + 0.7) # 下一个分支的长度
#         # 右转一定角度，画右分支
#         right(b)
#         tree(n - 1, d)
#         # 左转一定角度，画左分支
#         left(b + c)
#         tree(n - 1, d)
#
#         # 转回来
#         right(c)
#     else:
#         # 画叶子
#         right(90)
#         n = cos(radians(heading() - 45)) / 4 + 0.5
#         pencolor(n, n*0.8, n*0.8)
#         circle(3)
#         left(90)
#
#         # 添加0.3倍的飘落叶子
#         if(random() > 0.7):
#             pu()
#             # 飘落
#             t = heading()
#             an = -40 + random()*40
#             setheading(an)
#             dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
#             forward(dis)
#             setheading(t)
#
#
#             # 画叶子
#             pd()
#             right(90)
#             n = cos(radians(heading() - 45)) / 4 + 0.5
#             pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
#             circle(2)
#             left(90)
#             pu()
#
#             #返回
#             t = heading()
#             setheading(an)
#             backward(dis)
#             setheading(t)
#
#     pu()
#     backward(l)# 退回
#
# bgcolor(0.5, 0.5, 0.5) # 背景色
# ht() # 隐藏turtle
# speed(0) # 速度，1-10渐进，0最快
# tracer(0, 0)
# pu() # 抬笔
# backward(100)
# left(90) # 左转90度
# pu() # 抬笔
# backward(300) # 后退300
# tree(12, 100) # 递归7层
# done()


# 网络编程  tcp
# 导入socket库: 客户端向一个服务器发送请求
# import socket
#
# # 创建一个socket:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 建立连接:
# s.connect(('www.sina.com.cn', 80))
#
# # 发送数据
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# # 关闭连接:
# s.close()
#
#
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)


# # 服务器 代码
# import socket
# import threading
# import time
#
# # 创建一个基于IPv4和TCP协议的Socket：
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 用9999这个端口号。请注意，小于1024的端口号必须要有管理员权限才能绑定：
# s.bind(('127.0.0.1', 9999))
# # 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
# s.listen(5)
# print('Waiting for connection...')
# # 服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
#
# #每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
# def tcplink(sock, addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         a = ('Hello, %s!' % data.decode('utf-8')).encode('utf-8')
#         print("send: %s"%a)
#         sock.send(a)
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)
#
# while True:
#     # 接受一个新连接:
#     sock, addr = s.accept()
#     # 创建新线程来处理TCP连接:
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()

# log
# Waiting for connection...
# Accept new connection from 127.0.0.1:52697...
# send: b'Hello, Michael!'
# send: b'Hello, Tracy!'
# send: b'Hello, Sarah!'
# Connection from 127.0.0.1:52697 closed.


# 客户端代码
# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('127.0.0.1', 9999))
# # 接收欢迎消息:
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()

# log
# Welcome!
# Hello, Michael!
# Hello, Tracy!
# Hello, Sarah!


# UDP 连接
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # 绑定端口:
# s.bind(('127.0.0.1', 9999))
# # 创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：
#
# print('Bind UDP on 9999...')
# while True:
#     # 接收数据:
#     data, addr = s.recvfrom(1024)
#     print(data)
#     print('Received from %s:%s.' % addr)
#     b = input()
#     c = b.encode('utf-8')
#     print(c)
#     s.sendto(c, addr)
#
#


# 数据库
# # 导入SQLite驱动:
# import sqlite3
# # 连接到SQLite数据库
# # 数据库文件是test.db
# # 如果文件不存在，会自动在当前目录创建:
# conn = sqlite3.connect('testdatabase.db')
# # 创建一个Cursor: 用来执行查询语句
# cursor = conn.cursor()
# # 执行一条SQL语句，创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# #<sqlite3.Cursor object at 0x10f8aa260>
# # 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# #<sqlite3.Cursor object at 0x10f8aa260>
# # 通过rowcount获得插入的行数:
# cursor.rowcount
# #1
# # 关闭Cursor:
# cursor.close()
# # 提交事务:
# conn.commit()
# # 关闭Connection:
# conn.close()
#
# import sqlite3
# # 我们再试试查询记录：
# conn = sqlite3.connect('testdatabase.db')
# cursor = conn.cursor()
# # 执行查询语句:
# cursor.execute('select * from user where id=?', ('1',))
# #<sqlite3.Cursor object at 0x10f8aa340>
# # 获得查询结果集:
# values = cursor.fetchall()
# print('查询的数据%s'%values)
# # values
# # [('1', 'Michael')]
# cursor.close()
# conn.close()
# 使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。
#
# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
#
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
#
# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))


# web 网页服务器
# 无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。
# 复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。
# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
#     return [body.encode('utf-8')]
#
# # server.py
# # 从wsgiref模块导入:
# from wsgiref.simple_server import make_server
#
# # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
# httpd = make_server('', 8000, application)
# print('Serving HTTP on port 8000...')
# # 开始监听HTTP请求:
# httpd.serve_forever()
# # 你可以在地址栏输入用户名作为URL的一部分，将返回Hello, xxx!： http://127.0.0.1:8000/yumez
#

# 使用模板
# from flask import Flask, request, render_template
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return render_template('home.html')
#
# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return render_template('form.html')
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     username = request.form['username']
#     password = request.form['password']
#     if username=='admin' and password=='password':
#         return render_template('signin-ok.html', username=username)
#     return render_template('form.html', message='Bad username or password', username=username)
#
# if __name__ == '__main__':
#     app.run()


# form.html'  #网页
# <html>
# <head>
#   <title>Please Sign In</title>
# </head>
# <body>
#   {% if message %}
#   <p style="color:red">{{ message }}</p>
#   {% endif %}
#   <form action="/signin" method="post">
#     <legend>Please sign in:</legend>
#     <p><input name="username" placeholder="Username" value="{{ username }}"></p>
#     <p><input name="password" placeholder="Password" type="password"></p>
#     <p><button type="submit">Sign In</button></p>
#   </form>
# </body>
# </html>


# 异步io 异步操作执行程序, 并且是在一个线程中, 类似于cpu中断操作
# import asyncio
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()