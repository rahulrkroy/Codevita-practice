p=input().split(',')
n=int(p[0])
k=int(p[1])
l=[1]
for i in range(2,(n//2)+1):
    if(n%i)==0:
        l.append(i)
l.append(n)
if k>len(l):
    print("1")
else:
    print(l[-k])