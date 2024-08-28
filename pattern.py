# Patterns
#1 square pattern
lines = 5
for val in range(lines):
    print('* '*lines)
#line
print("- "*20)
#Triangle Pattern
lines=5
star=1
for val in range(1,lines+1):
    print("* "*star)
    star+=1
#opposit pattern for triangle
lines=5
space=1,
for val in range(1,lines+1):
    print(' '*space,end=' ')
    print('* '*val)
    print()
    space -=1
