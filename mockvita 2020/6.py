import math

for _ in range(int(input())):
    l=list(map(int,(input().split())))
    a=l[0]
    h=l[1]
    l1=l[2]
    l2=l[3]
    m=l[4]
    c=l[5]
    luck=l1/l2
    attack=m*(a+c)*luck
    print("Attack=",attack)


