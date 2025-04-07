# Hàm xếp loại học lực
def xep_loai(diem):
    if diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

# Hàm nhập thông tin sinh viên
def nhap_sinh_vien():
    global so_luong, ten1, diem1, ten2, diem2, ten3, diem3

    so_luong = int(input("Nhập số sinh viên (tối đa 3): "))
    if so_luong > 3:
        print("Chỉ cho phép tối đa 3 sinh viên.")
        so_luong = 3

    for i in range(1, so_luong + 1):
        print(f"\n--- Nhập thông tin sinh viên {i} ---")
        ten = input("Nhập tên: ")
        diem = float(input("Nhập điểm: "))

        if i == 1:
            ten1 = ten
            diem1 = diem
        elif i == 2:
            ten2 = ten
            diem2 = diem
        elif i == 3:
            ten3 = ten
            diem3 = diem

# Hàm hiển thị kết quả sinh viên
def hien_thi_sinh_vien():
    if so_luong == 0:
        print("Chưa có dữ liệu sinh viên. Vui lòng nhập trước.")
        return

    print("\n===== DANH SÁCH SINH VIÊN =====")
    print("{:<5} {:<20} {:<10} {:<10}".format("STT", "Tên", "Điểm", "Xếp loại"))

    for i in range(1, so_luong + 1):
        if i == 1:
            print("{:<5} {:<20} {:<10} {:<10}".format(i, ten1, diem1, xep_loai(diem1)))
        elif i == 2:
            print("{:<5} {:<20} {:<10} {:<10}".format(i, ten2, diem2, xep_loai(diem2)))
        elif i == 3:
            print("{:<5} {:<20} {:<10} {:<10}".format(i, ten3, diem3, xep_loai(diem3)))
# Hàm tìm điểm cao nhất
def tim_diem_cao_nhat():
    if so_luong == 0:
        print("Chưa có dữ liệu sinh viên. Vui lòng nhập trước.")
        return

    max_diem = diem1
    ten_max = ten1

    if so_luong >= 2 and diem2 > max_diem:
        max_diem = diem2
        ten_max = ten2
    if so_luong == 3 and diem3 > max_diem:
        max_diem = diem3
        ten_max = ten3

    print(f"\nSinh viên có điểm cao nhất là: {ten_max} ({max_diem} điểm, xếp loại {xep_loai(max_diem)})")
# Hàm tính điểm trung bình của cả lớp
def tinh_diem_trung_binh():
    if so_luong == 0:
        print("Chưa có dữ liệu sinh viên. Vui lòng nhập trước.")
        return

    tong = 0
    if so_luong >= 1:
        tong += diem1
    if so_luong >= 2:
        tong += diem2
    if so_luong == 3:
        tong += diem3

    trung_binh = tong / so_luong
    print(f"\n Điểm trung bình của lớp là: {trung_binh:.2f}")
# Hàm chức năng đếm số sinh viên xếp loại Giỏi, Khá, Trung bình và Yếu
def thong_ke_xep_loai():
    if so_luong == 0:
        print("Chưa có dữ liệu sinh viên. Vui lòng nhập trước.")
        return

    gioi = kha = tb = yeu = 0

    for i in range(1, so_luong + 1):
        if i == 1:
            loai = xep_loai(diem1)
        elif i == 2:
            loai = xep_loai(diem2)
        elif i == 3:
            loai = xep_loai(diem3)

        if loai == "Giỏi":
            gioi += 1
        elif loai == "Khá":
            kha += 1
        elif loai == "Trung bình":
            tb += 1
        else:
            yeu += 1

    print("\nThống kê xếp loại:")
    print(f"Giỏi: {gioi} | Khá: {kha} | Trung bình: {tb} | Yếu: {yeu}")

# Khởi tạo các biến lưu thông tin sinh viên
so_luong = 0
ten1 = ten2 = ten3 = ""
diem1 = diem2 = diem3 = 0.0

# Chương trình chính sử dụng vòng lặp while
def main():
    while True:
        print("\n===== MENU CHƯƠNG TRÌNH =====")
        print("1. Nhập danh sách sinh viên")
        print("2. Hiển thị kết quả")
        print("3. Tìm sinh viên điểm cao nhất")
        print("4. Tính điểm trung bình của lớp")
        print("5. Thống kê xếp loại")
        print("6. Thoát chương trình")
        chon = input("Chọn chức năng (1–6): ")
        if chon == "1":
            nhap_sinh_vien()
        elif chon == "2":
            hien_thi_sinh_vien()
        elif chon == "3":
            tim_diem_cao_nhat()
        elif chon == "4":
            tinh_diem_trung_binh()
        elif chon == "5":
            thong_ke_xep_loai()
        elif chon == "6":
            print("Kết thúc chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Gọi hàm main để chạy chương trình
main()
