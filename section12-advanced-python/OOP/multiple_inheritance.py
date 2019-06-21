class ClassA:
    def hi(self):
        print("Hello")


class ClassB:
    def hi(self):
        print('Hell yo!')

"""Multiple inheritance uses properties from the super classes in order. 
If property is not available in the first super class, then it moves into the second, and so on
until it finds a the property or it doesnt and throws error"""
class ClassC(ClassA, ClassB):
    pass


c = ClassC()
c.hi()


class ClassC(ClassB, ClassA):
    pass


c = ClassC()
c.hi()
