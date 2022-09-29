import math

class Category:

  def __init__(self,category):
    self.category = category
    self.ledger = []
    self.budget = 0
    self.withdrawal = 0

  def __str__(self):
    self.output = self.category.center(30, "*") + "\n"
    for transaction in self.ledger:
      self.output+=transaction['description'].ljust(23)[:23] + "{:.2f}".format(transaction['amount']).rjust(7)+"\n"
    self.output+="Total: {:.2f}".format(self.budget)
    return self.output

  def check_funds(self,amount):
    return True if self.budget>=amount else False

  def deposit(self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.budget += amount

  def withdraw(self,amount,description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.budget-=amount
      self.withdrawal+=amount
      return True
    else:
      return False

  def get_balance(self):
    return self.budget

  def transfer(self,amount,other_category):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": "Transfer to {}".format(other_category.category)})
      self.budget-=amount
      self.withdrawal+=amount
      
      other_category.ledger.append({"amount": amount, "description": "Transfer from {}".format(self.category)})
      other_category.budget+=amount
      return True
    else:
      return False

  
def create_spend_chart(categories):

  output_string = "Percentage spent by category\n"
  category_percentage = []
  total_withdrawal = sum(category.withdrawal for category in categories)
  for category in categories:
    category_percentage.append(
      tuple([
      category.category,
      math.floor(((category.withdrawal*100)/total_withdrawal)/10)*10
      ]))
  for i in range(100,-1,-10):
    output_string+=str(i).rjust(3) + "|"
    for elem in category_percentage:
      if elem[1]>=i:
        output_string+=" o "
      else:
        output_string+=3*" "
    output_string+=" \n"

  output_string+=4*" " + (3*len(category_percentage)+1)*"-" +"\n"
  max_category_len = max(len(category.category) for category in categories)
  for i in range(0,max_category_len):
    output_string+=4*" "
    for elem in category_percentage:
      try:
        output_string+=" {} ".format(elem[0][i])
      except:
        output_string+=3*" "
    
    output_string+=" \n"

  return output_string[:-1]
