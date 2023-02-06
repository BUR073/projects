#Write a function swapNeighbours(s) that takes a list parameter containing an even number of elements and returns a string where adjacent characters are swapped. Thus, swapNeighbours(['a', 1, 'b', 2, 'c', 3]) would return [1, 'a', 2, 'b', 3, 'c']. Your function should report an error if the parameter length is odd.

def swapNeighbours(s):
  reversedList = []
  if (len(s) % 2) != 0:
    print("Must be an even number of values in the list")

  x = len(s) - 1
  for i in s:
      newValue = s[x]
      x -= 1
      reversedList.append(newValue)

  print(s, ':', reversedList)
      








swapNeighbours(['a', 1, 'b', 2, 'c', 3])
swapNeighbours(['e', 2, 'c', 3, 'n', 38])
swapNeighbours(['g', 3, 'f', 2, 'a', 3])
swapNeighbours(['w', 4, 'h', 1, 'u'])
swapNeighbours(['a', 1, 'b', 2, 'c', 3, 'e', 3, 't', 5])


