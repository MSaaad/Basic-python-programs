class operations:
    def __init__(self):
        self.value1=10
        self.value2=3
        option=input('Enter option:')
        if option=='add':
            Add.add(self)
        elif option=='sub':
            Sub.sub(self)

class Add(operations):
    def add(self):
        plus=self.value1+self.value2
        print(plus)
class Sub(operations):
    def sub(self):
       minus=self.value1-self.value2
       print(minus)
