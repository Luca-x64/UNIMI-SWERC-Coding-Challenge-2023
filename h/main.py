import math
d = input().split(" ")

a = []
for i in d:
    a.append(int(i))

n,x = a[0],a[1] 
#n numero di funi 
#x num max di operazioni

funi = []
funi= [int(j) for j in input().split(" ")]
print(funi)

print(funi)
c = min(funi)/2
print(c)
for i in range(x):
    if c > min(funi):
        #c = (math.floor(min(funi)))/2
        c-=1
    indexMax = max(funi)
    l1,l2 = c, indexMax-c
    funi.append(l1)
    funi.append(l2)
    funi.remove(indexMax)
    
    print("c",c)

print(funi)
print("out",math.ceil(max(funi)))
