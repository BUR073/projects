####Factorial
##n = int(input(":"))
##
##def fac():
##    print(n)
##    if n == 0:
##        return 1
##        print('return 1')
##    else:
##        return n*fac(n-1)
##        print('n*fac(n-1')
##
##fac(n)
s = ("help")

def rreverse(s):
    if s == "":
        print("reached base case")
        return s
        
    else:
        print("recursive step with "+s[0])
        return rreverse(s[1:]) + s[0]

dave = rreverse("djfsadjgjhcsdhvkahsdvkjchdkjshvkjdshxkvhdskjhvkjshdzvhshdiohvowhsdh sdxfchdsxhoi hsdoxfhidhfxlkchd iosedhfc iodfcdzxk  ")

print(dave)
