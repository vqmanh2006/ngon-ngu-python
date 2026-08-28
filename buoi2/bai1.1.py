
# Chu thich mot dong: khai bao thong tin sinh vien
"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""
ho_ten = "Tran Thi B" # bien luu ho ten
#ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))

'''Yêu cầu: giải thích vì sao phải ép kiểu int()/float() cho nam_sinh và diem_tb, trong khi ho_ten thì không
cần.
vì ho_ten là một chuỗi (string) nên không cần phải ép kiểu, còn nam_sinh và diem_tb là các giá trị số,
do đó cần phải ép kiểu int() cho nam_sinh để đảm bảo nó là một số nguyên và float() cho diem_tb để đảm bảo nó là một số thực,
việc ép kiểu giúp chương trình xử lý dữ liệu đúng cách và tránh lỗi khi thực hiện các phép toán hoặc so sánh.'''