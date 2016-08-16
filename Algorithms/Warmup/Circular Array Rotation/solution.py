# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k,q = list(map(int,input().strip().split(' ')))
x = list(map(int,input().strip().split(' ')))
k = k % n
a = n - k
y = x[a:]
for m in x[:a]:
    y.append(m)
for i in range(q):
    n = eval(input())
    print((y[n]))
