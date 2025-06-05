thong_tin = {"masv":123456789, "ten":"Nguyễn Văn A", "lop":"CNTT18-13", "GPA":3.0, "tuoi":19}
print(thong_tin)
print(thong_tin["ten"])
print(thong_tin.get("tuoi", "khong co key tuoi"))
if "masv" in thong_tin:
    print("Key masv có tồn tại")
if "masv" not in thong_tin:
    print("Key masv không tồn tại")