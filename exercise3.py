def even_num():
  enter = input("Enter string: ")
  enter_len = len(enter)
  print("Original string is: ", enter)
  print("Printiny only even index chars")
  for x in range(0, enter_len, 2):
    print("Index[ ", str(x), " ]", " ", enter[x])

even_num()
