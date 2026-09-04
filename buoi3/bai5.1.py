import math
diem_a = (2, 3)
diem_b = (7, 8)
xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

'''Yêu cầu: tạo thêm danh sách cac_diem = [(0,0), (3,4), (6,8)] (list chứa các tuple tọa độ), dùng for để in ra
khoảng cách của từng điểm so với gốc tọa độ (0, 0).'''
cac_diem = [(0, 0), (3, 4), (6, 8)]
for diem in cac_diem:
    x, y = diem
    khoang_cach = math.sqrt(x ** 2 + y ** 2)
    print(f"Khoang cach giua {diem} va (0, 0) la: {round(khoang_cach, 2)}")