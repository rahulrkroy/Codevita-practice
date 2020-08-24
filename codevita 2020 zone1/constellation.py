n=int(input())

a=[['.','*','.'],['*','*','*'],['*','.','*']]
e=[['*','*','*'],['*','*','*'],['*','*','*']]
I=[['*', '*', '*'],['.', '*', '.'],['*', '*', '*']]
o=[['*','*','*'],['*','.','*'],['*','*','*']]
u=[['*','.','*'],['*','.','*'],['*','*','*']]


l=[]
l1=[]
t=input()
for i in t:
    l1.append(i)
l.append(l1)
t=input()
l1=[]
for i in t:
    l1.append(i)
l.append(l1)
t=input()
l1=[]
for i in t:
    l1.append(i)
l.append(l1)
ans=''
i=0
p=[l[0][0:3],l[1][0:3],l[2][0:3]]
while(i<n-2):
    # print("i=",i)
    letter=[l[0][i:i+3],l[1][i:i+3],l[2][i:i+3]]
    # print("Letter=",letter)
    if '#' in letter[0][0]:
        i+=1
        ans+='#'
        continue
    else:
        if letter==a:
            ans+='A'
            i+=3
        elif letter==e:
            ans+='E'
            i+=3
        elif letter==I:
            ans+='I'
            i+=3
        elif letter==o:
            ans+='O'
            i+=3
        elif letter==u:
            ans+='U'
            i+=3
        else:
            i+=1
            continue

print("Ans=",ans)