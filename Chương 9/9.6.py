x=int(input("Nhập vào x: "))
def kiem_tra_so_nguyen_to(x):
    if x == 1:
        return False
    elif x ==2:
        return True
    else:
        for i in range (2,x):
            if x%i == 0:
                return False
            else:
                return True

if kiem_tra_so_nguyen_to(x):
    print(x,"là số nguyên tố")
else:
    print(x,"không là số nguyên tố")

            