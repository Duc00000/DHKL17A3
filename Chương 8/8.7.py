kwh=float(input("Nhập vào sô Kwh tiêu thụ: "))
if kwh <=50:
    print("Tổng tiền =",kwh*1678)
elif kwh <=100:
    print("Tổng tiền =",50*1678+(kwh-50)*1734)
elif kwh <=200:
    print("Tổng tiền =",50*1678+50*1734+(kwh-100)*2014)
elif kwh <= 300:
    print("Tổng tiền =",50*1678+50*1734+100*2014+(kwh-200)*2536)
elif kwh <= 400:
    print("Tổng tiền =",50*1678+50*1734+100*2014+100*2536+(kwh-300)*2834)
else:
    print("Tổng tiền =",50*1678+50*1734+100*2014+100*2536+100*2834+(kwh-400)*2927)   