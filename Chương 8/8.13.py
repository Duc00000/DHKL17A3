n=int(input("Nhập n: "))
s=0
for i in range(1,n+1):
    if i%2 != 0:
        s+=i
print("A =",s)
s1=0
for i in range(1,n+1):
    if i%2 == 0:
        s1+=i
print("B =",s1)
s2=1
for i in range(1,n+1):
    s2*=i
print("C =",s2)
s3=1
for i in range(1,n+1):
    if i%3 == 0:
        s3*=i
print("D =",s3)
s4=0
for n in range(2,n):
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        s4+=n
print("E =",s4)
s5=0
for i in range(1,n+1):
    if i%2 == 0:
        s5-=(1/i)
    elif i%2 != 0:
        s5+=(1/i)
print("F =",s5)