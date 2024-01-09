n=int(input("Nhập vào n:"))
def so_hoan_hao(n):
    if n<0:
        return False
    tong_uoc=0
    for i in range(1,n):
        if n%i == 0:
            tong_uoc+=i
    if tong_uoc == n:
        return True
    else:
        return False
if so_hoan_hao(n):
    print(n,"là số hoàn hảo")
else:
    print(n,"không là số hoàn hảo")