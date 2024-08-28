'''CDT = [1,2,3,4,4,3,21,55,66,1,2,3,4]
def Removing_duplicates(CDT):
    print(set(CDT));
Removing_duplicates(CDT);
num =145
def Is_special(num,dup=num,sol=0):
    while num != 0:
        ld = (num%10);
        fact = 1;
        for value in range(1,ld+1):
            fact *= value;
        sol += fact;
        num //=10;
    return sol == dup;
print("Special Number" if Is_special(145) else 'Not Special Number');
num = 145
dup = num
def sqr(ld,n=1):
    if n == ld:
        return ld
    return n*sqr(ld,n+1)
def special(num):
    if num == 0:
        return 0
    return sqr(num%10)+special(num//10)
print('Special number' if special(num)== dup  else 'Not')'''
string = 'happy birth of the baby';
string += ' '
result = []
sol = ''
for val in range(len(string)-1,-1,-1):
    if string[val] == ' ':
        result.append(sol)
        sol =''
    else:
        sol += string[val]
print(' '.join(result))

            
    
