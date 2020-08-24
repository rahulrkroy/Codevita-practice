
m,n=map(int,input().split())
arr=[]
for i in range(m):
    l=list(map(int,input().split()))
    arr.append(l)

rot=list(map(int,input().split()))
nooflayer=len(rot)
g=[[0 for i in range(n)] for j in range(m)]

# rotate
def rotate_clock(row_start,row_end,col_start,col_end,r,arr):
    z=[]
    # print("row end",row_end,col_end,row_start,col_start)

    for i in range(col_start,col_end):
        z.append(arr[row_start][i])
    
    for i in range(row_start+1,row_end):
        z.append(arr[i][col_end-1])

    for i in range(col_end-2,col_start-1,-1):
        z.append(arr[row_end-1][i])

    for i in range(row_end-2,row_start,-1):
        z.append(arr[i][col_start])

    # print("final z=",z)
    r=r%(len(z))

    k=z[-r:]+z[:-r]
    # print(k)
    j=0
    for i in range(col_start,col_end):
        g[row_start][i]=k[j]
        j+=1
    
    for i in range(row_start+1,row_end):
        g[i][col_end-1]=k[j]
        j+=1

    for i in range(col_end-2,col_start-1,-1):
        g[row_end-1][i]=k[j]
        j+=1

    for i in range(row_end-2,row_start,-1):
        g[i][col_start]=k[j]
        j+=1



def rotate_anti(row_start,row_end,col_start,col_end,r,arr):
    z=[]
    
    for i in range(col_start,col_end):
        z.append(arr[row_start][i])
    
    for i in range(row_start+1,row_end):
        z.append(arr[i][col_end-1])

    for i in range(col_end-2,col_start-1,-1):
        z.append(arr[row_end-1][i])

    for i in range(row_end-2,row_start,-1):
        z.append(arr[i][col_start])

    # print("final z=",z)
    r=r%(len(z))
    

    k=z[r:]+z[:r]
    # print(k)
    j=0
    for i in range(col_start,col_end):
        g[row_start][i]=k[j]
        j+=1
    
    for i in range(row_start+1,row_end):
        g[i][col_end-1]=k[j]
        j+=1

    for i in range(col_end-2,col_start-1,-1):
        g[row_end-1][i]=k[j]
        j+=1

    for i in range(row_end-2,row_start,-1):
        g[i][col_start]=k[j]
        j+=1



for i in range(0,nooflayer):
    if (i+1)%2==0:
        rotate_clock(0+i,m-i,0+i,n-i,rot[i],arr)
    else:
        rotate_anti(0+i,m-i,0+i,n-i,rot[i],arr)



for i in range(m):
    for j in range(n):
        print(g[i][j],end=' ')
    print()