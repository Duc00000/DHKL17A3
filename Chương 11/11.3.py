list_animals=[]
print("Nhập vào con thú cần nhập:",end="")
x=input().split(",")
list_animals.append(x)
a=list_animals[-1]
print("List of animals:",a)
print("Number of animals:",len(a))
ten_thu_can_tim=input("I want to find:")
for i in a:
    if ten_thu_can_tim == i:
        print("There is",ten_thu_can_tim,"in list of animals")
        break
    else:
        print("There is no",ten_thu_can_tim,"in list of animals")
        break