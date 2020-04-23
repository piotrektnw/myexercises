def first_last():
  sum = first_num + second_num
  multiplication = first_num * second_num
  if multiplication > 1000:
    print("The result is ", sum)
  else:
    print("The result is ", multiplication)

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

first_last()
