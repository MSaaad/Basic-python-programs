class Calculation:
    def __init__(self):
        choice=int(input('Enter your choice:'))
        if choice==1:
            Min.min(self)
        elif choice==2:
            Hours.hour(self)

class Min(Calculation):
    def min(self):
        self.seconds=int(input('Enter data in seconds:'))
        minutes=self.seconds/60
        print(minutes,'mins')
class Hours(Calculation):
    def hour(self):
        self.seconds=int(input('Enter data in seconds:'))
        hours=(self.seconds/(60*60))
        print(hours,'hrs')
    
