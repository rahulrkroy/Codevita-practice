n=int(input())
bride=input()
groom=input()
while(True):
    if(len(bride)==0): 
        break
    else:
        c=bride[0]
        flag=False
        for i in range(len(groom)):
            if groom[0]==c:
                groom=groom[1:]
                bride=bride[1:]
                flag=True
                break
            else:
                groom=groom[1:]+groom[0]
        if(flag==False):
            break
print(len(bride))
