Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

list_a = [10, 20, 33, 46, 55]

def division_by_five(list_1):
    for x in list_1:
        if x % 5 == 0:
            print(x)

print("Given list is", list_a)
print("Divisible of 5 in a list ")
division_by_five(list_a)
