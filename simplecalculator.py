num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))
operator = input("which operation do you want to perform:")
if operator == "addition":
  print(f"sum of two numbers:{num1 + num2}")
elif operator == "subtraction":
  print(f"difference of two numbers:{num1 - num2}")
elif operator == "multiplication":
  print(f"product of two numbers:{num1*num2}")
elif operator == "division":
  if num2 != 0:
    print(f"division of two numbers:{num1/num2}")
  else:
    print("DIVISION NOT POSSIBLE")
elif operator == "exponent":
  print(f"power is:{num1**num2}")
else:
  print("error!!!, THIS OPERATION CANNOT PERFORM")
