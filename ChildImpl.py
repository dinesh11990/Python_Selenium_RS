from Class import Calu


class ChildImpl(Calu):
    num2 = 200

    def __init__(self):
        Calu.__init__(self,1,1)

    def getCompleteData(self):
        return self.num + self.summation() + self.num2

final = ChildImpl()

print(final.getCompleteData())
