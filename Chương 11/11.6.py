list_chieu_cao_inch = [74,74,72,72,73,69,69,71,76,71]  #tao list
list_chieu_cao_met = []
for i in list_chieu_cao_inch:
    met = i * 0.0254
    list_chieu_cao_met.append(met)
print("Chieu cao sau khi doi tu inch sang met la: ",list_chieu_cao_met)

print("Ba chieu cao dau tien cua danh sach la: ",list_chieu_cao_met[0:3],end=' ')

print("Ba chieu cao cuoi cung cua danh sach la: ",list_chieu_cao_met[-3:])

print("Chieu cao trung binh cua danh sach la: ",sum(list_chieu_cao_met)/len(list_chieu_cao_met))

print("Chieu cao nho nhat la: ",min(list_chieu_cao_met))

print("Chieu cao lon nhat la: ",max(list_chieu_cao_met))

list_chieu_cao_met.sort()
print("Sap xep list theo gia tri tang dan: ",list_chieu_cao_met)

list_chieu_cao_met.sort()
list_chieu_cao_met.reverse()
print("Sap xep list theo gia tri gian dan: ",list_chieu_cao_met)