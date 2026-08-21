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