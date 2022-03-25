#self keyword is mandatory for calling variable name into method
#instance variable and class variable have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object

class Calculator:
    num=100 # class variable

    def __init__(self,a, b):

        self.fn = a;
        self.sn = b;

        print("default constructor is called automatically")

    def getData(self):
        print("Sample Class Programme")

    def Summation(self):

        return self.fn + self.sn + self.num

Obj = Calculator(2,3)
Obj.getData()
print(Obj.Summation())

Obj = Calculator(4,5)
Obj.getData()
print(Obj.Summation())