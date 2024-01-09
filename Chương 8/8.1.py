a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
c = int(input('Nhập c: '))
d = int(input('Nhập d: '))

max = a
min = a

if b > max:
    max = b
elif b < min:
    min = b

if c > max:
    max = c
elif c < min:
    min = c

if d > max:
    max = d
elif d < min:
    min = d
print("Số lớn nhất là:", max)
print("Số nhỏ nhất là:", min)