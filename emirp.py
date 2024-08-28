def is_pali(num,copy,dsum=0):
    while num!=0:
        ld=num%10
        dsum=dsum*10+ld
        num//=10
    return copy!=dsum
def is_prime(num):
    for val in range(2,num//2+1):
        if num%val==0:
            return False
    return True
num=13
print('Emirp number' if isprime(num,num) and is_prime(num) and (dsum!=num) else 'not Emirp number')
        
