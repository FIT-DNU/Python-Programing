s1 ={"Nghĩa", "Hoàn", "An", "Quân"}
s2 ={"Dũng", "Quân", "Huy"}

# #Phép hợp (union)
# #Cách 1: Sử dụng union
# s = s1.union(s2)
# print("Danh sách: ",s)
# #Cách 2: Sử dụng toán tử |
# s3 = s1|s2
# print(s3)

# #Phép giao (intersection)
# s = s1.intersection(s2)
# print("Danh sách: ", s)
# #Sử dụng & 
# s3 = s1 & s2
# print(s3)

# #Phép hiệu (difference)
# s = s1.difference(s2)
# print(s)
# #Sử dụng toán tử -
# s3 = s1 - s2
# print(s3)

# #Phép hiệu đối xứng (symetric difference)
# s = s1.symmetric_difference(s2)
# print(s)
# #Sử dụng toán tử ^
# s3 = s1 ^ s2
# print(s3)