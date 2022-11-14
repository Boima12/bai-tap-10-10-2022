n, k, ln, t, a =  int(input("nhập n ",)), int(input("nhập k ",)), [], 0, list(map(int, input("nhập các phần tử a :",).split()))

"""for i in range(n):                           
    a.append(int(input()))"""

for sk in range(0,(len(a)-k)+1,1): 
    for i in range(sk,sk+k,1): 
        t += a[i]
    if len(ln) == 0: 
        ln.append(t)
    elif t > ln[0]: 
        ln[0] = t
    t = 0 

print("có k=",k,"phần tử liên tiếp thì được giá trị lớn nhất là",ln[0])

#Cao Hoang Phuoc Bao - Boima
#tất cả code trên được viết theo Boima's algorithm , chính là thuận toán nhà làm của Cao Hoàng Phước Bảo
#đây là code nếu k là phần tử được nhập từ client