a = map(int,raw_input().split())
b = map(int,raw_input().split())
s1,s2=0,0
for i in range(3):
    if a[i] == b[i]:continue
    if a[i] > b[i]:s1+=1
    else:s2+=1
print s1,s2
