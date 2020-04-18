#Accept string from a user and display only those characters which are present at an even index number.


enter_string = input("Enter a string: ")
enter_string_len = len(enter_string)

for x in range(0, enter_string_len, 2):
    print("Index[ ", str(x), " ]", " ", enter_string[x])
