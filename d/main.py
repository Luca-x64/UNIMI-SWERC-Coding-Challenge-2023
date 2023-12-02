k = int(input())

x,y = 1,1
cnt = 0

for x in range(k)[1:]:
    for y in range(k)[1:]:
            if x*y < k:
                cnt+=1
            elif x*y > k:
                break

print(cnt)


