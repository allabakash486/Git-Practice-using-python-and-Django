def fact(num,mul=1):
    for val in range(1,num+1):
        mul *=val
    return mul
def digi(num,copy,sum=0):
    while num!=0:
        ld=num%10
        sum+=fact(ld)
        num//=10
    return sum==copy
def special(num):
    return digi(num,num)
num =145
print('special number' if special(num) else 'not special number')
