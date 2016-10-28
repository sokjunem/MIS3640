# oop = object oriented project
class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """
    def __str__(self):
        return 'This point is ({},{})'.format(self.x, self.y) 

my_point = Point()
# print(my_point)
my_point.x = 3       # x and y is attributes of the Point 
my_point.y = 4

new_point = Point()
new_point.x = 100
new_point.y = 50
print(new_point)


def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))

# print_point(my_point)
Alex_point = Point()
Alex_point.x = 5
Alex_point.y = 7
# print_point(Alex_point)


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.
    p1: Point
    p2: Point
    returns: float
    """
    import math
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p2.y)**2)

d = distance_between_points(my_point, Alex_point)
print(d)

class Rectangle:
    """Represents a rectangle. 
    attributes: width, height, corner.
    """

SJ_rect = Rectangle()
SJ_rect.width = 10
SJ_rect.height = 20
SJ_rect.corner = Point()
SJ_rect.corner.x = 3
SJ_rect.corner.y = 4
# print_point(SJ_rect.corner)
# print_point(my_point)
# print(SJ_rect.corner == my_point)
# print(SJ_rect.corner is my_point)

def find_center(rect):
    """Returns a Point at the center of a Rectangle.
    rect: Rectangle
    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p

# print_point(find_center(SJ_rect))


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.
    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight

grow_rectangle(SJ_rect, -4, -10)
# print(SJ_rect.width, SJ_rect.height)

def print_rectangle(rect):
    print('The width of the rectangle is ', rect.width,'.')
    print('The height of the rectangle is ', rect.height,'.')
    print('The lower-left corner is ')
    print_point(rect.corner)

print_rectangle(SJ_rect)
grow_rectangle(SJ_rect, -4, -10)
print_rectangle(SJ_rect)

def main():
    my_point = Point()
    my_point.x = 3
    my_point.y = 4
    print('My point', end=' ')
    print_point(my_point)

    print('Is my_point an instance of Point?', isinstance(my_point, Point))
    print('Is my_point an instance of Rectangle?', isinstance(my_point, Rectangle))
    print('Does my_point have an attribute x?', hasattr(my_point, 'x')) # in (x,y) does x has y as an attribute
    print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print('Does bos have an attribute x?', hasattr(box,'x')) # False because x is under the corner. Not directly under the box
    print('Does box have an attribute conrner?', hasattr(box,'corner'))
    # dir() = directory. Shows what attributes are under it.
    print(dir(box))

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)


# if __name__ == '__main__':
#     main()
print(dir(my_point))