first_list = [10, 20, 23, 11, 17]
second_list = [13, 43, 24, 36, 12]
new_list = []
for x in first_list:
    if (x % 2) != 0:
        new_list.append(x) #inspired by pynative solution
for y in second_list:
    if (y % 2) == 0:
        new_list.append(y)

print(new_list)









