so_giay = 997200
kim_giay = 0
kim_gio = 0
for giay in range(so_giay):
    kim_giay += 1
    if kim_giay % 3600 == 0:
        kim_gio += 1
print(f"Kim giây thực hiện số lần là: {kim_giay}")
print(f"Kim giờ thực hiện số lần là: {kim_gio}")