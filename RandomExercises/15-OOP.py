
class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Creates a new point at the origin """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute the distance from the origin """
        return ((self.x **2) + (self.y **2)) ** 0.5
        
    def halfway(self, target):
        """ Return the midpoint of points p1 and p2 """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx,my)

    def reflect_x(self):
        mx = self.x * -1
        return Point(mx,self.y)

    def slope_from_origin(self):
        p = Point()
        q = (p.y - self.y) / (p.x - self.x)
        return q

    def __str__(self):
        return f'{self.x}, {self.y}'


p = Point(3,4)
q = Point(5,12)
r = p.reflect_x()
print(Point(4, 10).slope_from_origin())

