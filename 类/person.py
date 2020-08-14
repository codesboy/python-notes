aa = 145

class Person():
    num = 0 #类变量
    def __init__(self,name,age): #构造函数 实例化的时候会自动调用该函数，一般用于初始化实例变量
        self.name = name #定义实例变量和赋值，如果实例变量没有定义的话，在实例化后访问实例变量时会去找相关的类变量，类变量没找到会去父类里面找
        self.age = age
        self.__score = 0 #定义一个私有变量，在类外部不能访问和修改

    def say(self): #定义实例方法
        #self指的是对象实例而不是类，self在定义方法的时候不能省略
        # print(self) 
        print('我叫'+self.name+',我今年'+str(self.age))  #在方法里访问实例变量
        
        print('类变量：' + str(self.__class__.num)) #访问类变量 或者print('类变量：' + str(Person.num))

    @classmethod 
    def count(cls): #加上@classmethod装饰器来定义类方法 cls参数是必须的，命名可以自定，类方法不能访问实例变量
        cls.num += 1 #操作类变量
        print(cls.num)
    
    @staticmethod
    def add(): #加上@staticmethod装饰器来定义静态方法，静态方法不能访问实例变量，静态方法一般都可以用类方法来代替使用，用的比较少
        print('static method')
        # Person.num 访问类变量

    def __foo(): #定义一个私有方法，在类的外部不能访问和
        pass



print(Person)
p1 = Person('rehack',18) #实例化

p1.say()
print(p1.name) #访问实例变量
print(Person.num) #访问类变量

print(p1.__dict__) #所有的实例变量
print(Person.__dict__) #所有的类变量和方法

Person.count() #调用类方法 实例对象也可以调用类方法，但不建议这样使用

p1.add() #通过类本身或者实例对象都可以调用静态方法

# print(p1.__score) #访问私有变量会报错
print(p1._Person__score) #强制访问私有变量