def calc(hist,n):
	ans=0
	for i in range(n):
		
		if hist[i]>0:
			ans=max(ans,1)
		
		places=2
		least=hist[i]
		# print(i,min(i+hist[i]-1,n))
		for j in range(i+1,min(i+hist[i],n)):
			if hist[j]>=places and places<=least:
				ans=max(ans,places)
				places+=1
				least = min(least,hist[j])
			else:
				break
	return ans

n = int(input())

mat = []
for r in range(n):
    cols=input().split()
    mat.append(cols)

hist1,hist2=[0]*n,[0]*n

for i in range(n):
    d1=0
    d2=0
    for j in range(n):
        if mat[i][j]=='D':
            d1+=1
        if mat[j][i]=="D":
            d2+=1
    hist1[i]=d1
    hist2[i]=d2
    # print(hist1,hist2)
a1=calc(hist1,n)
    # print(a1)
a2=calc(hist2,n)
    # print(a2)
print(max(a1,a2))