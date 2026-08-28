ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))
#Với 3 biến đã nhập ở Bài tập 1.1, in ra một dòng thông tin bằng cả 3 cách:

# f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

# str.format()
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))

# toán tử %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))

''' Thảo luận: 3 cách trên cho kết quả giống nhau, vậy vì sao Python hiện nay khuyến khích dùng f-string hơn?
    Vì f-string đọc dễ hơn, viết nhanh hơn, và thường chạy nhanh hơn.'''

