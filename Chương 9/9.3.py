chieu_cao=float(input("Nhập vào chiều cao:"))
can_nang=float(input("Nhập vào cân nặng:")) 
def tinh_bmi(chieu_cao,can_nang):
    bmi=can_nang/(chieu_cao**2)
    return bmi

bmi=tinh_bmi(chieu_cao,can_nang)
print(tinh_bmi(chieu_cao,can_nang))
def danh_gia(bmi):
    if bmi < 18.5:
        danh_gia="Gầy"
    elif 18.5 <= bmi <=24.99:
        danh_gia="Bình thường"
    else:
        danh_gia="Thừa cân"

    return danh_gia



print(danh_gia(bmi))  