d = input().split(" ")

aa = []
for i in d:
    aa.append(int(i))

tupla = []
n = aa[0] #n totale linee bus differenti
for i in range(n):
    tupla.append([int(j) for j in input().split(" ")])
#print(tupla)

k = aa[1] #6 euro #costo giornaliero
#a = bb[0] # primo giorno
#b = bb[1] # ultimo giorno
#p = bb[2] # prezzo al giorno

t = tupla
costo = 0

lastday = 0
lastcosto = 0
for i in range(len(t)):

    a = t[i][0] # primo day
    b = t[i][1] # ultimo day
    c = t[i][2] # costo
    #print("lastday,lastcosto: ",lastday,lastcosto)
    if lastday >= a:
        diffNday = lastday-a +1 #differenza giorni overlaps
        if diffNday * lastcosto + diffNday*c >= k*diffNday: #1*4 + 1*4 = 8
                                                    # 8 > 6? si
            costo = costo - diffNday*lastcosto + diffNday*k
            #print("costo sub",costo)
        else:
            costo += (b-a +1) * c
            
        nviaggi = b - lastday
        costo += nviaggi*c
        #print("costo fine if",costo)
    else:
        nviaggi = b - a +1
        #print("nviaggi:",nviaggi)

        costo += nviaggi*c
        #print("costo:",costo)
        
    lastday = b
    lastcosto = c

print(costo)
    
    
    

