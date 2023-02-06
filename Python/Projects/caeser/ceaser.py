word = "xyz"; places = 28
if places > 25: places = places - 25; res = '.'.join(word[i:i + 1] for i in range (0, len(word), 1)); list = res.split("."); res = [ord(ele) for sub in list for ele in sub]; res = [x+places for x in res]; newList = []
for i in res:
    if i >= 122:i = i - 25; newList.append(i)
else: newList.append(i)
s = "".join([chr(c) for c in newList]); print(s)



    


