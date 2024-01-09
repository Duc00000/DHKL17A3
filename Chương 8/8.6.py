loai_xe = int(input('Nhập loại xe: '))
so_km = int(input('Nhập số km: '))
tg_cho = int(input('Nhập thời gian chờ: '))
if loai_xe == 4:
    tien_cuoc = (so_km/0.8)*11000
    if so_km < 20:
        tien_di_chuyen = so_km * 12100
    else: 
        tien_di_chuyen = 20 * 12100 + (so_km - 20) * 10000
else:
    tien_cuoc = (so_km/0.8) * 13000
    if so_km < 20:
        tien_di_chuyen = so_km * 14100
    else: 
        tien_di_chuyen = 20 * 14100 + (so_km - 20) * 12000
if tg_cho < 5:
    tien_cho = 0
else: 
    tien_cho = (tg_cho - 5) * 800
print('Tiền chờ: ', tien_cho)
print('Tiền di chuyển: ', tien_di_chuyen)
print('Tiền cước: ', tien_cuoc)