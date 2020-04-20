#Reverse a given number and return true if it is the same as the original number

var1 = "121"
rev_var1 = var1[::-1]
var2 = "123"
rev_var2 = var2[::-2]
check_item = True

if var1 == rev_var1:
    check_item = True
else:
    check_item = False

print("Original number: ", var1)
if check_item == True:
    print("The original and reverse number is the same:", check_item)
else:
    print("The original and reverse number is the same:", check_item)
print("Original number: ", var2)
if var2 == rev_var2:
    check_item = True
else:
    check_item = False

if check_item == True:
    print("The original and reverse number is the same:", check_item)
else:
    print("The original and reverse number is the same:", check_item)
