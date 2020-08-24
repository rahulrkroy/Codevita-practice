n=int(input())
l=list(map(int,(input().split())))
print("l=",l)
bit_scores=[]
for i in l:
    p=i
    t=[]
    while(p>0):
        t.append(p%10)
        p=p//10
    a=max(t)*11
    b=min(t)*7
    a=a+b
    if (a>100):
        a=a%100
    bit_scores.append(a)
t=0
print("bit scores:",bit_scores)
even=[0,0,0,0,0,0,0,0,0,0]
odd=[0,0,0,0,0,0,0,0,0,0]
for i in range(len(bit_scores)):
    if bit_scores[i]>9:
        t=bit_scores[i]//10
    else:
        t=bit_scores[i]
    if((i+1)%2==0):
        even[t]+=1
    else:
        odd[t]+=1

print("Even=",even)
print("odd=",odd)

t=0
for i in even:
    p=0
    if i==2:
        p=1
    elif i>2:
        p=2
    t+=p
    
for i in odd:
    p=0
    if i==2:
        p=1
    elif i>2:
        p=2
    t+=p

print("Ans=",t)


