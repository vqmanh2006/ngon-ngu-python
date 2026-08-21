"""Viết chương trình gán cứng họ tên và điểm 3 môn học, sau đó chỉ dùng biến và toán tử (số học, so
sánh, logic) đã học để:
-Tính điểm trung bình (toán tử số học).
-Kiểm tra các điều kiện xếp loại bằng biểu thức so sánh/logic, gán kết quả True/False vào biến rồi in
ra (chưa dùng if/elif/else)."""

ho_ten = "Vuong Quoc Manh"
Diem_toan = 8.5
Diem_ly = 7.0
Diem_hoa = 9.0
dtb = (Diem_toan + Diem_ly + Diem_hoa) / 3
xep_loai_gioi = dtb >= 8.0
xep_loai_kha = dtb >= 6.5 and dtb < 8.0
xep_loai_trung_binh = dtb >= 5.0 and dtb < 6.5
xep_loai_yeu = dtb < 5.0
print(ho_ten, "- DTB:", round(dtb, 2))
print("Điểm trung bình:", dtb)
print("Xếp loại giỏi:", xep_loai_gioi)
print("Xếp loại khá:", xep_loai_kha)
print("Xếp loại trung bình:", xep_loai_trung_binh)
print("Xếp loại yếu:", xep_loai_yeu)
print("Kiểu dữ liệu của biến xep_loai_gioi:", type(xep_loai_gioi))