n1,n2,n3 = raw_input().split()
h1 = map(int,raw_input().split())
h2 = map(int,raw_input().split())
h3 = map(int,raw_input().split())
s1,s2,s3 = sum(h1),sum(h2),sum(h3)
while not (s1==s2 and s1==s3):
    if s1 >= s2 and s1>=s3: s1 -= h1.pop(0)
    elif s2 >= s1 and s2>=s3: s2 -= h2.pop(0)
    elif s3 >= s1 and s3 >= s2: s3 -= h3.pop(0)
print s1
