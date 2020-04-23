#Given a range of first 10 numbers, Iterate from start number to the end number 
#and print the sum of the current number and previous number

def myfunc():
  for x in range(1, 10, 1):
    current_num = x
    previous_num = 0 + x - 1
    summary = current_num + previous_num
    print("Current number:", current_num, "Previous num: ", previous_num, "Sum: ", summary)

myfunc()
