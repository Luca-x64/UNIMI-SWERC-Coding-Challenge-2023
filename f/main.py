
d = input().split(" ")

a = []
for i in d:
    a.append(int(i))

n,g = a[0],a[1] 
#n num studenti
#g tempo per ordine


studenti = []

for i in range(n):
    studenti.append([int(j) for j in input().split(" ")])


#h,m = 14,00
m = 840 #minuti delle 14
last = []
posto=0
p = 0
tmaxOccupato= 0
ofinecliente = 0
for s in studenti:
    oc = s[0]*60+ s[1] #orario cliente
    if oc+g <= m: # riesce guido
        if oc > p:
            p = oc
    ofinecliente = oc+s[2]
if ofinecliente +g<=m :
    p = ofinecliente
    
if n == 0:
    p = m-g
print(p//60,p%60)
