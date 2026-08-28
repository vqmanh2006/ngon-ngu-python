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