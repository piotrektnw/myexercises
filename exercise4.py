
counter = 0
while counter < 10:
    enter_string = input("Enter a string: ")
    n = input("Enter a number: ")
    if int(n) > len(enter_string):
        print("Too long. It must be less than: ", len(enter_string))
        counter += 1
    else:
        print(enter_string[4:])








