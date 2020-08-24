n=int(input())
def prime(p):
    for i in range(2,(p//2)+1):
        if p%i==0:
            return(False)
    return(True)
l=[2]
i=2
count=0
while sum(l)<=n:
    i+=1
    if prime(i):
        l.append(i)
        p=sum(l)
        if prime(p) and p<=n:
            count+=1
            

print("Ans=",count)

