# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k,q = map(int,raw_input().strip().split(' '))
x = map(int,raw_input().strip().split(' '))
k = k % n
a = n - k
y = x[a:]
for m in x[:a]:
    y.append(m)
for i in range(q):
    n = input()
    print y[n]
