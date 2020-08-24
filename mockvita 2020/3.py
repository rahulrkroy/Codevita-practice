p=int(input())
q=int(input())
r=int(input())
s=int(input())
c=0
for i in range(p,q+1):
    for j in range(r,s+1):
        # i*j is the size of chocolate
        d=0
        small=min(i,j)
        large=max(i,j)
        print("Small=",small)
        print("Large=",large)
        while(small < large):
            d+=1
            small,large=large-small,small
        c+=(d+2)
        print("c=",c)

print("Ans=",c)