



def denaryToRoman(denary):
  roman = ""

  if denary == 50:
    roman += "L"
    denary -= 50

  if denary == 41:
        roman += "XLI"
        denary -= 41

  elif denary == 42:
        roman += "XLII"
        denary -= 42

  elif denary == 43:
        roman += "XLIII"
        denary -= 43

  elif denary == 44:
        roman += "XLIV"
        denary -= 44

  elif denary == 45:
        roman += "XLV"
        denary -= 45

  elif denary == 46:
        roman += "XLVI"
        denary -= 46

  elif denary == 47:
        roman += "XLVII"
        denary -= 47

  elif denary == 48:
        roman += "XLVIII"
        denary -= 48

  elif denary == 49:
        roman += "XLIX"
        denary -= 49



  if denary == 40:
      roman += "XL"
      denary -= 40

  while denary >= 10:
    roman += "X"
    denary -= 10
    
  if denary == 15:
    roman += "XV"
    denary -= 15

  if denary == 9:
    roman += "IX"
    denary -= 9

  if denary >= 5:
    roman += "V"
    denary -= 5

  if denary == 4:
    roman += "IV"
    denary -= 4

  while denary > 0:
    roman += "I"
    denary -= 1

 



  return roman

def asserting( actual, expected, message): 
  if actual == expected:
    print("succeded")
  else:
    print(message)


def check(asserting):
  
  asserting(denaryToRoman(1), "I", "1 did not work")
  asserting(denaryToRoman(2), "II", "2 did not work")
  asserting(denaryToRoman(3), "III", "3 did not work")
  asserting(denaryToRoman(4), "IV", "4 did not work")
  asserting(denaryToRoman(5), "V", "5 did not work")
  asserting(denaryToRoman(6), "VI", "6 did not work")
  asserting(denaryToRoman(7), "VII", "7 did not work")
  asserting(denaryToRoman(8), "VIII", "8 did not work")
  asserting(denaryToRoman(9), "IX", "9 did not work")
  asserting(denaryToRoman(10), "X", "10 did not work")

  asserting(denaryToRoman(11), "XI", "11 did not work")
  asserting(denaryToRoman(12), "XII", "12 did not work")
  asserting(denaryToRoman(13), "XIII", "13 did not work")
  asserting(denaryToRoman(14), "XIV", "14 did not work")
  asserting(denaryToRoman(15), "XV", "15 did not work")
  asserting(denaryToRoman(16), "XVI", "16 did not work")
  asserting(denaryToRoman(17), "XVII", "17 did not work")
  asserting(denaryToRoman(20), "XX", "20 did not work")

  asserting(denaryToRoman(21), "XXI", "21 did not work")
  asserting(denaryToRoman(22), "XXII", "22 did not work")
  asserting(denaryToRoman(23), "XXIII", "23 did not work")
  asserting(denaryToRoman(24), "XXIV", "24 did not work")
  asserting(denaryToRoman(25), "XXV", "25 did not work")
  asserting(denaryToRoman(26), "XXVI", "26 did not work")
  asserting(denaryToRoman(27), "XXVII", "27 did not work")
  asserting(denaryToRoman(28), "XXVIII", "28 did not work")
  asserting(denaryToRoman(29), "XXIX", "29 did not work")
  asserting(denaryToRoman(30), "XXX", "30 did not work")

  asserting(denaryToRoman(31), "XXXI", "31 did not work")
  asserting(denaryToRoman(32), "XXXII", "32 did not work")
  asserting(denaryToRoman(33), "XXXIII", "33 did not work")
  asserting(denaryToRoman(34), "XXXIV", "34 did not work")
  asserting(denaryToRoman(35), "XXXV", "35 did not work")
  asserting(denaryToRoman(36), "XXXVI", "36 did not work")
  asserting(denaryToRoman(37), "XXXVII", "37 did not work")
  asserting(denaryToRoman(38), "XXXVIII", "38 did not work")
  asserting(denaryToRoman(39), "XXXIX", "39 did not work")
  asserting(denaryToRoman(40), "XL", "40 did not work")

  asserting(denaryToRoman(41), "XLI", "41 did not work")
  asserting(denaryToRoman(42), "XLII", "42 did not work")
  asserting(denaryToRoman(43), "XLIII", "43 did not work")
  asserting(denaryToRoman(44), "XLIV", "44 did not work")
  asserting(denaryToRoman(45), "XLV", "45 did not work")
  asserting(denaryToRoman(46), "XLVI", "46 did not work")
  asserting(denaryToRoman(47), "XLVII", "47 did not work")
  asserting(denaryToRoman(48), "XLVIII", "48 did not work")
  asserting(denaryToRoman(49), "XLIX", "49 did not work")
  asserting(denaryToRoman(50), "L", "50 did not work")


ask = str(input("Input"))
if input == "check":
  check()

else:
  denary = ask
  denaryToRoman() 
    


