from itertools import combinations
n=int(input())
digits=list(map(int,input().split()))

letters=['']*100
letters=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
arr=[2,2,1,2,2,2,1,2,1,2,1,3,2,3,4,3,3,4,3,4,1]
t=[0]*80
arr+=t
arr[30]=1
arr[40]=1
arr[50]=1
arr[60]=1
arr[70]=2
arr[80]=1
arr[90]=2
arr[100]=2
t=[""]*80
letters+=t
letters[30]="thirty"
letters[40]="forty"
letters[50]='fifty'
letters[60]='sixty'
letters[70]="seventy"
letters[80]="eighty"
letters[90]="ninety"
letters[100]="hundred"

t=0
for i in range(21,100):
    if(i%10==0):
        continue
    t1=i%10
    t2=i//10
    arr[i]=arr[t1]+arr[t2*10]

t=0
for i in range(21,100):
    if(i%10==0):
        continue
    t1=i%10
    t2=i//10
    letters[i]=letters[t2*10]+' '+letters[t1]
flag=True
# print(letters)
D=0
for i in digits:
    if(i>100):
        print("greater 100")
        flag=False
        break
    else:
        D+=arr[i]
if flag:
    count=0
    combo=list(combinations(digits,2))
    for i in combo:
        if sum(i)==D:
            count+=1

    if(count>100):
        print("greater 100")
    else:
        print(letters[count])





print("68",letters[68])