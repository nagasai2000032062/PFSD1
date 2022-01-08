class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        print("area=",3.14*self.r*self.r)
class rectangle(circle):
    def __init__(self,r,l,b):
        super().__init__(r)
        self.l=l
        self.b=b
    def area(self):
        super().area()
        print("area=",self.l*self.b)
ob=rectangle(3,4,5)
ob.area()