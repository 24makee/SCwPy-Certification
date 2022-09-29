def arithmetic_arranger(problems, showAnswer=False):
  
  if showAnswer == True:
      answers=[]
  if len(problems)>5:
    return "Error: Too many problems."

  problems_string = "".join(problem for problem in problems).replace(" ","")
  accepted = "0123456789+-"
  if any(ch in "/*" for ch in problems_string):
    return "Error: Operator must be \'+\' or \'-\'." 

  if not all(char in accepted for char in problems_string):
    return "Error: Numbers must only contain digits." 

  first_ops,operations,second_ops=[],[],[]
  for problem in problems:
    terms = problem.split()
    if len(terms[0])>4 or len(terms[2])>4:
      return "Error: Numbers cannot be more than four digits."
    first_ops.append(terms[0])
    operations.append(terms[1])
    second_ops.append(terms[2])

    if 'answers' in locals():
      answers.append(str(eval(problem)))

  arranged_problems=""
  for t1,t2 in zip(first_ops,second_ops):
    arranged_problems += (max(len(t1),len(t2)) + 2 - len(t1))*" " + t1 + 4*" "
  arranged_problems = arranged_problems[:-4] + "\n"
  for t1,op,t2 in zip(first_ops,operations,second_ops):
    arranged_problems += op + (max(len(t1),len(t2)) + 1 - len(t2))*" " + t2 + 4*" "
  arranged_problems = arranged_problems[:-4] + "\n"
  for t1,t2 in zip(first_ops,second_ops):
    arranged_problems += (max(len(t1),len(t2)) + 2) *"-" + 4*" "
  arranged_problems = arranged_problems[:len(arranged_problems)-4]

  if showAnswer==True:
    arranged_problems = arranged_problems + "\n"
    for t1,t2,ans in zip(first_ops,second_ops,answers):
      arranged_problems += (max(len(t1),len(t2)) + 2 - len(ans))*" " + ans + 4*" "
    arranged_problems = arranged_problems[:len(arranged_problems)-4]

  return arranged_problems
