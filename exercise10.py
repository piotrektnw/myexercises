 #Given a two list of numbers create a new list 
 #such that new list should contain only odd numbers from the first list and even numbers from the second list

def odd_even(first_l, second_l):
    print("First list is", first_l)
    print("Second list is", second_l)
    new_l = []
    for x in first_l:
        if (x % 2) != 0:
         new_l.append(x)
    for y in second_l:
        if (y % 2) == 0:
         new_l.append(y)
    print("Mixed lists are: ", new_l)

first_l = [10, 20, 23, 11, 17]
second_l = [13, 43, 24, 36, 12]
new_l = []
odd_even(first_l, second_l)









