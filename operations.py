class operation:
    def __init__(self):
        self.value1=int(input('First value'))
        self.value2=int(input('Second value'))
        self.operations=input('Operation:')
        if self.operations=='add':
            Add.add(self)
        elif self.operations=='sub':    
            Sub.sub(self)
        elif self.operations=='mul':
            Mul.mul(self)
class Add(operation):
    def add(self):
        print(self.value1+self.value2)
class Sub(operation):
    def sub(self):
        print(self.value1-self.value2)
class Mul(operation):
    def mul(self):
        print(self.value1*self.value2)
        
        
            
