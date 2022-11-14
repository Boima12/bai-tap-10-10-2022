# bài 1 tính tổng các số nguyên lẻ trong dãy
n = int(input())
a = list(map(int, input().split()))
t = 0

"""for i in range(0,n):
    a.append(int(input()))"""

for i in a:
    if i % 2 != 0:
        t += i

print("tổng số nguyên lẻ trong dãy là:",t)

#Cao Hoang Phuoc Bao - Boima