t=input().split()
n=int(t[0])
m=int(t[1])
l=list(map(int,input().split()))
# l.sort()
for _ in range(m):
    k=input().split()
    r1=int(k[0])
    r2=int(k[1])
    l.append(r1)
    l.append(r2)
    l.sort()
    t1=l.index(r1)
    t2=len(l)-l[::-1].index(r2)-1
    c=(t2-t1-1)
    print("ans=",c)
    l.remove(r1)
    l.remove(r2)

    
    
