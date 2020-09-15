class Counter(object): 
    number = 0 
 
    def __init__(self): 
        self.number += 1 
 
    def __del__(self): 
        self.number -= 1

class Account(Counter): 
    def __init__(self,name,current_tension,next_tension): 
        Counter.__init__(self)
