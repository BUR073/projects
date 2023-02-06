def digitSum(n):
  x = 0
  reversedNo = 0
  
  for i in n:
    number = n[x]
    
    reversedNo += number 
    x += 1 
  
  if reversedNo == 0:
    print("Value's can't be 0")

  else:
    print("n :", reversedNo)
    
digitSum((3, 4, 5))
digitSum((9, 9, 9))
digitSum((0, 0, 0))
digitSum((3, 4, 5, 7, 9, 4, 5, 6))
 
