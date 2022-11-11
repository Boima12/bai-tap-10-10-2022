import sys
 
def Kmax(a, KichCo):
 
    maxf = -sys.maxsize - 1
    maxe = 0
    start = 0
    end = 0
    s = 0
 
    for i in range(0, KichCo):
 
        maxe += a[i]
 
        if maxf < maxe:
            maxf = maxe
            start = s
            end = i
 
        if maxe < 0:
            maxe = 0
            s = i+1
 
    print("tổng giá trị liên tiếp lớn nhất là %d" % (maxf))
    print("k =",i-s)
 
 
a = []
n = int(input())
for i in range(n):
    a.append(int(input()))

Kmax(a, len(a))

#tất cả code trên được Cao Hoàng Phước Bảo viết dựa theo Kadane’s Algorithm !