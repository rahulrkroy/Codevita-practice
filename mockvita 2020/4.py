l=list(map(int,(input().split())))
l.sort(reverse=True)
a=[l[0]]
b=[l[1]]
flag=False
t=0
if(len(l)%2==1):
    flag=True
    t=l.pop()

for i in range(2,len(l),2):
    p=l[i]
    q=l[i+1]
    if (sum(a)>sum(b)):
        a.append(q)
        b.append(p)
    else:
        a.append(q)
        b.append(p)
if flag:
    if (sum(a)>sum(b)):
        b.append(t)
    else:
        a.append(t)
print("Ans=",max(sum(a),sum(b)))
