n=int(input("Enter no of batches:- "))
t=int(input("Enter time delay in between samples:- "))
batches=list(map(int,(input("Enter no of samples in diff batches:- ").split())))
time=0
batches.sort(reverse=True)
while(batches[0]>0):
    if sum(batches)>len(batches):
        time+=t
        if(t<len(batches)):
            for j in range(t):
                batches[j]-=1
        else:
            for j in range(len(batches)):
                batches[j]-=1
    else:
        if sum(batches)>t:
            time+=t
            for j in range(t):
                batches[j]-=1
        else:
            time+=sum(batches)
            for j in range(len(batches)):
                batches[j]-=1

    batches.sort(reverse=True)
    while(batches[-1]==0):
        if len(batches)>1:
            batches.pop()
        else:
            break

print("Ans=",time)