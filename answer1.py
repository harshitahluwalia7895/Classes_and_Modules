import math as m
class Circle:
        def __init__(self,r):
            self.radius=r
        def getArea(self):
            return m.pi*((self.radius)**2)
        def getCircumference(self):
            return 2*(m.pi)*self.radius
r=float(input("Enter radius of circle: "))
c1=Circle(r)
print("Radius={} Area={} Circumference={}".format(c1.radius,c1.getArea(),c1.getCircumference()))
