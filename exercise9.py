#Reverse a given number and return true if it is the same as the original number

def reversecheck(num):
    original_num = num
    print("Original number is: ", original_num)
    rev_num = num[::-1]
    if num == rev_num:
        score = True
    else:
        score = False
    print("The original and reverse num is the same:", score)
    
reversecheck("121")
reversecheck("221")
