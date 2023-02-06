##import textwrap
##
##rawS = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras id turpis sed ipsum mattis vestibulum. Donec in tortor arcu. Duis egestas ipsum ipsum, quis maximus ipsum hendrerit eget. Nunc commodo ipsum tristique congue accumsan. Sed condimentum neque a odio porttitor convallis. Fusce eleifend libero ipsum, sagittis tincidunt metus elementum ac. Aenean sodales nunc quis erat faucibus, vel consequat quam posuere. Fusce vitae nisl sodales, tristique lacus quis, lobortis lacus")
##
##list = (rawS.split())
##print(list)
##
##def wraptext(width = 40):
##    lines = []
##    for i in range(0, len(rawS), width):
##        lines.append(rawS[i:i+width])
##    print( '\n'.join(lines))
##
##def wrapText(width=50):
##    i = width
##    rawS = list(rawS)
##    while width < (len(rawS)):
##        while i > rawS[i] != " ":
##            i = i - 1
##            rawS[i].append = '/n'
##            i = i + width 
##




    
def wrapIt(s ,width=80):
    s = list(s)
    i = width
    while i < len(s):
        while i > 0 and s[i] != ' ':
            i = i - 1
        s[i] = '\n'
        i = i + width
    return "".join(s)


print( wrapIt("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras id turpis sed ipsum mattis vestibulum. Donec in tortor arcu. Duis egestas ipsum ipsum, quis maximus ipsum hendrerit eget. Nunc commodo ipsum tristique congue accumsan. Sed condimentum neque a odio porttitor convallis. Fusce eleifend libero ipsum, sagittis tincidunt metus elementum ac. Aenean sodales nunc quis erat faucibus, vel consequat quam posuere. Fusce vitae nisl sodales", 24 ))x









