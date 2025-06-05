danhsach_sv = [
    {"name": "nguyễn Văn A", "GPA":2.5},
    {"name":"Nguyễn Văn b", "GPA":3.0},
    {"name":"nguyễn Văn C", "GPA":2.0}
]
filter_sv = list(filter(lambda danhsach_sv: danhsach_sv["GPA"]>=2.5, danhsach_sv))
print(filter_sv)
map_sv = list(map(lambda danhsach_sv:danhsach_sv["name"].title(), danhsach_sv))
print(map_sv)
