def taobang(b):
    for i in range(1,1000,1):
        b.append(i)
    return b
def nhap(c,n):
    for i in range(1, n + 1):
        m = int(input("Nhap so thu {}: ".format(i)))
        c.append(m)
    return c
if __name__ == '__main__':
    b=[]
    c=[]
    b=taobang(b)
    n = int(input("Ban muon nhap vao day bao nhieu so:"))
    c=nhap(c,n)
    for i in b:
        dem=0
        for j in c:
            if i%j==0:
                dem+=1
        if dem==n:
            print("Uoc chung lon nhat cua cac so la:",i)
            break

