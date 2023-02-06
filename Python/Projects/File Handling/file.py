fh1 = open("demo.dat", "r")
print(fh1)

word = "INTERESTING"

for line in fh1.readlines():
    x = (line[18:29])
    print(x)
    print(len(x))

line = fh1.readline()
