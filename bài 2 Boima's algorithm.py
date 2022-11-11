a, ln, t, k, n = [], [], 0, 0, int(input())

for i in range(n):                           
    a.append(int(input()))

for kc in range(len(a),1,-1):  
    for sk in range(0,(len(a)-kc)+1,1): 
        for i in range(sk,sk+kc,1): 
            t += a[i]
        if len(ln) == 0: 
            ln.append(t)
        elif t > ln[0]: 
            ln[0] = t
            k = kc
        t = 0 

print("có k=",k,"phần tử liên tiếp thì được giá trị lớn nhất là",ln[0])

#Cao Hoang Phuoc Bao - Boima
#tất cả code trên được viết theo Boima's algorithm , chính là thuận toán nhà làm của Cao Hoàng Phước Bảo