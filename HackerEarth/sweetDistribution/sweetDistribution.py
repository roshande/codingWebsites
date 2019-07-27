
n = int(input())
for a0 in range(n):
    n,m = map(int,input().strip().split(' '))
    sx,sy = map(int,input().strip().split(' '))
    mx,my = map(int,input().strip().split(' '))
    matrix = [[0]*m]*n
    i=sx-1
    j=sy-1
    while(i<n):
        while(j<m):
            matrix[i][j]=1
            if j+1<m and matrix[i][j+1] != 1:
                j=j+1
                if matrix[mx-1][my-1]==1:
                    direct=1
                    break
            elif j-1>=0 and matrix[i][j-1]!=1:
                j=j-1
                if matrix[mx-1][my-1]==1:
                    direct=2
                    break
            elif i-1>=0 and matrix[i-1][j]!=1:
                i=i-1
                if matrix[mx-1][my-1]==1:
                    direct=3
                    break
            elif i+1<n and matrix[i+1][j]!=1:
                i=i+1
                if matrix[mx-1][my-1]==1:
                    direct=4
                    break
            else:
                if matrix[mx-1][my-1]==1:
                    direct=5
                    break
        if matrix[mx-1][my-1]==1:
            break
    if direct==1:
        print("Right")
    elif direct==2:
        print("Left")
    elif direct==3:
        print("Front")
    elif direct==4:
        print("Back")
    elif direct==5:
        print("Over")
