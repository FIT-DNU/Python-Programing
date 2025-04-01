# Hàm xếp loại theo điểm
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
    global so_luong
    global ten1, diem1, ten2, diem2, ten3, diem3

    so_luong = int(input("Nhập số sinh viên (tối đa 3): "))
    if so_luong > 3:
        print("Chỉ cho phép tối đa 3 sinh viên.")
        so_luong = 3

    if so_luong >= 1:
        print("\n--- Sinh viên 1 ---")
        ten1 = input("Nhập tên: ")
        diem1 = float(input("Nhập điểm: "))
    if so_luong >= 2:
        print("\n--- Sinh viên 2 ---")
        ten2 = input("Nhập tên: ")
        diem2 = float(input("Nhập điểm: "))
    if so_luong == 3:
        print("\n--- Sinh viên 3 ---")
        ten3 = input("Nhập tên: ")
        diem3 = float(input("Nhập điểm: "))

# Hàm hiển thị kết quả sinh viên
def hien_thi_sinh_vien():
    if so_luong == 0:
        print("Chưa có dữ liệu. Vui lòng nhập trước.")
        return

    print("\n===== DANH SÁCH SINH VIÊN =====")
    print("{:<5} {:<20} {:<10} {:<10}".format("STT", "Tên", "Điểm", "Xếp loại"))

    if so_luong >= 1:
        print("{:<5} {:<20} {:<10} {:<10}".format(1, ten1, diem1, xep_loai(diem1)))
    if so_luong >= 2:
        print("{:<5} {:<20} {:<10} {:<10}".format(2, ten2, diem2, xep_loai(diem2)))
    if so_luong == 3:
        print("{:<5} {:<20} {:<10} {:<10}".format(3, ten3, diem3, xep_loai(diem3)))

# Biến khởi tạo ban đầu
so_luong = 0
ten1 = ten2 = ten3 = ""
diem1 = diem2 = diem3 = 0.0

# Chương trình chính
def main():
    while True:
        print("\n===== MENU CHƯƠNG TRÌNH =====")
        print("1. Nhập danh sách sinh viên")
        print("2. Hiển thị kết quả")
        print("3. Thoát")

        chon = input("Chọn chức năng (1–3): ")

        if chon == "1":
            nhap_sinh_vien()
        elif chon == "2":
            hien_thi_sinh_vien()
        elif chon == "3":
            print("Kết thúc chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Gọi hàm main
main()
