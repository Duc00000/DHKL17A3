n=float(input("Nhập vào n:"))
x=float(input("Nhập vào x:"))
def a(n,x):
    a=(x**2+x+1)**n + (x**2-x+1)**n
    return a
print(a(n,x))
    