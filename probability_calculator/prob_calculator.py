import copy
import random

class Hat:

  def __init__(self,**kwargs):
    self.contents=[]
    for color, number in kwargs.items():
      for i in range(number):
        self.contents.append(str(color))

  def draw(self,balls_to_draw):
    if balls_to_draw>=len(self.contents):
      return self.contents
    else:
      self.drawn = []
      for i in range(0,balls_to_draw):
        self.drawn.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
      return self.drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  if num_balls_drawn>=len(hat.contents):
    return 1
  got_expected = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn = hat_copy.draw(num_balls_drawn)
    got_balls = sum([1 for color,number in expected_balls.items() if drawn.count(color)>=number])
    got_expected+=1 if got_balls==len(expected_balls) else 0
  
  return got_expected/num_experiments
