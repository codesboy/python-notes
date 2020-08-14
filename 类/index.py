aa = 145

class Person():
    num = 0 #类变量
    def __init__(self,name,age): #构造函数 实例化的时候会自动调用该函数，一般用于初始化实例变量
        self.name = name #定义实例变量和赋值，如果实例变量没有定义的话，在实例化后访问实例变量时会去找相关的类变量，类变量没找到会去父类里面找
        self.age = age

    def say(self): #定义实例方法
        #self指的是对象实例而不是类，self在定义方法的时候不能省略
        # print(self) 
        print('我叫'+self.name+',我今年'+str(self.age))  #在方法里访问实例变量
        
        print('类变量：' + str(self.__class__.num)) #访问类变量 或者print('类变量：' + str(Person.num))


print(Person)
p1 = Person('rehack',18) #实例化

p1.say()
print(p1.name) #访问实例变量
print(Person.num) #访问类变量

print(p1.__dict__) #所有的实例变量
print(Person.__dict__) #所有的类变量和方法