#Test system
class CourseTest(object):
    def __init__(self,date,day,marks):
        self.date=date
        self.day=day
        self.marks=marks


class BEL(CourseTest):
    def bel(self):
           #CourseTest.Tests(self)
        print('Date =',self.date,'==','Day =',self.day,'==','Marks =',self.marks)
            
class AP(CourseTest):
    def ap(self):
        print('Date =',self.date,'==','Day =',self.day,'==','Marks =',self.marks)

class DS(CourseTest):
    def ds(self):
        print('Date =',self.date,'==','Day =',self.day,'==','Marks =',self.marks)
        
