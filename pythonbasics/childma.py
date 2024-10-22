from oopsdemo import Calculator


class Childimp(Calculator):
    num2=200

    def __init__(self):
        Calculator.__init__(self,2,10)       #giving the parent class's parameter in the child class

    def getcompletedata(self):
        return self.num2 + self.num + self.summation()

obj = Childimp()
print(obj.getcompletedata())