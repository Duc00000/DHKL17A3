a=[]
while True:
    m=int(input("Nhap gia tri: "))  #nhap gia tri
    a.append(m)
    #cho phep nguoi nhap nhap cac pt vao list cho den khi khong can nhap nua
    n=int(input("Tiep tuc nhap gia tri?    1:Co     0:Khong   "))
    if n==1:
        continue
    else:
        break
print("List: ",a) 
def so_nguyen_to(x):
    if x <= 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
b=[]
c=[]
d=[]
for i in a:
    if so_nguyen_to(i):
        b.append(i)

if len(b) != 0:
    print("Cac so nguyen to trong list: ",b)
else:
    print("Khong co so nguyen to nao trong list")

for j in a:
    if j < 0:
        c.append(j)   #them ptu am vao list c
    if j > 0:
        d.append(j)   #them ptu duong vao list d
        

if len(c) != 0:
    print("Cac phan tu am trong list: ",c)
    print("Trung binh cong cac phan tu am: ",sum(c)/len(c))
else:
    print("Khong co phan tu am nao trong list")

if len(d) != 0:   
    print("Cac phan tu duong trong list: ",d)
    print("Trung binh cong cac phan tu duong: ",sum(d)/len(d))
else:
    print("Khong co phan tu duong nao trong list")

print("Gia tri max trong list: ",max(a))
print("Gia tri min trong list: ",min(a))

a.sort()
print("List sap xep tang dan: ",a)

