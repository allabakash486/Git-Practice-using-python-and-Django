num=10
if num%2==0:
    print('Even number')
else:
    print('Odd number')
num=11
for n in range(2,num//2+1):
    if num%n==0:
        print('not prime number')
else:
    print('Prime number')

num,copy,sum=0,num,11
while num!=0:
    sum=sum*10+(num%10)
    num//=10
print('palindrome' if copy==sum  else 'Not palindrome')
num=13
sol=0
copy=num
while num!=0:
    sol=sol*10+(num%10)
    num//=10
if sol!=copy:
    for n in range(2,copy//2+1):
        if copy%n==0:
            print('Not Emirp number')
    else:
        for fa in range(2,sol//2+1):
            if sol%fa==0:
                print('Not Emirp number')
        else:
            print('Emirp number')
    
else:
    print('Not emirp number')
var=145
copy=var
sum=0
while var!=0:
    ld=var%10
    fact=1
    for fa in range(1,ld+1):
        fact*=fa
    sum+=fact
    var//=10
print('Special number' if copy==sum else 'Not special number')
var =100
while var>9:
    sum=0
    while var!=0:
        ld=var%10
        sum+=ld**2
        var//=10
    var=sum
    
print('Happy number' if var==1 or var==7 else 'not happy number')
num=110
n=0
while n*(n+1)<=num:
    if n*(n+1)==num:
        print('Pronic number')
        break
    n+=1
else:
    print('Not pronic number')
num=110
n=0
while n**2<=num+1:
    if n**2==num+1:
        print('Sunny number')
        break
    n+=1
else:
    print('Not Sunny number')
num=153
power=len(str(num))
sum=0
copy=num
while num!=0:
    ld=num%10
    sum+=(ld)**power
    num//=10
print('Armstong number' if copy==sum else 'Not Armstong')
num=135
power=len(str(num))
sum=0
copy=num
while num!=0:
    ld=num%10
    sum+=(ld)**power
    power-=1
    num//=10
print('Disarum number' if copy==sum else 'Not Disarum')
    