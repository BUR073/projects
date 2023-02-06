Pound = int(input("Input Pounds"))
Shillings = int(input("Input Shillings"))
Pence = int(input("Input Pence"))





def LSD_to_Decimal():
    full_pence = (Shillings * 12) + Pence

    deci_pence = (full_pence / 2.4) / 100

    decimal = Pound + deci_pence

    return decimal 



wage = round(LSD_to_Decimal(), 2)
print(wage)

money = {1 : "Pound", 0.05 : "Shilling", 0.0041666667 : "Pence"}
needed = {"Pound" : 0, "Shilling" : 0, "Pence" : 0}

for coin in money:
    while wage  >= coin:
        needed[money[coin]] += 1
        wage -= coin



print(needed)





            















 
