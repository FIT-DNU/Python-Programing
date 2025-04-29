def khoi_tao_du_lieu(ten_file):
    sinh_vien = {
        "SV001": {"Ho_ten": "Lê Thị Vân Anh", "Tuoi": 20, "Khoa": "CNTT", "Diem": 8.5},
        "SV002": {"Ho_ten": "Lê Thị Ngọc Châu", "Tuoi": 19, "Khoa": "Toán", "Diem": 7.0},
        "SV003": {"Ho_ten": "Lê Tuấn Anh", "Tuoi": 21, "Khoa": "Vật lý","Diem": 8.0},
    }
    try:
        with open(ten_file, 'w', encoding='utf-8') as f:
            for sid, info in sinh_vien.items():
                f.write(f"{sid}|{info['Ho_ten']}|{info['Tuoi']}|{info['Khoa']}|{info['Diem']}\n")
    except IOError as e:
        print("Lỗi khi tạo file mẫu:", e)
    else:
        print(f"Đã khởi tạo dữ liệu mẫu và lưu vào '{ten_file}'.")
    return sinh_vien


def doc_du_lieu_txt(ten_file):
    sinh_vien = {}
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            for line in f:
                sid, Ho_ten, Tuoi, Khoa, Diem = line.strip().split('|')
                sinh_vien[sid] = {
                    "Ho_ten":  Ho_ten,
                    "Tuoi":   int(Tuoi),
                    "Khoa": Khoa,
                    "Diem": float(Diem)
                }
    except FileNotFoundError:
        print(f"File '{ten_file}' không tồn tại.")
    except ValueError as e:
        print("Lỗi định dạng dữ liệu:", e)
    else:
        print(f"Đã tải {len(sinh_vien)} sinh viên từ '{ten_file}'.")
        print(sinh_vien)
    return sinh_vien

def luu_du_lieu_txt(ten_file, sinh_vien):
    try:
        with open(ten_file, 'w', encoding='utf-8') as f:
            for sid, info in sinh_vien.items():
                f.write(f"{sid}|{info['Ho_ten']}|{info['Tuoi']}|{info['Khoa']}|{info['Diem']}\n")
    except IOError as e:
        print("Lỗi khi ghi file:", e)
    else:
        print(f"Đã lưu {len(sinh_vien)} sinh viên ra '{ten_file}'.")


def them_sinh_vien(sinh_vien):
    try:
        sid = input("Mã SV: ").strip()
        if sid in sinh_vien:
            print("Mã đã tồn tại, không thể thêm.")
            return
        Ho_ten  = input("Họ tên: ").strip()
        Tuoi   = int(input("Tuổi: "))
        Khoa = input("Ngành: ").strip()
        Diem = float(input("Điểm TB: "))
    except ValueError:
        print("Tuổi hoặc điểm không hợp lệ.")
    else:
        sinh_vien[sid] = {"Ho_ten":Ho_ten, "Tuoi":Tuoi, "Khoa":Khoa, "Diem":Diem}
        print("Thêm thành công.")


def tim_sinh_vien(sinh_vien):
    sid = input("Mã SV cần tìm: ").strip()
    try:
        info = sinh_vien[sid]
    except KeyError:
        print("Không tìm thấy sinh viên.")
    else:
        print(f"{sid}: {info['Ho_ten']}, {info['Tuoi']} tuổi, {info['Khoa']}, điểm {info['Diem']}")


def cap_nhat_sinh_vien(sinh_vien):
    sid = input("Mã SV cần sửa: ").strip()
    try:
        info = sinh_vien[sid]
    except KeyError:
        print("Mã không tồn tại.")
        return
    try:
        Diem_moi = float(input("Điểm TB mới: "))
    except ValueError:
        print("Điểm phải là số.")
    else:
        info['Diem'] = Diem_moi
        print("Cập nhật điểm thành công.")

def xoa_sinh_vien(sinh_vien):
    sid = input("Mã SV cần xóa: ").strip()
    if sinh_vien.pop(sid, None):
        print("Xóa thành công.")
    else:
        print("Mã không tồn tại.")

def dem_sinh_vien(sinh_vien):
    print(f"Số sinh viên hiện có: {len(sinh_vien)}")

def tinh_diem_trung_binh(sinh_vien):
    try:
        avg = sum(info['Diem'] for info in sinh_vien.values()) / len(sinh_vien)
    except ZeroDivisionError:
        print("Chưa có dữ liệu sinh viên.")
    else:
        print("Điểm TB lớp:", avg)



if __name__ == "__main__":
    sinh_vien = {}
    while True:
        print("""
            === QUẢN LÝ SINH VIÊN (FILE TXT) ===
            1. Khởi tạo dữ liệu mẫu và lưu file .txt
            2. Đọc dữ liệu từ file .txt
            3. Lưu dữ liệu ra file .txt
            4. Thêm sinh viên mới
            5. Tìm sinh viên theo mã
            6. Cập nhật thông tin sinh viên
            7. Xóa sinh viên
            8. Đếm sinh viên hiện có
            9. Tính điểm trung bình lớp
            10. Thoát
            ===================================
            """)
        choice = input("Nhập lựa chọn của bạn (1–10): ").strip()
        if choice == '1':
            sinh_vien = khoi_tao_du_lieu('sinh_vien.txt')
        elif choice == '2':
            sinh_vien = doc_du_lieu_txt('sinh_vien.txt')
        elif choice == '3':
            ten_file = input("Nhập tên file cần lưu: ")
            luu_du_lieu_txt(ten_file, sinh_vien)
        elif choice == '4':
            them_sinh_vien(sinh_vien)
        elif choice == '5':
            tim_sinh_vien(sinh_vien)
        elif choice == '6':
            cap_nhat_sinh_vien(sinh_vien)
        elif choice == '7':
            xoa_sinh_vien(sinh_vien)
        elif choice == '8':
            dem_sinh_vien(sinh_vien)
        elif choice == '9':
            tinh_diem_trung_binh(sinh_vien)
        elif choice == '10':
            print("Chào tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

