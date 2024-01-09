#Tính chu vi và diện tích hình tròn 
dien_tich = lambda r: 3.14 * r**2
chu_vi = lambda r: 2 * 3.14 * r
print("Diện tích hình tròn là",dien_tich(5))
print(f"Chu vi hình tròn là",chu_vi(5))
#Tính chu vi và diện tích hình chữ nhật
dien_tich = lambda a, b: a * b
chu_vi = lambda a, b: 2 * (a + b)
print("Diện tích hình chữ nhật là",dien_tich(4,5))
print("Chu vi hình chữ nhật là",chu_vi(4,5))