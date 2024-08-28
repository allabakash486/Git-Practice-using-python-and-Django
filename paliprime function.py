def is_pali(num,dup,res=0):
    while num!=0:
        ld=num%10
        res = res*10+ld
        num //= 10
    return res == dup
def is_prime(num):
    for val in range(2,num//2+1):
        if num%val==0:
            return False
    return True
num =11
print('paliprime' if is_pali(num,num) and is_prime(num) else 'not paliprime')
