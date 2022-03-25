class Calu:
    num=110
    #default constructor

    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        print("I am automatically created_f")

    def getData(self):
        print("I am executing method in class")

    def summation(self):
        return self.firstnumber + self.secondnumber + self.num


obj = Calu(2,2)
obj.getData()
print(obj.summation())

obj2 = Calu(3,3)
print(obj2.summation())
