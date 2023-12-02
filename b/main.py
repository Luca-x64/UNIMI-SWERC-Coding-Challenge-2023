d = input().split(" ")

a = []
for i in d:
    a.append(int(i))

x = a[0]
b = a[1]
y = a[2]
d = a[3]

print(max([x*d,x*y,b*y,b*d]))