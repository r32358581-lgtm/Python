class Student:
        def__init__(self, name=None, age=0):
                self.__name = name
                self.__age = age
        
        def getage(self):
                return self.__age
        
        def getName(self):
                return self.__qualname__
        
        def setAge(self, age):
                self.__age=age

        def setName(self, name):
                self.__name=name

obj=Student("Hong", 20)
obj.getName()