print("-----------------------------------------")
print("1. Hiển thị danh sách sinh viên")
print("2. Tìm kiếm sinh viên theo mã sinh viên")
print("3. Tìm kiếm sinh viên theo tên")
print("4. Tìm kiếm sinh viên theo ngày sinh")
print("5. Thêm sinh viên mới")
print("6. Cập nhật thông tin sinh viên")
print("7. Xoá sinh viên")
print("8. Lọc sinh viên theo lớp")
print("9. Tính điểm trung bình của từng sinh viên")
print("10. Thống kê số lượng sinh viên theo lớp")
print("-----------------------------------------")
lua_chon = int(input("Nhập lựa chọn của bạn: "))
if lua_chon == 1:
    print("Thực hiện chức năng: 1. Hiển thị danh sách sinh viên")
elif lua_chon == 2:
    print("Thực hiện chức năng: 2. Tìm kiếm sinh viên theo mã sinh viên")
elif lua_chon == 3:
    print("Thực hiện chức năng: 3. Tìm kiếm sinh viên theo tên")
elif lua_chon == 4:
    print("Thực hiện chức năng: 4. Tìm kiếm sinh viên theo ngày sinh")
elif lua_chon == 5:
    print("Thực hiện chức năng: 5. Thêm sinh viên mới")
elif lua_chon == 6:
    print("Thực hiện chức năng: 6. Cập nhật thông tin sinh viên")
elif lua_chon == 7:
    print("Thực hiện chức năng: 7. Xoá sinh viên")
elif lua_chon == 8:
    print("Thực hiện chức năng: 8. Lọc sinh viên theo lớp")
elif lua_chon == 9:
    print("Thực hiện chức năng: 9. Tính điểm trung bình của từng sinh viên")
elif lua_chon == 10:
    print("Thực hiện chức năng: 10. Thống kê số lượng sinh viên theo lớp")
else:
    print("Lựa chọn không phù hợp, yêu cầu thực hiện lại!")