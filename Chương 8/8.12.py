n=int(input("Nhập vào n: "))
for i in range(2,n):
    if n%i==0:
        print("Đây không phải là số nguyên tố")
        break
else:
    print("Đây là sô nguyên tố")    