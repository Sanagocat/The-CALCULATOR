condition = True

while(condition == True):
  print("Calculator + - * / ^")
  number1=int(input(" number 1:"))
  number2=int(input(" number 2:"))
  operator=input(" operator? (+ - * / ^):")
  
  if (operator=="+") :
    plus = number1 + number2
    print("Plus is " + str(plus))
  elif(operator=="-") :
    minus = number1 - number2
    print("minus is " + str(minus))
  elif(operator=="*") :
    multiply = number1 * number2
    print("product is " + str(multiply))
  elif(operator=="/") :
    if(number2==0) :
      print("anwser is infinity")
    else: 
      divide = number1 / number2
      print("quotient is " + str(divide))
  elif(operator=="^") :
    square = pow(number1, number2)
    print("square is " + str(square))
  else:
    print("[ERROR] Not an operator. Try again!!")

  user_answer = input("Press [N] to quit, Any key to continue.")
  if ( user_answer=="N" or  user_answer=="n"):
    condition=False
  else:
    condition=True

#if number1 and number2 
#"** Plus ** is ***"
#terry







