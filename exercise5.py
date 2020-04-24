Given a list of numbers, return True if first and last number of a list is same

list_a = [10, 20, 30, 40, 10]
list_b = [10, 20, 30, 40, 50]
def checklist(first):
    if first[0] == first[-1]:
        print("Result is", True)
    else:
        print("Result is", False)

print("Given list is ", list_a)
checklist(list_a)
print("Given list is ", list_b)
checklist(list_b)
