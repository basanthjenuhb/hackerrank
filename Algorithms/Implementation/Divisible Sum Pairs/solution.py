n,k = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
count=0
for i in range(n):
    for j in range(i):
        if (a[i]+a[j])%k == 0:count+=1
print count
