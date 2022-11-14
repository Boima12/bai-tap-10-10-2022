n, ln, t, k, a = int(input("nhập n : ")), [], 0, 0,list(map(int, input("nhập các phần tử a :").split()))

"""for i in range(n):                           
    a.append(int(input()))"""

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
#tất cả code trên được viết theo Boima's algorithm , chính là thuật toán nhà làm của Cao Hoàng Phước Bảo