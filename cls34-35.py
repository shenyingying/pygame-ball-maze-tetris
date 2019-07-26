# -*- coding: utf-8 -*-
# @Time    : 19-7-16 下午4:21
# @Author  : shenyingying
# @Email   : shen222ying@163.com
# @File    : cls34-35.py
# @Software: PyCharm

# 访问限制

'''如果要让内部属性不被外部访问,可以把属性名字前加上__,在python中如果实例的变量名以__开头,就变成一个私有变量(private)
只有内部可以访问,外部不能访问'''


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    '''如果外部想访问name和score怎么办,为了防止不让外界修改内部数据'''

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    '''特殊条件下需要修改怎么办,原先也可以修改为什么要大费周折进行这样写,因为有时候在参数设置的时候可以进行参数检查'''

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if (0 <= score <= 100):
            self.__score = score
        else:
            print('please enter the correct score!')


'''1.变量名字 __XX__,是特殊变量是可以直接访问的,不是private
   2._x,这样的变量是可以被外界访问的,但是按着约定成俗的规定,请你把我认为是private
   3.在有时候 __x 可用通过 _Student__name,但是强烈建议不这么做.
   总结:python本身没有任何机制防止你干坏事,一些靠自觉
   
    bart.__name='new NAME'
    print(bart.__name)
    这种写法是错误的,是外部代码给bart变量新增了一个__name 属性
    bart.get_name()'''

# 继承和多态
'''在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
   而被继承的class称为基类、父类或超类（Base class、Super class)
   继承最大的好处是:子类能够获取父类的全部功能,由于父类拥有了run方法,子类什么也不干也拥有了run的方法
   继承的第二个好处 多态: 当子类和父类都存在相同的run()方法时,子类的run()覆盖了父类的run(),在代码运行时候会调用子类run()方法
  '''


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is runing')


class Cat(Animal):
    pass


''' 多态:当我们定义一个class时,我们实际上定义了一种数据类型,它和python自带的数据类型{str,list,dict}没什么区别
    a = list() # a是list类型
    b = Animal() # b是Animal类型
    c = Dog() # c是Dog类型
    >>> isinstance(a, list)
    True
    >>> isinstance(b, Animal)
    True
    >>> isinstance(c, Dog)
    True
    >>> isinstance(c, Animal)
    True
    >>> isinstance(b, Dog)
    False
    在继承关系中,如果一个实例的数据类型是某个子类,那他的数据类型可以被看成是父类,但反过来不行'''


def run_twice(animal):
    animal.run()
    animal.run()
    '''若新增一个Animal 子类,不必对 run_twice()做任何修改,任何依赖Animal作为参数的函数或者方法都可以正常运行,这是多态的功劳
    多态中的开闭原则:
    对扩展开放:允许新增Animal子类
    对修改封闭:不需要修改Animal类型的run_twice()函数'''

    '''静态语言vs动态语言 :
    这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
    Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
    但是，许多对象，只要有read()方法，都被视为“file-like object“。
    许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象'''

    '''小结:
    
    继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
    动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。'''


def duo_tai():
    run_twice(Animal())
    run_twice(Dog())

    '''获取对象的信息:
    当我们拿到一个对象的运用时,如果要判断这个对象是什么数据类型,有哪些方法
    如果判断一个对象是否是函数,可以用types模块中定义的常量:'''


import types


def ttype():
    print(type(123))
    print(type(abs))
    print(type(123) == int)
    type(abs) == types.BuiltinFunctionType
    type(lambda x: x) == types.LambdaType
    type((x for x in range(10)) == types.GeneratorType)


'''要判断class类型 用 ininstance() 函数'''


def issstance():
    # 用来判断是否是list 或者是tuple
    isinstance([1, 2, 3], (list, tuple))
    isinstance((1, 2, 3), (list, tuple))


'''要获得一个对象的所有属性和方法,可以用dir()
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
    >>> len('ABC')
    3
    >>> 'ABC'.__len__()
    3
我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
    >>> class MyDog(object):
    ...     def __len__(self):
    ...         return 100
    ...
    >>> dog = MyDog()
    >>> len(dog)
    100
仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
    >>> class MyObject(object):
    ...     def __init__(self):
    ...         self.x = 9
    ...     def power(self):
    ...         return self.x * self.x
    ...
    >>> obj = MyObject()
紧接着可以测试对象的属性;
    >>> hasattr(obj, 'x') # 有属性'x'吗？
    True
    >>> obj.x
    9
    >>> hasattr(obj, 'y') # 有属性'y'吗？
    False
    >>> setattr(obj, 'y', 19) # 设置一个属性'y'
    >>> hasattr(obj, 'y') # 有属性'y'吗？
    True
    >>> getattr(obj, 'y') # 获取属性'y'
    19
    >>> obj.y # 获取属性'y'
    19
如果试图获取不存在的属性，会抛出AttributeError的错误：
    >>> getattr(obj, 'z') # 获取属性'z'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'MyObject' object has no attribute 'z'
也可以获得对象的方法：    
    >>> hasattr(obj, 'power') # 有属性'power'吗？
    True
    >>> getattr(obj, 'power') # 获取属性'power'
    <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
    >>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
    >>> fn # fn指向obj.power
    <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
    >>> fn() # 调用fn()与调用obj.power()是一样的
    81
'''

'''小结:
   通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息
   https://www.liaoxuefeng.com/wiki/1016959663602400/1017499532944768'''


def dirr():
    print(dir('ABD'))


'''实例属性和类属性'''
'''给实例绑定属性的方法是通过实例变量或者通过self变量'''


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# s = Student('bob')
# s.score = 90


'''给类本身绑定一个属性则可以直接在class中定义属性,这种属性属于类属性'''
# class Student(object):
#     name = 'Student'
'''当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：
    >>> class Student(object):
    ...     name = 'Student'
    ...
    >>> s = Student() # 创建实例s
    >>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
    Student
    >>> print(Student.name) # 打印类的name属性
    Student
    >>> s.name = 'Michael' # 给实例绑定name属性
    >>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
    Michael
    >>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
    Student
    >>> del s.name # 如果删除实例的name属性
    >>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
    Student
从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。'''

if __name__ == '__main__':
    if Student.count != 0:
        print('test error')
    else:
        bart = Student('Bart')
        if Student.count != 1:
            print('1 test error')

#     dirr()

# dog = Dog()
# dog.run()
