class Drawing:
    def __init__(self):
        self.sides=int(input('Enter the sides:'))
        if self.sides==2:
            Triangle.triangle(self)
        else:
            Rectangle.rectangle(self)
         
class Triangle(Drawing):
    def triangle(self):
        self.side1=int(input('side1:'))
        self.side2=int(input('side2:'))
        tri_area=((self.side1+self.side2)/2)
        print(tri_area)

class Rectangle(Drawing):
    def rectangle(self):
        self.side1=int(input('side1:'))
        self.side2=int(input('side2:'))
        self.side3=int(input('side3:'))    
        rec_area=((self.side1+self.side2+self.side3))
        print(rec_area)
