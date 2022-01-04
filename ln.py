a=[10,7,6,4,5,2,8,3,11]
ht={}
ans=1
for ele in a:
    ht[ele]=True

for ele in a:
    if(ele -1 not in ht):
        c=1
        while(ele + c in ht):
            c+=1

        if(c>ans):
            ans=c
print(ans)


