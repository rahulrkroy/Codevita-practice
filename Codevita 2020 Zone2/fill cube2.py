n = int(input())

mat = []
for r in range(n):
    cols=input().split()
    mat.append(cols)

def calc(a):
    while(True in (['D' in a[i] for i in range(n)])):
        for i in range(n-1,-1,-1):
            for j in range(n):
                if a[i][j]=='D' and not(i==0):
                    for k in range(i,0,-1):
                        a[k][j]=a[k-1][j]
                    a[0][j]='-'
    print("mat a=",a)   
    return 1     


c=[]
for i in range(4):
    sub=[row[:] for row in mat]
    c.append(calc(sub))
    rotated=list(zip(*mat[::-1]))
    mat=rotated

print(max(c))

