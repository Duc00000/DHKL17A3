x = int(input("Nhập số tiền cần đổi: "))
print("Số tiền cần đổi là: ", x)
so_to_500 = x // 500000
x = x - so_to_500*500000
so_to_200 = x // 200000
x = x - so_to_200*200000
so_to_100 = x // 100000
x = x - so_to_100*100000
so_to_50 = x // 50000
so_le = x - so_to_50*50000
print("So to menh gia 500.000: ", so_to_500)
print("So to menh gia 200.000: ", so_to_200)
print("So to menh gia 100.000: ", so_to_100)
print("So to menh gia 50.000: ", so_to_50)
print("So tien le: ", so_le)