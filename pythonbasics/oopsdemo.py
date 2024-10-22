#Class

class Calculator:
    num =100       #class variable

    #default constructor
    def __init__(self,a,b):
        self.firstnumber=a
        self.secondnumber=b
        print("I am called automatically when object created")

    def getdata(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstnumber + self.secondnumber + self.num


obj = Calculator(2,3)      #syntax to create object
obj.getdata()
print(obj.num)
print(obj.summation())

obj1 = Calculator(4,5)
print(obj1.summation())
