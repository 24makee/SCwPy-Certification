import math
class Rectangle:

  def __init__(self,width,height):
    self.width=width
    self.height=height

  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)

  def set_width(self,width):
    self.width = width
    
  def set_height(self,height):
    self.height = height
    
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * (self.width + self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height **2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    return "".join((self.width*"*" + "\n")*self.height)

  def get_amount_inside(self,shape):
    return math.floor(self.width/shape.width) * math.floor(self.height/shape.height)


class Square(Rectangle):

  def __init__(self,side):
    self.width=self.height=side

  def __str__(self):
    return "Square(side={})".format(self.width)

  def set_side(self,side):
    self.width=self.height=side
