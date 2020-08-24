m,n=map(int,input().split())

d={}
for i in range(m):
    t=[]
    l=input().split()
    a=int(l[0])
    b=int(l[1])
    if a in d:
        d[a].append(b)
    else:
        t.append(b)
        d[a]=t

print("d=",d)