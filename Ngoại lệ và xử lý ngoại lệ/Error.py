# a = float(input("Nhập vào số thứ nhất: "))
# b = float(input("Nhập vào số thứ hai: "))
# try:
#     tong = a + b
#     hieu = a - b
#     tich = a * b
#     thuong = a / b
# except ZeroDivisionError:
#     print("Lỗi nhập vào số 0")
# except ValueError:
#     print("Nhập vào không phải là số")
# else:
#     print(tong)
#     print(hieu)
#     print(tich)
#     print(thuong)
# finally:
#     print("Chương trình kết thúc")

#Học IndexError

# sinhvien = [
#     {"name":"Vũ Trọng Anh", "age":19},
#     {"name":"Nguyễn Minh Đức", "age":10}
# ]
# try:
#     print(sinhvien[1])
# except IndexError:
#     print("Lỗi truy cập sai chỉ số")
# finally:
#     print("Chương trình kết thúc")

#Học KeyError

# monhoc = {
#     "tenmon":"Python", "Lop":"CNTT18-01"
#     }
# try:
#     print(monhoc["tenmon"])
# except KeyError:
#     print("Lỗi không tồn tại khóa")
# finally:
#     print("Chương trình kết thúc")

#Học TypeError

# a = 5
# b = 1
# try:
#     c = a + b
#     print(c)
# except TypeError:
#     print("Nhập sai kiểu dữ liệu")
# finally:
#     print("Kết thúc chương trình")

#Tự sinh ngoại lệ
def set_age(age):
    if age < 0:
        raise ValueError("Nhập sai kiểu dữ liệu")
    print("Tuổi", age)
try:
    age_input = int(input("Nhập tuổi: "))
    set_age(age_input)
except ValueError as e:
    print("Lỗi", e)