lua_chon = 0

while lua_chon != 6:
    print("\n===== MENU QUẢN LÝ SINH VIÊN =====")
    print("1. Thêm sinh viên")
    print("2. Hiển thị danh sách sinh viên")
    print("3. Tìm kiếm sinh viên theo MSSV")
    print("4. Cập nhật thông tin sinh viên")
    print("5. Xóa sinh viên")
    print("6. Thoát")
    print("==================================")

    nhap = input("Chọn chức năng (1-6): ")

    if nhap == "1":
        lua_chon = 1
        print("Bạn chọn: Thêm sinh viên")
    elif nhap == "2":
        lua_chon = 2
        print("Bạn chọn: Hiển thị danh sách sinh viên")
    elif nhap == "3":
        lua_chon = 3
        print("Bạn chọn: Tìm kiếm sinh viên theo MSSV")
    elif nhap == "4":
        lua_chon = 4
        print("Bạn chọn: Cập nhật thông tin sinh viên")
    elif nhap == "5":
        lua_chon = 5
        print("Bạn chọn: Xóa sinh viên")
    elif nhap == "6":
        lua_chon = 6
        print("Thoát chương trình. Tạm biệt!")
    else:
        print("Vui lòng nhập số từ 1 đến 6.")
