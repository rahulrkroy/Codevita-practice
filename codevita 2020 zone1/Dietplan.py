total=input()
l=list(input().split('|'))

# arrangement
c=''
limitF,limitC,limitP=0,0,0
for i in total:
    if i==' ':
        continue
    elif i=='P':
        limitP=int(c)
        c=''
    elif i=='C':
        limitC=int(c)
        c=''
    elif i=='F':
        limitF=int(c)
        c=''
    else:
        c+=i



currC,currF,currP=0,0,0
data=[]
for i in l:
    c=''
   
    for j in i:
        if j==' ':
            continue
        elif j=='P':
            currP=(int(c))
            c=''
        elif j=='C':
            currC=int(c)
            c=''
        elif j=='F':
            currF=int(c)
            c=''
        else:
            c+=j
    data.append([currP,currC,currF])



data.sort(key=sum,reverse=True)

usable=[True for i in range(len(data))]
while(True):
    flag=True
    for i in range(len(data)):
        if(usable[i] and (limitP-data[i][0]>=0) and (limitC-data[i][1]>=0) and (limitF-data[i][2]>=0)):
            limitP-=data[i][0]
            limitC-=data[i][1]
            limitF-=data[i][2]
            flag=False
        else:
            usable[i]=False
    if(flag):
        break
    
print("Ans=", limitP," ",limitC," ",limitF)