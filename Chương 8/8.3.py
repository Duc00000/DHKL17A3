a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
if a != 0:
    x = -b/a
    print('Nghiệm của phương trình là: ', x)
else:
    if b == 0:
        print('Phương trình vô số nghiệm')
    else:
        print('Phương trình vô nghiệm')        