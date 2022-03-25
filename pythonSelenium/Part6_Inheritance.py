from pythonSelenium.Part5_Contructor import Calculator


class ChildImpl(Calculator):

    num2=200

#you need to call the parent constructor here
    def __init__(self):
        Calculator.__init__(self, 2, 5)


    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj = ChildImpl()
print(obj.getCompleteData())
