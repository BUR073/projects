## Reverse String

string = str(input("Input: "))

reversed = []

def string_reverse():
  for i in range(len(string)-1, 0-1, -1):
    add = (string[i])
    reversed.append(add)

  str1 = ''.join(reversed)

  print(str1)

string_reverse()
