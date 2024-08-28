length = int(input('Enter the length of list:'))
mat=[]
for element in range(length):
    listelement=[]
    ele_size =int(input('enter elementlist size:'))
    for row in range(ele_size):
        num = int(input('enter the element:'))
        listelement.append(num)
    mat.append(listelement)
print(mat)
