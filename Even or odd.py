
'''for even in range(0,10):
    if even %2 ==0:
        print(f'{even} is even')
    else:
        print(f'{even} is not a even')

for odd in range(0,10):
    if odd %2 ==1:
        print(f'{odd} is odd')
    else:
        print(f'{odd} is not a odd')'''
s='madam'

for ind in range(len(s)//2+1):
    if s[ind]!=s[-1-ind]:
        print('Not palindrome')
        break
    
else:
    print('Palindrome')
