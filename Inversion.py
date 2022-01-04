a=[5,4,3,2,1]
n=len(a)
c=0
for i in range(n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            c+=1


print(c)



