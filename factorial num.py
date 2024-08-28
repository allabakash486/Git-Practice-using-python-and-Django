var=10
facount=0
if var>=2:
    for num in range(1,var+1):
        if var%num==0:
            facount +=1
    if facount ==2:
        print(f'{var} is prime')
    else:
        print(f'{var} is not prime')

else:
    print(f'{var} is not prime')

var=10
facount=0
if var>=2:
    for num in range(1,var+1):
        if var%num==0:
            facount +=1
    if facount !=2:
        print(f'{var} is composite')
    else:
        print(f'{var} is not composite')

else:
    print(f'{var} is not composite')

'''factorial program'''

vaar =5
factorial =1
for num in range(1,vaar+1):
    factorial *=num
print(factorial)
'''reverse of a number'''
var =123
vaar =var
rev =0
while var!=0:
    rem=var%10
    rev=rev*10+rem
    var//=10
print(rev)

var =121
copy =var
rev =0
while var!=0:
    rem=var%10
    rev=rev*10+rem
    var//=10
print()
if rev==copy:
    print(f'{copy} is palindrome')
else:
    print(f'{copy} not palindrome')
