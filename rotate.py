def rotate(mat):
    res=[]
    for row  in range (len(mat)):
        line =[]
        for col in range (len(mat)-1,-1,-1):
            line.append(mat[col][row])
        res.append(line)
    return res
mat=([1,2,3],[4,5,6],[7,8,9])
print(rotate(mat))


    
