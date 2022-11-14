n = int(input())
a = []
ct = 0

while ct == 0:
    if n < 2 or n > 10**7:
        print("vui lòng nhập n sao cho 2 <= n <= 10^7",)
        n = int(input())
    elif n >= 2 and n <= 10**7:
        ct += 1

for i1 in range(2,n+1):
    for i2 in range(2,i1+1):
        if i2 == i1:
            a.append(i1)
            break
        elif i1 % i2 == 0:
            break

print(a)

#Cao Hoang Phuoc Bao - Boima