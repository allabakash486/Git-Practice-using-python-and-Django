'''def sqr(num,sol=0):
    while num!=0:
        sol += (num%10)**2
        num //= 10
    return sol
def Happy(num):
    while num>9:
        num = sqr(num)
    return num==1 or num==7
print('Happy number' if Happy(19) else 'Not')
def sqr(num):
    if num ==0:
        return 0
    return ((num%10)**2) +sqr(num//10)
def Happy(num):
    if num<=9:
        return num==1 or num==7
    return Happy(sqr(num))
print('Happy number' if Happy(19) else 'Not a happy number')
# Bubble sort method
L= [1,2,3,4,5,6,0,9,8,7,6,5,4,32,1,2]
for val in range(len(L)-1,0,-1):
    for ind in range(val):
        if L[ind]>L[ind+1]:
            L[ind],L[ind+1]=L[ind+1],L[ind]
print(L)
#Selection sort method
l=[1,2,3,4,5,6,0,9,8,7,6,5,4,32,1,2]
for val in range(len(l)):
    lowind = val
    for ind in range(val+1,len(l)):
        if l[lowind]>l[ind]:
            lowind=ind
    l[val],l[lowind]=l[lowind],l[val]
print(l)
# Quick sort
l=[1,2,3,4,5,6,0,9,8,7,6,5,4,32,1,2]
def quick(l):
    if len(l)<=1:
        return l
    pivot = l[0]
    left= [ l[i] for i in range(1,len(l)) if pivot>l[i]]
    right = [ l[i] for i in range(1,len(l)) if pivot<=l[i]]
    return quick(left) + [pivot] + quick(right)
print(quick(l))
# Merg sort 
l=[1,2,3,4,5,6,0,9,8,7,6,5,4,32,1,2]
def conqure(Mlist,Leftlist,Rightlist):
    li,mi,ri=0,0,0
    while li<len(Leftlist) and ri<len(Rightlist):
        if Leftlist[li]>Rightlist[ri]:
            Mlist[mi] = Rightlist[ri]
            ri+=1
        else:
            Mlist[mi] = Leftlist[li]
            li +=1
        mi +=1
    while ri<len(Rightlist):
        Mlist[mi] = Rightlist[ri]
        ri +=1
        mi +=1
    while li<len(Leftlist):
        Mlist[mi] = Leftlist[li]
        li +=1
        mi +=1
def divid(l):
    if len(l)>1:
        left,right = l[:len(l)//2],l[len(l)//2:]
        divid(left)
        divid(right)
        conqure(l,left,right)
divid(l)
print(l)
# Linear search
l=[1,2,3,4,5,6,7]
user = 7
for val in range(len(l)):
    if user == l[val]:
        print(val)
        break
else:
    print(-1)
# Binary search
l=[1,2,3,4,5,6,7]
low =0
high= len(l)-1
user = 5
while (l[low]<=user<=l[high])and (low<high):
    mid = (low + ((low-high)//(l[low]+l[high]))*(user-l[low]))
    if user <l[mid]:
        high -=1
    elif user >l[mid]:
        low +=1
    elif user == l[mid]:
        print(mid)
        break
    else:
        print(-1)'''
import numpy as np
mat1 = np.array([[1,2,34,5],[1,2,3,5]])
mat2 = np.array([[2,3,4,5],[1,2,3,4]])
print(np.dot(mat2,mat1),axis=1)


        
    
    




















        
              
    
    
    
