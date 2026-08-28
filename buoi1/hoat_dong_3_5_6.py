"""Cho danh sách định danh sau, sinh viên xác định định danh nào hợp lệ, định danh nào sai và giải thích lý do:

1diem               gia-tri     _tam_thoi     Diem_TB
class               so luong    MAX_SPEED     diemTB
2024_data tong$     sinhVien1

-Định danh hợp lệ :"_tam_thoi", "Diem_TB", "class", "MAX_SPEED", "diemTB", "sinhVien1".
-Lý do hợp lệ : định danh hợp lệ chỉ được bắt đầu bằng chữ cái in hoa hoặc in thường hoặc bắt đầu bằng dấu gạch dưới(_)
cấu trúc định danh không được có các kí tự khác ngoài dấu gạch dưới(_) hoặc viết liền nhau.

-Định danh không hợp lệ : "1diem", "gia-tri", "so luong", "2024_data tong$".
-Lý do không hợp lệ: các định danh trên thường bắt đầu bằng số hay trong đó có các kí tự không hợp lệ như gạch ngang(-), khoảng cách( )."""
#Đặt lại tên biến cho đoạn code sau theo đúng chuẩn PEP8 (snake_case cho biến, UPPER_CASE cho hằng số).
#Yêu cầu: Viết lại đoạn code trên bằng tên biến chuẩn, sau đó thêm lệnh print() xuất ra toàn bộ thông tin.

#Ten = "Nguyen Van A"
#DiemToan = 8.5
#DiemVan = 7.0
#SoLuongMonHoc = 2
#MUCLUONGTOITHIEU = 5000000 # đây là một hằng số

# Tên biến được đặt lại:
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000 # đây là một hằng số
print("Ten : ", ten)
print("Diem Toan : ", diem_toan)
print("Diem Van : ", diem_van)
print("So Luong Mon Hoc : ", so_luong_mon_hoc)
print("Muc Luong Toi Thieu : ", MUC_LUONG_TOI_THIEU)

# Tính và in ra: a + b, a - b, a * b, a / b, a // b, a % b, a ** b
a = 17
b = 5
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

#Yêu cầu giải thích rõ sự khác nhau giữa / và //, giữa % với //.
""" Sự khác nhau giữa / và //:
- / (chia lấy phần thực): Toán tử này thực hiện phép chia và trả về kết quả dưới dạng số thực (float). Ví dụ: 17 / 5 = 3.4
- // (chia lấy phần nguyên): Toán tử này thực hiện phép chia và trả về kết quả dưới dạng số nguyên (int), bỏ qua phần thập phân. Ví dụ: 17 // 5 = 3
    Sự khác nhau giữa % và //:
- % (chia lấy dư): Toán tử này thực hiện phép chia và trả về phần dư của phép chia. Ví dụ: 17 % 5 = 2"""
""" Toán tử so sánh & logic:
Viết các biểu thức kiểm tra:
 -diem có đạt loại Khá (từ 6.5 đến dưới 8.0) hay không (kết hợp and).
 -tuoi có phải chưa đủ 18 hoặc trên 60 không (kết hợp or).
 -Phủ định lại điều kiện trên bằng not."""
 
diem = 6.5
tuoi = 20
if ( diem >= 6.5 and diem < 8.0):
    print("Điểm đạt loại Khá")
    
if ( tuoi < 18 or tuoi > 60):
    print("không")
    
if not ( diem >= 6.5 and diem < 8.0):
    print("Điểm không đạt loại Khá")
    """Toán tử gán & toán tử đặc biệt:
x = 10
x += 5 # tương đương x = x + 5
# Yêu cầu: viết tiếp với -=, *=, /=, //=, **= và in giá trị x sau mỗi bước
danh_sach1 = [1, 2, 3, "python"]
# Dùng toán tử "in" để kiểm tra 3 có trong danh_sach1 không
# Dùng toán tử "is" để so sánh 2 biến cùng tham chiếu tới 1 list """

x = 10
print("x =", x)
x += 5
print("x =", x)
x -= 3
print("x =", x)
x *= 2
print("x =", x)
x /= 4
print("x =", x)
x //= 2
print("x =", x)
x **= 3
print("x =", x)
danh_sach1 = [1, 2, 3, "python"]
danh_sach2 = danh_sach1
if 3 in danh_sach1:
    print("3 có trong danh_sach1")
if danh_sach1 is danh_sach2:
    print("danh_sach1 và danh_sach2 cùng tham chiếu tới 1 list")
    
# Độ ưu tiên toán tử: Dự đoán kết quả trước khi chạy, sau đó kiểm tra lại bằng Python:

print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)
#Ket qua du doan :  print(2 + 3 * 4 ** 2) : Độ ưu tiên sẽ là **, *, +, => 2 + 3 * 16 = 2 + 48 = 50
#Ket qua du doan :  print((2 + 3) * 4 ** 2) : Độ ưu tiên sẽ là (), **, *,  => (5) * 16 = 80
#Ket qua du doan :  print(10 > 5 and 3 < 1 or not False) : Độ ưu tiên sẽ là and, or, not => (True and False) or True = False or True = True

#Khai báo lần lượt các biến với nhiều kiểu dữ liệu khác nhau và in kiểu bằng type():
bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))
"""Câu hỏi: Vì sao cùng một biến bien có thể mang nhiều kiểu dữ liệu khác nhau trong Python? Điều này
khác gì so với khai báo biến trong C/C++/Java mà các bạn đã học (ví dụ int bien = 10;)?"""

""" việc cùng một biến có thể mang nhiều kiểu dữ liệu khác nhau trong Python là do Python là ngôn ngữ lập trình động (dynamic typing).
Trong Python không cần phải khai báo kiểu dữ liệu của biến trước khi sử dụng nó. Khi gán một giá trị mới cho biến,
Python sẽ tự động xác định kiểu dữ liệu của giá trị đó và thay đổi kiểu dữ liệu của biến tương ứng.
Trong các ngôn ngữ lập trình như C/C++/Java,ta phải khai báo kiểu dữ liệu của biến trước khi sử dụng nó."""

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