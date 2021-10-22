
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

    def get_line_to(self, target):
        slope = (target.y - self.y) // (target.x - self.x)
        y_int = self.y - (slope * self.x)
        final = (slope,y_int)
        return final

    def midpoint_of_circle_four_coords(self, target1, target2, target3):
        slope_of_first_pair = (target1.y - self.y) // (target1.x - self.x)
        slope_of_second_pair = (target3.y - target2.y) // (target3.x - target2.x)
        
        mx = (self.x + target1.x)/2
        my = (self.y + target1.y)/2
        midpoint_first_pair = Point(mx,my)
        perpendicular_of_first_slope = slope_of_first_pair * -1
        # y_int_of_perpendicular = self.y - (perpendicular_of_first_slope * self.x)
        y_int_of_perpendicular = midpoint_first_pair.y - (perpendicular_of_first_slope * midpoint_first_pair.x)
        final = (perpendicular_of_first_slope,y_int_of_perpendicular) 

        mx1 = (target2.x + target3.x)/2
        my1 = (target2.y + target3.y)/2
        midpoint_second_pair = Point(mx1,my1)
        perpendicular_of_second_slope = slope_of_second_pair * -1
        # y_int_of_perpendicular1 = target2.y - (perpendicular_of_second_slope * target2.x)
        y_int_of_perpendicular1 = midpoint_second_pair.y - (perpendicular_of_second_slope * midpoint_second_pair.x)
        final1 = (perpendicular_of_second_slope, y_int_of_perpendicular1)

        final3 = ((perpendicular_of_first_slope * perpendicular_of_second_slope), y_int_of_perpendicular)
        ################### work in progress ##########################################
        # return final3

    def __str__(self):
        return f'{self.x}, {self.y}'


p = Point(-7,7)
q = Point(1,9)
r = Point(3,1)
s = Point(-7,1)

print(p.midpoint_of_circle_four_coords(q,r,s))

