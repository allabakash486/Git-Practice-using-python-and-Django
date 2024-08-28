def prime(num):
    lv=int(num**(0.5)+1)
    for val in range(2,lv):
        if num%val==0:
            return False
    return True
num=10
print('prime' if prime(num) else 'not prime')
