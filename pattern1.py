var=5
for line in range(1,var+1):
    print(f"{'* '*var}")
print()

var=5
star=1
for line in range(1,var+1):
    print(f"{'*'*star}")
    star+=1
print()
var=5
space=var-1
star=1
for line in range(1,var+1):
    print(f"{' '*space}{'*'*star}")
    space-=1
    star+=1
print()
var=5
space=0
star=var
for line in range(1,var+1):
    print(f"{' '*space}{'*'*star}")
    star-=1
    space+=1
print()
n=15
star=1
space=n-1
for line in range(1,n+1):
    print(f"{' '*space}{'*'*star}")
    star+=2
    space-=1
print()
var=15

star=2*var-1
space=0
for line in range(1,var+1):
    print(f"{' '*space}{'*'*star}")
    star-=2
    space+=1
print()
var=15

space=n//2
star=1
for line in range(n//2+1):
    print(f"{' '*space}{'*'*star}")
    star+=2
    space-=1
space=1
star=n-2
for line in range(n//2):
    print(f"{' '*space}{'*'*star}")
    star-=2
    space+=1
print()
n=7
star=n
space=0
for line in range(n//2+1):
    print(f"{' '*space}{'*'*star}")
    star-=2
    space+=1
star=3
space=n//2-1
for line in range(n//2+1):
    print(f"{' '*space}{'*'*star}")
    star+=2
    space-=1
    

    
