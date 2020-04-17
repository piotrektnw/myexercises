#mysolution
num1 = ("Number: ")
num2 = ("Number2 :")
counter = 0

while counter < 99:
    num1 = input("Type digit: ")
    num2 = input("Type digit2: ")

    if num1.isdigit() and num2.isdigit() is True:
        break
    else:
        print("Only digits please.")
        counter += 1


product = int(num1) * int(num2)

if product > 1000:
    print(int(num1) + int(num2))
else:
    print("Ok")
