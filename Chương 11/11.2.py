def nhap_ten_doi():
    so_doi = int(input("Nhập số đội: "))
    danh_sach_doi = []

    for i in range(so_doi):
        print("Nhập tên đội",i+1,end=":")
        ten_doi=input().split(",")
        danh_sach_doi.append(ten_doi)

    return danh_sach_doi
danh_sach_doi=nhap_ten_doi()
print("Danh sách các đội:", danh_sach_doi)
a=danh_sach_doi[-1]
b=a[1]
print("Tên của đội trưởng tệ nhất là:",b)