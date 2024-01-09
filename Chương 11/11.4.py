def danh_sach():
    danh_sach = []
    while True:
        phan_tu = input("Nhập một số nguyên (nhập 'x' để kết thúc): ")
        if phan_tu == 'x':
            break
        danh_sach.append(int(phan_tu))
    return danh_sach
a=danh_sach()
print("List:",a)
print("Tổng các giá trị trong list:",sum(a))
x=int(input("Nhập giá trị cần tìm:"))
print(x,"xuất hiện",a.count(x),"lần trong list")
if x > max(a):
    print(x,"lớn hơn tất cả các số trong list")
else:
    print(x,"không lớn hơn tất cả các số trong list")   
print("Các số lớn hơn",x,"trong list:",end=" ")
for i in a:
    if i > x:
        print(i,end=",")      
