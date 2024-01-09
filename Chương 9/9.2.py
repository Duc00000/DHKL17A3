n=int(input("Nhập vào năm: "))
can=["Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỷ"]
chi=["Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]
def tinh_can(n):
    can_index=n%10
    can_year=can[can_index]
    return can_year
def tinh_chi(n):
    chi_index=n%12
    chi_year=chi[chi_index]
    return chi_year
print("Năm",n,"lịch âm là năm",tinh_can(n),tinh_chi(n))