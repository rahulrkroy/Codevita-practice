from itertools import combinations
n=int(input())
decimal=list(map(int,input().split()))




binary=['0']*100000
# find out largest number and its binary and highest 
lar=max(decimal)
padding=len(bin(lar)[2:])
count=0

# create function to check binary equivalence of a list
def checkbin(a):
    ones,zero=0,0
    for i in a:
        if int(binary[i])>0:
            bini=binary[i]
        else:
            bini=bin(i)[2:]
            t=len(bini)
            if(t<padding):
                temp='0'*(padding-t)
                bini=temp+bini
            binary[i]=bini
        ones+=bini.count('1')
        zero+=bini.count('0')
    if ones==zero:
        return True
    else:
        return False
# find out all combinations and if binary equival increase counter by 1
allcombo=[]
for i in range(1,n+1):
    l=combinations(decimal,i)
    myit=iter(l)
    while(True):
        try:
            temp2=next(myit)
            if checkbin(temp2):
                count+=1
        except:
            break
# print output rounded to highest padding

countbin=bin(count)[2:]
t=len(countbin)
if t<padding:
        temp='0'*(padding-t)
        countbin=temp+countbin

print(countbin)