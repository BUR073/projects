fh1 = open("shorelines.txt", "r")
print(fh1)

for line in fh1.readlines():
    print(line)

line = fh1.readline()


## Demial Degrees = Degrees + (Minutes/60) + (Seconds/3600)
