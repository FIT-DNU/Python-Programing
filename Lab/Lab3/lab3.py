def nhap_danh_sach_sinh_vien():
    global danh_sach_sinh_vien, so_luong
    danh_sach_sinh_vien = []
    so_luong = int(input("Nhập số lượng sinh viên: "))
    for i in range(so_luong):
        ten = input(f"Nhập tên sinh viên thứ {i + 1}: ")
        danh_sach_sinh_vien.append(ten)
    return danh_sach_sinh_vien

def hien_thi_danh_sach_sinh_vien(danh_sach_sinh_vien):
    for i in range(so_luong):
        print(f'Tên sinh viên: {i + 1}: {danh_sach_sinh_vien[i]}')

def kiem_tra_ton_tai(ten):
    if ten in danh_sach_sinh_vien:
        print(f"Sinh viên {ten} có trong danh sách.")

def tim_kiem_sinh_vien(ten):
    ket_qua = danh_sach_sinh_vien.count(ten)
    print(f"Số lượng sinh viên có tên {ten} là: {ket_qua}")

def sua_thong_tin_sinh_vien(thu_tu):
    global danh_sach_sinh_vien
    ten_moi = input(f"Nhập tên sinh viên mới cho sinh viên thứ {thu_tu}: ")
    danh_sach_sinh_vien[thu_tu - 1] = ten_moi

def xoa_sinh_vien_khoi_danh_sach(ten):
    global danh_sach_sinh_vien
    if ten in danh_sach_sinh_vien:
        danh_sach_sinh_vien.remove(ten)
        print(f"Đã xóa sinh viên {ten} khỏi danh sách.")

def so_luong_khong_trung_lap():
    so_luong_khong_trung = len(set(danh_sach_sinh_vien)) # Sử dụng "set" để loại bỏ các phần tử trùng lặp
    print(f"Số lượng sinh viên không trùng lặp tên là: {so_luong_khong_trung}")

if __name__ == "__main__":
    while True:
        print("\n===== MENU CHƯƠNG TRÌNH =====")
        print("1. Nhập danh sách sinh viên")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Kiểm tra tên sinh viên có tồn tại trong lớp hay không")
        print("4. Tìm kiếm sinh viên theo tên (trả về số lượng)")
        print("5. Sửa thông tin sinh viên")
        print("6. Xoá sinh viên ra khỏi danh sách (xoá tên đầu tiên tìm thấy)")
        print("7. Đếm số lượng tên sinh viên trong danh sách (không tính trùng lặp)")
        print("8. Thoát chương trình")
        print("================================\n")
        lua_chon = int(input("Nhập lựa chọn của bạn (1-8): "))
        if lua_chon == 1:
            nhap_danh_sach_sinh_vien()
        elif lua_chon == 2:
            hien_thi_danh_sach_sinh_vien(danh_sach_sinh_vien)
        elif lua_chon == 3:
            ten = input("Nhập tên sinh viên cần kiểm tra: ")
            kiem_tra_ton_tai(ten)
        elif lua_chon == 4:
            ten = input("Nhập tên sinh viên cần tìm kiếm: ")
            tim_kiem_sinh_vien(ten)
        elif lua_chon == 5:
            thu_tu = int(input("Nhập thứ tự sinh viên cần sửa: "))
            sua_thong_tin_sinh_vien(thu_tu)
        elif lua_chon == 6:
            ten = input("Nhập tên sinh viên cần xoá: ")
            xoa_sinh_vien_khoi_danh_sach(ten)
        elif lua_chon == 7:
            so_luong_khong_trung_lap()
        elif lua_chon == 8: 
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")