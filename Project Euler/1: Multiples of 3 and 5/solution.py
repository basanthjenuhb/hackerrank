def count(a,n):
    return a*n*(n+1)/2

k = eval(input())
for i in range(k):
    n, sum = eval(input()), 0
    n-=1
    print((count(3,n/3)+count(5,n/5)-count(15,n/15)))
