#Given a string and an integer number n, remove characters from a 
#string starting from zero up to n and return a new string

def removeChars(txt, n):

  if n > len(txt):
    print("Too long")
  else:
    print(txt[n:])

removeChars("pynative", 4) 







