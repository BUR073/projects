with open("grades.txt", "r") as a_file:
  for line in a_file:
    grade_convert = int(line.strip())
    
    if grade_convert > 90:
        grade = 'A'

    elif grade_convert > 70:
        grade = 'B'

    elif grade_convert > 50:
        grade = 'C'

    elif grade_convert > 30:
        grade = 'D'

    else:
         grade = 'E' 

    
    print(grade)
