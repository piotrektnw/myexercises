#Given a range of first 10 numbers, Iterate from start number to the end number 
#and print the sum of the current number and previous number

x = range(10)
curr = "Current number: "
prev = " Previous number: "
sum = " Sum: "

print("Printing current and previous number sum in a given range(10)")
print("Current Number: 0 Previous Number: 0 Sum: 0")
for x in range(1, 10, 1):
    print(curr + str(x) + prev + str(x - 1) + sum + str(x + (x - 1)))
