'''Yêu cầu: Viết chương trình cho phép nhập các thông tin sau và kiểm tra dữ liệu cơ bản, chỉ dùng biến,
toán tử và các phương thức String/Number đã học (chưa dùng if, kết quả kiểm tra chỉ cần in ra biến True/False):
 Họ tên → chuẩn hóa theo Bài tập 4.4.
 Số điện thoại (dạng chuỗi) → kiểm tra đủ 10 ký tự bằng len().
 Email → kiểm tra có chứa ký tự "@" bằng toán tử in (đã học Buổi 1).'''

ho_ten = input("Nhap ho ten: ")
sdt = input("Nhap so dien thoai: ")
email = input("Nhap email: ")
ho_ten_chuan = " ".join(ho_ten.split()).title()
sdt_hop_le = len(sdt) == 10
email_hop_le = "@" in email
print(f"Ho ten (da chuan hoa): {ho_ten_chuan}")
print(f"So dien thoai hop le (du 10 ky tu)? {sdt_hop_le}")
print(f"Email hop le (co ky tu @)? {email_hop_le}")