import string
import random
x = 1
letters = []

while x < 500000:
    string.ascii_letters = ' a b c d e f g h i j k l m n o p q r s t u v w x y z'

    letters.append(random.choice(string.ascii_letters))
 
    x = x + 1

print(''.join(letters))
