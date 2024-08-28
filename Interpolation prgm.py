#for Boublesort  but in bouble sort we can apply 
c=[1,32,4,5,67,8]
for line in range(len(c)-1,0,-1):
    for line2 in range(line):
        if c[line2]>c[line2+1]:
            c[line2],c[line2+1]=c[line2+1],c[line2]

print(c)
#for binary search we need to be remove duplicte and we need to sort the list
l=c
user=8
low=0
high=len(l)-1
while low<=high:
    mid=(low+high)//2
    if l[mid]>user:
        high=mid-1
    elif l[mid]<user:
        low=mid+1
    elif l[mid]==user:
        print(mid)
        break
else:
    print(-1)
