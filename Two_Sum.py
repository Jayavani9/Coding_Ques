a=[2,5,1,3,4,2,6]
n=len(a)
target=10
ht={}
for i in range(n):
    if(a[i] in ht):
        ht[a[i]].append(i)
    else:
        ht[a[i]]=[i]
print(a)
print(ht)

'''c=0
for i in range(n):
    key=target-a[i] '''

