#interpolation program
c=[1,23,2,3,4,5]
for line in range(len(c)-1,0,-1):
    for line1 in range(line):
        if c[line1]>c[line1+1]:
            c[line1],c[line1+1]=c[line1+1],c[line1]
print(c)
#interpolation for highest element program
c=[1,23,2,3,4,5]
for line in range(len(c)-1,len(c)-2,-1):
    for line1 in range(line):
        if c[line1]>c[line1+1]:
            c[line1],c[line1+1]=c[line1+1],c[line1]
print(c[-1])
#interpolation for lowest element
c=[1,23,2,3,4,5]
for line in range(len(c)-1,len(c)-2,-1):
    for line1 in range(line):
        if c[line1]<c[line1+1]:
            c[line1],c[line1+1]=c[line1+1],c[line1]
print(c[-1])
#interplolation method
l=[1,2,3,4,5,234]
user=234
low=0
high=len(l)-1
while l[low]<=user<=l[high] and low<=high:
    ind=int(low+((low-high)/(l[low]-l[high]))*(user-l[low]))#interpolation formula
    if l[ind]>user:
        high=ind-1
    elif l[ind]<user:
        low=ind+1
    elif l[ind]==user:
        print(ind)
        break
else:
    print(-1)
    

    
