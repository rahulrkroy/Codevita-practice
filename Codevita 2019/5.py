for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    s=l[0]
    t=0
    for i in range(1,n):
        s=s+l[i]
        t+=s
    print("ans=",t)
