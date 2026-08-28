'''Cho chuỗi họ tên nhập vào có khoảng trắng thừa và chữ hoa/thường lộn xộn, ví dụ " nguyễn
văn an ". Yêu cầu dùng strip(), split(), join() để: xóa khoảng trắng thừa ở đầu/cuối và
giữa các từ, sau đó viết hoa chữ cái đầu mỗi từ bằng phương thức title().'''

ho_ten_tho = " nguyen van an "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(ho_ten_sach) # Nguyen Van An