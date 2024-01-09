import math

def kiem_tra_tam_giac(a, b, c):
    return a + b > c and b + c > a and c + a > b

def tinh_dien_tich_tam_giac(a, b, c):
    if not kiem_tra_tam_giac(a, b, c):
        print("Ba cạnh không hợp lệ để tạo thành tam giác.")
        return None

    p = (a + b + c) / 2
    dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return dien_tich

a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

dien_tich_tam_giac = tinh_dien_tich_tam_giac(a, b, c)
if dien_tich_tam_giac is not None:
    print(f"Diện tích tam giác là: {dien_tich_tam_giac}")