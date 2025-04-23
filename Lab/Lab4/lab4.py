# === QUẢN LÝ SINH VIÊN ===
# 1. Thêm sinh viên mới
# 2. Hiển thị danh sách sinh viên
# 3. Tìm sinh viên theo mã
# 4. Cập nhật thông tin sinh viên
# 5. Xóa sinh viên
# 6. Thống kê điểm trung bình lớp
# 7. Thoát
# ========================

def them_sinh_vien(sinh_vien):
    mssv = input("Nhập mã SV: ")
    if mssv in sinh_vien:
        print("Mã đã tồn tại!")
        return
    ten = input("Họ tên: ")
    tuoi  = int(input("Tuổi: "))
    nghanh_hoc= input("Ngành: ")
    diem_trung_binh= float(input("Điểm TB: "))
    sinh_vien[mssv] = {"ten": ten, "tuoi": tuoi, "nghanh_hoc": nghanh_hoc, "diem_trung_binh": diem_trung_binh}
    print("Thêm sinh viên thành công.")

def hien_thi_danh_sach(sinh_vien):
    if not sinh_vien:
        print("Danh sách trống!")
        return
    print("Mã   | Họ tên           | Tuổi | Ngành | Điểm TB")
    for mssv, thong_tin in sinh_vien.items():
        print(f"{mssv} | {thong_tin['ten']:<15} |  {thong_tin['tuoi']}  | {thong_tin['nghanh_hoc']:<5} | {thong_tin['diem_trung_binh']}")

def tim_sinh_vien_theo_ma(sinh_vien):
    mssv = input("Nhập mã SV cần tìm: ")
    if mssv in sinh_vien:
        print(f"Mã: {mssv}")
        print(f"Họ tên: {sinh_vien[mssv]['ten']}")
        print(f"Tuổi: {sinh_vien[mssv]['tuoi']}")
        print(f"Ngành: {sinh_vien[mssv]['nghanh_hoc']}")
        print(f"Điểm TB: {sinh_vien[mssv]['diem_trung_binh']}")
    else:
        print("Không tìm thấy SV.")

def cap_nhat_thong_tin_sinh_vien(sinh_vien):
    mssv = input("Mã SV cần sửa: ")
    if mssv not in sinh_vien:
        print("Không tồn tại!")
        return
    # Giả sử chỉ sửa điểm và ngành học, do tên và tuổi ít kh thay đổi
    diem_trung_binh_moi = float(input("Điểm TB mới: "))
    nghanh_hoc_moi = input("Ngành học mới: ")
    sinh_vien[mssv]['diem_trung_binh'] = diem_trung_binh_moi
    sinh_vien[mssv]['nghanh_hoc'] = nghanh_hoc_moi
    print("Cập nhật thành công.")

def xoa_sinh_vien(sinh_vien):
    mssv = input("Mã SV cần xóa: ")
    if sinh_vien.pop(mssv, None):
        print("Xóa thành công.")
    else:
        print("Mã không tồn tại.")

def thong_ke_diem_trung_binh(sinh_vien):
    if not sinh_vien:
        print("Chưa có dữ liệu.")
        return
    tong_diem = sum(info['diem_trung_binh'] for info in sinh_vien.values())
    print("Điểm TB lớp:", tong_diem / len(sinh_vien))


if __name__ == "__main__":
    sinh_vien = {}
    while True:
        print("=== QUẢN LÝ SINH VIÊN ===")
        print("1. Thêm sinh viên mới")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Tìm sinh viên theo mã")
        print("4. Cập nhật thông tin sinh viên")
        print("5. Xóa sinh viên")
        print("6. Thống kê điểm trung bình lớp")
        print("7. Thoát")
        print("============================")

        lua_chon = int(input("Nhập lựa chọn của bạn (1–7): "))

        if lua_chon == 1:
             them_sinh_vien(sinh_vien)
        elif lua_chon == 2:
             hien_thi_danh_sach(sinh_vien)
        elif lua_chon == 3: 
            tim_sinh_vien_theo_ma(sinh_vien)
        elif lua_chon == 4: cap_nhat_thong_tin_sinh_vien(sinh_vien)
        elif lua_chon == 5:
            xoa_sinh_vien(sinh_vien)
        elif lua_chon == 6: 
            thong_ke_diem_trung_binh(sinh_vien)
        elif lua_chon == 7:
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")