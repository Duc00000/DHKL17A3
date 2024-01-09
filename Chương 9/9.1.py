x=float(input("Nhập vào x: "))
def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1
print(sign(x))