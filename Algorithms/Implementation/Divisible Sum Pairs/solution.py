n,k = list(map(int,input().strip().split(' ')))
a = list(map(int,input().strip().split(' ')))
count=0
for i in range(n):
    for j in range(i):
        if (a[i]+a[j])%k == 0:count+=1
print(count)
