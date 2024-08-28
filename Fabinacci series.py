#write a program to print fabinacci series  range of the program
'''end_value = int(input("Enter the ending value"))
num1 = 0
num2 = num1+1
next_num = (num1 + num2)
print(num1,num2,end=' ')
while (next_num <= end_value):
    print(next_num,end=' ')
    num1 = num2
    num2 = next_num
    next_num = num1 + num2'''
#write a program to print fabinacci series from range to range
sv = int(input("Enter the starting value :"))
ev = int(input("Enter the ending value :"))
num = sv
num2 = num+1
next_num = (num+num2)
print(num,num2,end=' ')
while (next_num <= ev):
    print(next_num,end=' ')
    num = num2
    num2 = next_num
    next_num = (num+num2)
