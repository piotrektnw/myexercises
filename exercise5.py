Given a list of numbers, return True if first and last number of a list is same

list1 = [10, 20, 30, 40, 10]
list2 = [10, 20, 30, 40, 50]

list_1_len = (len(list1))
list_2_len = (len(list2))

print("Given list is ", list1)
if list1[0] == list1[list_1_len - 1]:
    print("result is True")
else:
    print("Result is False")

print("Given list is ", list2)
if list2[0] == list2[list_2_len - 1]:
    print("result is True")
else:
    print("Result is False")
